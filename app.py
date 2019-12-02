from flask import Flask, request, redirect
from flask import render_template
import os,time
from git_action import check_github,diff_pkg_plist,gitdir

# 自己创建git仓库，仓库名iosplist，底下有两个项目的文件夹viawallet，pool

githome = "https://gitee.com/dengyouxinviabtc/{0}".format(gitdir)

app = Flask(__name__)

@app.route('/')
def hello_world():
    # os.path.getctime() 函数是获取文件最后创建时间
    # os.path.getmtime() 函数是获取文件最后修改时间
    # viawallet
    ios_filelist = os.listdir("./static/pkg/iOS/viawallet")
    ios_filelist1 = sorted(ios_filelist, key=lambda x: os.path.getmtime(os.path.join("./static/pkg/iOS/viawallet", x)),reverse=True)
    ios_filelist_new = [(i,time_convert(os.path.getmtime(os.path.join("./static/pkg/iOS/viawallet", i)))) for i in ios_filelist1]
    android_filelist = os.listdir("./static/pkg/Android/viawallet")
    android_filelist1 = sorted(android_filelist, key=lambda x: os.path.getmtime(os.path.join("./static/pkg/Android/viawallet", x)),reverse=True)
    android_filelist_new = [(i, time_convert(os.path.getmtime(os.path.join("./static/pkg/Android/viawallet", i)))) for i in android_filelist1]

    # pool
    pool_ios_filelist = os.listdir("./static/pkg/iOS/pool")
    pool_ios_filelist1 = sorted(pool_ios_filelist, key=lambda x: os.path.getmtime(os.path.join("./static/pkg/iOS/pool", x)),reverse=True)
    pool_ios_filelist_new = [(i,time_convert(os.path.getmtime(os.path.join("./static/pkg/iOS/pool", i)))) for i in pool_ios_filelist1]
    pool_android_filelist = os.listdir("./static/pkg/Android/pool")
    pool_android_filelist1 = sorted(pool_android_filelist, key=lambda x: os.path.getmtime(os.path.join("./static/pkg/Android/pool", x)),reverse=True)
    pool_android_filelist_new = [(i, time_convert(os.path.getmtime(os.path.join("./static/pkg/Android/pool", i)))) for i in pool_android_filelist1]

    return render_template('hello.html', ios_filelist=ios_filelist_new,android_filelist= android_filelist_new,pool_ios_filelist=pool_ios_filelist_new,pool_android_filelist= pool_android_filelist_new)

@app.route('/ios/viawallet', methods=['POST'])
def ios_viawallet():
    version = ""
    if request.method == 'POST':
        if request.form['version']:
            version = request.form['version']
            # 检查iosplist文件夹是否有该plist
            diff_pkg_plist("viawallet")
            # 检查仓库是否推送最新
            check_github()
            filename = version.split(".ipa")[0]
            return redirect('itms-services://?action=download-manifest&url={0}/raw/master/viawallet/{1}.plist'.format(githome,filename))
        else:
            version = "找不到选定版本"
            return version
    return "参数错误"

@app.route('/android/viawallet', methods=['POST'])
def android_viawallet():
    version = ""
    if request.method == 'POST':
        if request.form['version']:
            version = request.form['version']
            filename = version.split('(')[0]
            return redirect('/static/pkg/Android/viawallet/{0}'.format(filename))
        else:
            version = "找不到选定版本"
            return version

    return "参数错误"

@app.route('/ios/pool', methods=['POST'])
def ios_pool():
    version = ""
    if request.method == 'POST':
        if request.form['version']:
            version = request.form['version']
            # 检查iosplist文件夹是否有该plist
            diff_pkg_plist("pool")
            # 检查仓库是否推送最新
            check_github()
            filename = version.split(".ipa")[0]
            return redirect('itms-services://?action=download-manifest&url={0}/raw/master/pool/{1}.plist'.format(githome,filename))
        else:
            version = "找不到选定版本"
            return version
    return "参数错误"

@app.route('/android/pool', methods=['POST'])
def android_pool():
    version = ""
    if request.method == 'POST':
        if request.form['version']:
            version = request.form['version']
            filename = version.split('(')[0]
            return redirect('/static/pkg/Android/pool/{0}'.format(filename))
        else:
            version = "找不到选定版本"
            return version

    return "参数错误"



def time_convert(time_int):
    ltime = time.localtime(time_int)
    return time.strftime('%Y-%m-%d %H:%M:%S',ltime)


if __name__ == '__main__':
    app.run()
    # 命令行 python -m flask run -h 0.0.0.0 -p 5000
