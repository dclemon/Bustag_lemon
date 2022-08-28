#!/usr/bin/env python
# coding=utf-8
import json
import os
import base64
import time
import random
import re
import argparse
from urllib.parse import quote
from urllib.parse import unquote
import requests
from bustag.app import cut


VERSION = "0.1.0"





session = requests.Session()

TID_URL = "https://ux.xiaoice.com/beautyv3"
IMG_URL = "https://ux.xiaoice.com/api/image/UploadBase64?exp=1"
SCORE_URL = "https://ux.xiaoice.com/api/imageAnalyze/Process?service=beauty"


def get_tid(personal_aiid):
    """
    获取 tid
    """
    head1 = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "Referer": "https://ux.xiaoice.com/PersonalizedBeauty?aiid="+personal_aiid,
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    try:
        req = session.get(TID_URL, headers=head1)
        a = unquote(req.cookies.get('logInfo'))

        tid = json.loads(a)['tid']


        return tid

    except Exception:
        pass


def get_img_url(img_path, personal_aiid):
    """
    获取图片地址
    """
    file = base64.b64encode(open(img_path, "rb").read())
    head1 = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "Referer": "https://ux.xiaoice.com/PersonalizedBeauty?aiid="+personal_aiid,
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    try:

        req = session.post(IMG_URL, headers=head1, data=file).json()

        return req["Host"] + req["Url"]
    except Exception:
        pass



def get_score(img_path, personal_aiid):
    """
    获取颜值测试评价
    """
    current = str(int(time.time()))
    msg_id = current + str(random.randint(100, 999))
    tid = get_tid(personal_aiid)

    forms = {
        "MsgId": msg_id,
        "CreateTime": current,
        "TraceId": tid,
        "Content": {"imageUrl": get_img_url(img_path, personal_aiid),"Metadata":{"UI.Image.AIId":personal_aiid}}
    }
    head2 = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "cpid=83e4223b56c07ecc2b97854101f950db; Hm_lvt_a9eb3172d11530f19707197df6a7b845=1661083700; salt=05675341C3349369DE1FFBD8A80A83C7; cookieid=bb18efcaefc84f2dae2e6e93f19054ec; uidcode=A3fWeu6F3Nvo8VIO_49T1uJtEn6r--Gkc0zMjwKq0rWeEdE86v2kYvYNTEvHb5H1GhHypJjJqCGkDp3JkhXHPHn_s97hhA; af_binded_aiid=bpb3c9d08397070e59b88c82380e58286a; logInfo=%7B%22pageName%22%3A%22beautyv3%22%2C%22tid%22%3A%22a3995ef4c01fa9d7df86a4df7505cc6c%22%7D",
        "Referer": "https://ux.xiaoice.com/PersonalizedBeauty?aiid="+personal_aiid,
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    req = requests.post(SCORE_URL, headers=head2, data=str(forms))
    try:
        req=req.json()


    except Exception:
        print(req)
        pass
    try:
        print("我的评价是：" + str(req["content"]["metadata"]['score']) + "分")
        return req["content"]["metadata"]['score']
    except:
        print('未能识别出颜值')
        return 0
def like(fanhao):
    #给数据库里的番号标喜欢，注意不能是推荐里的番号
    url = "http://127.0.0.1:8880/tag/"+fanhao+"?page=1&like=None"
    head = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "upgrade-insecure-requests": "1",
    "cookie": "_SSID=DFVRstr1k8Ff2EkJWCN8pgZGztxjScHLde6MtX9Cfg8; did=SlYuXAiGHYb0KOqLTeFg_5ILGEj-mRh3PY-leMaoIQV8FX3C-GRMmNU-gMkNBKhKAMMA-7XbbNMycU2yMRKiiw; _CrPoSt=cHJvdG9jb2w9aHR0cDo7IHBvcnQ9NTAwMDsgcGF0aG5hbWU9Lzs%3D; stay_login=1; id=vYQHip-6SF0NhYBNaGFFHs8bS598dt9UHK0slASSIEUa3fPj0jglxOOL9q1SA0xgu6qF9NgSbmlP3zKZiZIcJs; litewait-v1-userauth-nonsec8002=xxxcookie",
    "Referer": "http://127.0.0.1:8877/tagit?",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
    body = "formid=form-1&submit=1"
    requests.post(url,headers=head, data=body)


    return
def dislike(fanhao):
    #给数据库里的番号标不喜欢，注意不能是推荐里的番号
    url = "http://127.0.0.1:8880/tag/"+fanhao+"?page=1&like=None"
    head = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "upgrade-insecure-requests": "1",
    "cookie": "_SSID=DFVRstr1k8Ff2EkJWCN8pgZGztxjScHLde6MtX9Cfg8; did=SlYuXAiGHYb0KOqLTeFg_5ILGEj-mRh3PY-leMaoIQV8FX3C-GRMmNU-gMkNBKhKAMMA-7XbbNMycU2yMRKiiw; _CrPoSt=cHJvdG9jb2w9aHR0cDo7IHBvcnQ9NTAwMDsgcGF0aG5hbWU9Lzs%3D; stay_login=1; id=vYQHip-6SF0NhYBNaGFFHs8bS598dt9UHK0slASSIEUa3fPj0jglxOOL9q1SA0xgu6qF9NgSbmlP3zKZiZIcJs; litewait-v1-userauth-nonsec8002=xxxcookie",
    "Referer": "http://127.0.0.1/tagit?",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }
    body = "formid=form-1&submit=0"
    requests.post(url,headers=head, data=body)


    return
def yes(fanhao, islike):
    head = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "Referer": "http://127.0.0.1:8880/",
        "Referrer-Policy": "strict-origin-when-cross-origin"}
    body = 'formid=form-1&submit=1'
    url = "http://127.0.0.1:8880/correct/" + fanhao + "?page=1&like="+islike

    requests.post(url, headers=head, data=body)
    return


def nope(fanhao, islike):
    head = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "Referer": "http://127.0.0.1:8880/",
        "Referrer-Policy": "strict-origin-when-cross-origin"}
    body = 'formid=form-1&submit=0'
    url = "http://127.0.0.1:8880/correct/" + fanhao + "?page=1&like=" + islike

    requests.post(url, headers=head, data=body)
    return




if __name__ == "__main__":
    '''
    基本流程：
    1.读取\src\\bustag\\app\\data内的db数据库
    2.查找数据表item-rate中type为2的值（表示未打标过）
    3.获取其iten_id（番号），交给机器人评分
    4.分数1<x<8.8的dislike(),x>8.8的like()
    5.设计一个网页用于触发程序命名为/autotag
    '''
    #cut.cut_face("111.png")
    get_score("222.png", "bpb3c9d08397070e59b88c82380e58286a")
    #like("HUNTB-351")

