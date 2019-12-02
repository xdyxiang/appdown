### **目录**：
* static 存放静态文件
    1. bootstrapsrc 存放bootstrap的资源文件
    2. iosplist 存放iosplist文件，该文件夹是一个git仓储，会把plist同步到github
    3. pkg 存放安装包文件，通过flask服务，提供包下载
* templates 存放html文件

* venv python虚拟环境

* app  程序入口

* git_action git相关函数，文件对比等

* plist_template plist的模板，用于生成plist文件 






***
### **使用教程**
1. 安装好git
2. 安装好python3.6  `安装python库：pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`
3. git 建立 iosplist仓库  `拉取git：git clone https://6b62c6d1573e252ca083419575508075419e690e@github.com/dengyouxinviabtc/iosplist.git`

* 启动程序：`python -m flask run -h 0.0.0.0 -p 5000`
* 


### Dockerfile的运行方式
1.找个地方放置pkg文件夹，里面的结构跟static/pkg 一致,保存git密码git config --global credential.helper store
2.运行docker：``docker run -d -p 5000:5000 --restart=unless-stopped  --name appdown -v pkg:/appdown/static/pkg appdown:v1 sh`

