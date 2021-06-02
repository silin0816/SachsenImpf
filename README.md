# SachsenImpf(just for fun)

这是一个利用Selenium创建的类似于按键精灵的Covid/19的也**页面刷新器**。


# 准备
* 1 python 3.x
* 2 安装Selenium, 可利用pip或者conda (输入命令conda install -c conda-forge selenium)
* 3 根据chrome的版本选择安装相应的浏览器驱动，例如chromedriver, foxfiredriver 例如chrome:<https://chromedriver.chromium.org/downloads 建议安装在C:\Program Files (x86)， 不然需要修改PATH为安装路径

# 变量
* 1 ACCOUNT: 注册获取的账户号
* 2 PWD: 注册时填入的密码
* 3 PATH: 安装driver的地址 默认(C:\Program Files (x86)\chromedriver.exe)

# 刷新频率
刷新频率主要由termin_update()里的sleep time 决定

# 建议
* 1 目前该刷新器用默认的刷新日期，如果时昨天打开的刷新器今天便会失效因为他不能选择该日期之前的日期
* 2 每周一三五放出新的termin，一般建议在放出termin前至少一个小时进入，不然由于太拥挤就无法进入系统，只要进入系统后，由于刷新器在不断刷新就不会被自动踢出
* 3 该刷新器有termin会发出声音和发送邮件功能(被注释掉了)，邮件功能需要开启SMTP功能(个人觉得有点鸡肋)


# 待完成
* 1 日期选择
* 2 parner 设置
* 3 

