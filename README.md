# Bustag_lemon
基于gxtrobot的bustag修复版，修复了图片不显示的问题，增加了代理功能，增加了AI颜值评分功能

Bustag 是一个基于我开发的 python 异步爬虫框架开发aspider的自动车牌推荐系统, 系统原理为定时爬取最新车牌信息, 然后可以对车牌进行打标(标示是否喜欢), 打标车牌到一定数量可以进行训练并生成模型, 以后就可以基于此模型自动对下载的车牌进行预测是否喜欢, 可以过滤掉大量不喜欢的车牌, 节约时间

原项目地址：https://github.com/gxtrobot/bustag

使用方法（群晖）

1.新建一个容器，https://registry.hub.docker.com/r/aiastia/bustag/

2.把项目上传到群晖

3.把项目的根目录文件夹映射为/app

5.config.ini内填写你的本地代理（不支持socks5，必须转为http代理才可使用）

6.去微软小冰申请一个自己的AI评分接口，例如:https://ux.xiaoice.com/PersonalizedBeauty?aiid=bpb3c9d08397070e59b88c82380e58286a&mode=share&share=1
在config的personal_aiid内填上链接里的aiid,即为bpb3c9d08397070e59b88c82380e58286a

目前点击打分一次只会处理10条数据,可以通过圈X或者python设定定时post任务

目前的BUG：貌似打包的镜像有问题，容器启动后爬取过程中容易卡死导致爬不到数据，首页不给推荐。由于我不太熟悉dockerfile，目前还没有解决。可以安装https://registry.hub.docker.com/r/aiastia/bustag/
这个镜像，映射好需要的路径，启动后进入docker,pip install需要的包完善环境后即可正常爬取。



效果截图：

添加代理
![MR`A(2410KVDVTV23GD(EY0](https://user-images.githubusercontent.com/63597032/186806355-ff3bb774-3fd3-4266-b1bd-38e156ebd63c.png)

AI打分

![W4WN 0IZLGAI6EQY@ Z9`67](https://user-images.githubusercontent.com/63597032/187053081-13578adc-0b9e-44e4-be7c-1cabde551698.png)
