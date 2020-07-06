#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime

o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径  

from common import config 
from common import common  

#主函数的实现
if  __name__ =="__main__":
    
    #入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    print ("脚本名：", sys.argv[0])
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1,count):
        print ("参数", i, sys.argv[i])
        if i==1:
            cmdPath = sys.argv[i]
    
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    
    print (gameType) 
    print (gameName) 

    configDirUnity = common.GetRootProjectUnity()+"/Assets/Resources/ConfigData/config"

    configAppType = config.GetConfigAppType(configDirUnity)
    configAppName = config.GetConfigAppName(configDirUnity)
    print ("unity:"+configAppType+" "+configAppName)

    if gameType!=configAppType or gameName!=configAppName:
        print ("check app type and name fail")
        sys.exit(0)


    dir1 = common.GetRootProjectUnity()+"/Assets/Resources/App"
    dir2 = common.GetResourceDataRoot()+"/"+gameType+"/"+gameName+"/"+"Resources/App"
    flag = os.path.exists(dir2)
    if flag:
        shutil.rmtree(dir2)
    shutil.copytree(dir1,dir2)

    # AppCommon
    dir1 = common.GetRootProjectUnity()+"/Assets/Resources/AppCommon" 
    dir2 = common.GetResourceDataRoot()+"/"+gameType+"/"+"AppCommon/Resources"
    flag = os.path.exists(dir2)
    common.CopyDir(dir1,dir2)

   # ConfigData
    dir1 = common.GetRootProjectUnity()+"/Assets/Resources/ConfigData" 
    dir2 = common.GetResourceDataRoot()+"/"+gameType+"/"+gameName+"/ConfigData"
    flag = os.path.exists(dir2)
    common.CopyDir(dir1,dir2)


    print ("save_resource sucess")