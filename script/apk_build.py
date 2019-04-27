#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys

# include appinfo.py
# sys.path.append('./common')
import appname


sys.path.append('./common')
import common

def buildApk():
    if common.isWindowsSystem():
        # dir1 = "C:\Program Files\Android\Android Studio\gradle"
    	dir2 = "C:/moon/gradle"
        flag = os.path.exists(dir2)
    	if not flag:
    		shutil.copytree(dir1,dir2)
        
        os.system(dir2+"/gradle-4.10.1/bin/gradle assembleRelease")
    else:
        os.system("gradle assembleRelease")
   


def copyApk(channel):
    gameName = common.getGameName()
    gameType = common.getGameType()
 # copy2 同时复制文件权限
    dirapk = common.GetProjectIconApp() + "/apk"
 

    if common.AppForPad():
        dirapk+="/heng"
        gameName += "_hd"
    else:
        dirapk+="/shu"

    if not os.path.exists(dirapk):
        os.makedirs(dirapk)

    shutil.copy2(common.getAndroidProjectApk(), dirapk + "/" +
                 gameType + "_" + gameName + "_" + channel + ".apk")

    
# 主函数的实现
if __name__ == "__main__":

     # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    print "脚本名：", sys.argv[0]
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    isHD = False

    for i in range(1, count):
        print "参数", i, sys.argv[i]
        if i == 1:
            cmdPath = sys.argv[i]

        if i == 2:
            if sys.argv[i] == "hd":
                isHD = True

    print "cmdPath="+cmdPath
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    print "gameName="+gameName
    print "gameType="+gameType
    android_studio_dir = common.GetRootDirAndroidStudio()
    print "android_studio_dir="+android_studio_dir
    # python 里无法直接执行cd目录，想要用chdir改变当前的工作目录
    os.chdir(android_studio_dir)
    buildApk()
    copyApk("")

    print "apk_build sucess"
