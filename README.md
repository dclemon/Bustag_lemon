# Bustag_lemon
gxtrobot的bustag修复版，修复了图片不显示的问题，增加了代理功能

使用方法（群晖）
1.新建一个容器，推荐使用https://registry.hub.docker.com/r/aiastia/bustag/
2.把项目上传到群晖
3.把项目目录内的bustag文件夹映射为/app/src/bustag
4.把项目目录内的data文件夹映射为/app/data
5.config.ini内填写你的本地代理（不支持socks5，必须转为http代理才可使用）

映射参数：
![I(8UBAA{$KZMHGKM%9) Q7R](https://user-images.githubusercontent.com/63597032/186806313-183e7b9c-3d6d-472c-9af2-e9b3de94005c.png)

效果截图：

![MR`A(2410KVDVTV23GD(EY0](https://user-images.githubusercontent.com/63597032/186806355-ff3bb774-3fd3-4266-b1bd-38e156ebd63c.png)
