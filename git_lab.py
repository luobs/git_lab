#coding=utf-8
import subprocess
import os,sys

PATH = os.path.abspath('.') + '/.git'
FilePath = os.path.exists(PATH)

#链接gitlab
def ccccs():
    sshCmd = 'ssh -T git@git.workec.com'
    process = subprocess.Popen(sshCmd,stdout=subprocess.PIPE,shell = True)
    process.wait()
    (stdoutdata, stderrdata) = process.communicate()
    if 'Welcome to GitLab' in stdoutdata:
        branlist = []
        print stdoutdata
        #查看本地和远程分支
        #branchCmd = 'git branch -a'
        branchCmd = 'git branch -r'
        process = subprocess.Popen(branchCmd,stdout=subprocess.PIPE,shell = True)
        process.wait()
        (stdoutdata, stderrdata) = process.communicate()
        branlist = stdoutdata.split('\n')
        for i in range(len(branlist)-1):
            print '%d %s'%(i,branlist[i])
        print '\n'
        return branlist
    else:
        print stdoutdata
        print 'Erorr:Please set ssh rsa.pub of Gitlab setting!'

def xxxxd(branlist,index):
    index = int(index)
    #抓取远程最新分支（所有分支）
    print '\n','Start fetch news ...'
    fetchCmd = 'git fetch'
    process = subprocess.Popen(fetchCmd,shell = True)
    process.wait()
    #合并到当前分支
    print '\n','Start rebase%s ...'%branlist[index]
    rebaseCmd = 'git rebase%s'%branlist[index]
    process = subprocess.Popen(rebaseCmd,stdout=subprocess.PIPE,shell = True)
    process.wait()
    (stdoutdata, stderrdata) = process.communicate()
    print stdoutdata
    #解决冲突
    if 'It seems that there is already' in stdoutdata:
        rmCmd = 'rm -fr /Users/mac/ECLite/.git/rebase-apply'
        process = subprocess.Popen(rmCmd,shell = True)
        process.wait()
        print '*************restart option*************'  
    
    #pod第三方库
    podCmd = 'pod update'
    #首次导入报错
    #podCmd = 'pod install'
    process = subprocess.Popen(podCmd,shell = True)
    process.wait()

def main():
    #还原本地库
    print 'REST HEAD...'
    resetCmd = 'git reset --hard origin/master'
    process = subprocess.Popen(resetCmd,shell = True)
    process.wait()
    #自助拉取分支
    branlist = ccccs()
    index = raw_input("Please input you want branch index（int）:")
    xxxxd(branlist,index)

def run():
    if FilePath:
        main()
    else:
        #创建版本库
        intgitCmd = 'git init'
        process = subprocess.Popen(intgitCmd,shell = True)
        process.wait()
        #关联远程库
        remoteCmd = 'git remote add origin git@git.workec.com:ios/lite-obc.git'
        process = subprocess.Popen(remoteCmd,shell = True)
        process.wait()
        #抓取远程仓库所有分支更新并合并到本地...
        pullCmd = 'git pull'
        process = subprocess.Popen(pullCmd,shell = True)
        process.wait()
        print 'GitLab Success Created!'
        main()

if __name__ == '__main__':
    run()
    #查看更新日志 ，Enter查看下一条
    lpgCmd = 'git log --oneline'
    process = subprocess.Popen(lpgCmd,shell = True)
    process.wait()



