#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime

#include common.py
sys.path.append('./common')
import common
 
def copy_plugins():
    dirname = "Plugins"
    dir1 = common.GetRootDir()+"/"+dirname
    dir2 = common.GetRootUnityAssets()+"/"+dirname
    flag = os.path.exists(dir2)
    if not flag:
        # shutil.rmtree(dir2)
        shutil.copytree(dir1,dir2)

#主函数的实现
if  __name__ =="__main__":
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print "参数", i, sys.argv[i]
        if i==1:
            cmdPath = sys.argv[i]
    
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
   
    print gameName
    print gameType 

    # resoucedata
    dirname = "Resources"
    dir1 = common.GetResourceDataRoot()+"/"+gameType+"/"+gameName+"/"+dirname
    dir2 = common.GetRootProjectUnity()+"/Assets/Resources"
    common.copyResourceFiles(dir1,dir2)

    copy_plugins()

    print "copy_resource sucess"