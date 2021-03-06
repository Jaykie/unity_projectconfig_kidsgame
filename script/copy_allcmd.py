#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys


sys.path.append('./common')
import common


def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

def ScanDir(sourceDir,channel,dir2):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file) 
        if os.path.isdir(sourceFile): 
            dirsrc = common.GetProjectConfigDefault()+"/cmd_win"
            if common.isWindowsSystem():
                dir = sourceFile+"/cmd_win" 
                flag = os.path.exists(dir)
                if flag:
                    shutil.rmtree(dir)
                shutil.copytree(dirsrc,dir)

            else:
                dir = sourceFile+"/cmd_mac"
                
              
              
# 主函数的实现
if __name__ == "__main__":

     # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    print ("脚本名：", sys.argv[0])
    cmdPath = cur_file_dir()
    count = len(sys.argv)
    channel = ""

    for i in range(1, count):
        print ("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

        if i == 2:
            channel = sys.argv[i] 

    dir2 = cmdPath
    if common.IsVMWare():
        cmdPath="/Volumes/VMware Shared Folders/"+cmdPath

    print ("dir2="+dir2)


    ScanDir(cmdPath,channel,dir2)

    print  ("build_huawei sucess")
