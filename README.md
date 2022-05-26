# XiudongTicket
基于Python的秀动抢票插件

1.准备
chromedriver 程序需要下载一下
https://chromedriver.chromium.org/downloads
py文件中其余所需要第三方依赖库 通过pip install xx 控制台安装即可
自行百度下载安装过程 ，较为简单

2.入参
event：在需要购票的链接中直接查看
ticketid：网页检查源代码定位对应票种可看到对应ticketid
ticketnum：购票数量 自行传入

3.运行
1）main方法
先运行mian 会调用flask使用本地路径端口执行，"127.0.0.1:9997"
2）浏览器执行登录购票操作
提供了两个 api
一个是跳转到登录页面，请自行登录 （127.0.0.1:9997/login
一个是通用购买演出票 api，请自行传入对应参数, 支持定时功能 /buy?event=xxx&ticketId=xxx&cron_time=xxx （127.0.0.1:9997/buy
如果多次刷新 login 且登录页面没有进行登录，可能会存在线程阻塞问题，因为 max_workers 设置了 10 个, 暂时可以通过关闭窗口解决
如果确认订单页面显示已售罄，需要不断刷新直到出现立即支付，这一点在捡漏的时候很有用
只是给大家提供点思路，其他请自行阅读代码，祝大家好运

Updata 2022-5-26
test：测试抢购姜云升演出，可以正常登录使用selenium调用浏览器。
![545c0ec374b829c56a9ac891832f589](https://user-images.githubusercontent.com/50318531/170515312-c957d12f-188a-47ab-835e-89bde5f855d9.png)


4.欢迎讨论技术上问题，需要帮忙调试可以联系wechat:15818337112提供有偿解答
*
https://github.com/yangn0/Xiudong-Script -> 提供了思路
