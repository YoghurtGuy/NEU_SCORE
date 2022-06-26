# ValueNEU_SCORE
检测东北大学NEU教务处成绩是否有更新（是否有新出成绩），有更新则通知

1. ### 简介

   利用Github Actions来实现自动化运行，score.py实现主要功能，score_num.js记录已有成绩科目数，以便进行比对。

2. ### 推送

   我使用的是pushkey进行推送（对ios来说比较好用，安卓建议使用其他方式），你可以选择使用自己的推送方式，需要自行修改score.py文件里的NEU类里的push函数。

   Pushdeer官网：http://www.pushdeer.com/在里面下载ios，或Android APP，在安装和登录后会得到一个key，下一步中我们会用到。

3. ### 使用

   1. 首先Fork本项目

   2. 设置您的信息

      打开仓库的Settings >> Secrets >> Actions >> new repository secret，依次填写name为SID,PASSWORD,PUSHKEY, Value为你的学号，密码，第二步的key。

      记住是每次填写一个！比如第一次填写SID和学号！

   3. 打开Actions

      最后到仓库的Actions页，看到有一个灰色的叫“CI”的workflow，点开后点击右侧 enable workflow

### 如果有任何问题可以Issues给我，如果搞不定其他推送方式，我也可以帮忙code，或者联系我的邮箱leftongyu@gmail.com，转载请注明





