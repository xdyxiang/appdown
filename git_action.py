from git import Repo
import os

gitdir = "iosplist"  # github文件名，在static目录下，建立git仓库，建立相应项目的文件夹
server_host = "http://10.1.5.33:5000" # 服务器的地址

def check_github():
    # 判断本地文件是否更新，更新则推送更新
    # clone_repo = Repo.clone_from(url='https://6b62c6d1573e252ca083419575508075419e690e@github.com/dengyouxinviabtc/iosplist.git', to_path='./static/iosplist')
    # 新建版本库对象(先建立好仓库)
    repo = Repo("./static/{0}".format(gitdir))
    git = repo.git  # 通过Repo对象获取git对象
    # 版本库中未跟踪的文件列表
    if repo.untracked_files:        # 未被管理的文件
        git.add('*')  # git add test1.txt

    if repo.is_dirty():    # 判断是否有变更
        git.commit('-am', 'data had changed')  # git commit -m 'this is a test'
        # # 获取版本库暂存区
        # index = repo.index
        # # 添加修改文件
        # index.add(["viabtc_wallet_release.plist"])
        # # 提交修改到本地仓库
        # index.commit('this is a test')
        # 获取远程仓库
        remote = repo.remote()
        # 推送本地修改到远程仓库
        remote.push()
        print("已推送最新plist 到github")
    else:
        print("未有新增plist")


def diff_pkg_plist(project):
    # 比较IOS包文件夹的文件名 与 iosplist文件夹的文件名是否一致，不一致则增加一个plist
    # 获取IOS包文件夹的文件名
    ios_name_list = os.listdir('./static/pkg/iOS/{0}'.format(project))
    iospilist_name_list = os.listdir('./static/{0}/{1}'.format(gitdir,project))
    ios_name_list1 = [element.split(".ipa")[0] for element in ios_name_list]
    iospilist_name_list1 = [element.split(".plist")[0] for element in iospilist_name_list if element.endswith(".plist")]
    # 对比他们的文件名,iosname有，但iosplist中没有 的名称
    diff = set(ios_name_list1).difference(set(iospilist_name_list1))
    if diff:
        # 增加plist文件
        for filename in diff:
            create_plist(filename,project)
    else:
        print("viawallet pkg 与 iosplist一致")

    # 对比他们的文件名,iosname没有，但iosplist中有 的名称
    diff2 = set(iospilist_name_list1).difference(set(ios_name_list1))
    if diff2:
        # 增加plist文件
        for filename2 in diff2:
            delete_plist(filename2,project)
    else:
        print("iosplist 与 viawallet pkg 一致")

def create_plist(filename,project):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    old_file = "./plist_template.plist"
    old_str1 = "pkgurl"  # plist_template.plist 里面的字符串
    new_str1 = "{0}/static/pkg/iOS/{1}/{2}.ipa".format(server_host,project,filename)
    new_file = "./static/{0}/{1}/{2}.plist".format(gitdir,project,filename)
    with open(old_file, "r", encoding="utf-8") as f1, open(new_file, "w", encoding="utf-8") as f2:
        for line in f1:
            if old_str1 in line:
                line = line.replace(old_str1, new_str1)
            if "pkgname" in line:
                line = line.replace("pkgname", filename)
            f2.write(line)

def delete_plist(filename,project):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"static/{0}/{1}/".format(gitdir,project))
    filepath = path + "{0}.plist".format(filename)
    if (os.path.exists(filepath)):
        os.remove(filepath)
        print('移除:{0}'.format(filepath))
    else:
        print("要删除的文件:{0}不存在！".format(filepath))

# create_plist("wa_12.12")
# diff_pkg_plist()
# check_github()
# print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"static/iosplist/viawallet/"))
