#! /user/bin/python3

import os
import threading

def isContainGit(path):
    if not os.path.isdir(path):
        return
    subDir=os.listdir(path)
    for line in subDir:
        if line == ".git" and os.path.isdir(path+"/"+line):
            return True

def update(dir):
    print("start pull "+dir)
    os.system("git -C "+dir+" pull")


cwd=os.getcwd()
listfile=os.listdir(cwd)
print(listfile)
for line in listfile:  #把目录下的文件都赋值给line这个参数
    filename=cwd+"/"+line
    if isContainGit(filename):
        update(line)
        # t = threading.Thread(target=update,args=(line,))
        # t.start()
    



       