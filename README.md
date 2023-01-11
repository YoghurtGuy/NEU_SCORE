# NEU_SCORE东北大学成绩公布推送

检测东北大学NEU教务处成绩是否有更新（是否有新出成绩），有更新则通知

1. ### 简介

   利用Github Actions来实现自动化运行，score.py实现主要功能，score_num.js记录已有成绩科目数，以便进行比对。

   检测时间为北京时间为8:05-23:05,检查间隔为30min。您可以在/.github/workflows/main.yml中修改，但是建议不要太频繁，可能会被学校管理员限制。

2. ### 推送

   1. 默认使用pushkey进行推送（**对iOS来说比较好用**，安卓建议使用其他方式）。打开[Pushdeer官网](http://www.pushdeer.com/) 在里面下载iOS或Android APP，在安装、登录和注册后会得到一个key，下一步中我们会用到。
   2. 其次支持Server酱(ServerChan)渠道(可以通过微信、钉钉等推送，但免费版**仅支持标题推送**，因此可能**无法推送具体成绩，仅通知新公布成绩的科目**），打开[Server酱官网](https://sct.ftqq.com/)，配置通道、绑定相关渠道后，得到一个Key,下一步中我们会用到。
   3. 以上两种方式会通过key自动识别对应通道，你可以选择使用自己的推送方式，可以联系我增加渠道，或者需要自行修改score.py文件里的NEU类里的push函数。

3. ### 使用

   1. 首先Fork本项目

   2. 设置您的信息

      打开仓库的Settings >> Secrets >> Actions >> new repository secret，依次填写name为SID,PASSWORD,PUSHKEY, Value为你的学号，密码，第二步推送获得的key。

      记住是每次填写一个！比如第一次填写SID和学号！

   3. 打开Actions

      最后到仓库的Actions页，看到有一个灰色的叫“CI”的workflow，点开后点击右侧 enable workflow

   4. 如果想要推送时不推送具体成绩，可自行修改score.py文件里第九行send_score_detail = False

4. ### 参考

   NEU统一身份登录部分代码参考了[NEU_health_daka](https://github.com/Bmaili/NEU_health_daka)，感谢作者Bmaili！

### 如果有任何问题可以Issues给我，或者联系我的邮箱leftongyu@gmail.com，转载请注明
