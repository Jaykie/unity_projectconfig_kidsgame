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
import source

# 获取脚本文件的当前路径


def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    return path


# http://help.apple.com/itc/appsspec/#/itc6e4198248
# 主函数的实现
if __name__ == "__main__":

    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    for i in range(1, count):
        print "参数", i, sys.argv[i]
        if i == 1:
            cmdPath = sys.argv[i]
   
    print "cmdPath="+cmdPath+" count="+str(count)
    common.SetCmdPath(cmdPath)
    gameName = common.getGameName()
    gameType = common.getGameType()
    print "gameName="+gameName
    print "gameType="+gameType

    isUploadIPA = False
    isExportIPA = False
    if count > 1:
        argv1 = sys.argv[2]
        if argv1 == "upload_ipa":
            isUploadIPA = True

        if argv1 == "export_ipa":
            isExportIPA = True

    if isExportIPA:
        if count > 2:
            channel = sys.argv[2]

    #  -u chyfemail163@163.com -p ayww-hcnh-uaau-lsgh
    # xcodebuild -list
    RootDir = common.GetRootProjectIos()
    target = "Unity-iPhone"
    xcode_project = common.GetRootDirXcode()+ "/Unity-iPhone.xcodeproj"
    archive_file = RootDir + "/app.xcarchive"
    # 不带后缀.ipa
    ipa_file = RootDir + "/app/" + target
    if isExportIPA:
        if count > 2:
            ipa_file = RootDir + "/app_" + channel + "/" + target


    exportOptionPlist_file = RootDir + "/ExportOptions.plist"

    # 清空频道文件
    channel_dir = common.GetRootDirXcode() + "/Data/Raw/channel"
    flag = os.path.exists(channel_dir)
    if flag:
        shutil.rmtree(channel_dir)

    # 生成频道文件
    if isExportIPA:
        if count > 2:
            os.makedirs(channel_dir)
            fp = open(channel_dir + "/" + channel, "w")
            if fp:
                fp.close()

    if isUploadIPA == True:
        # 上传ipa
        strCmd = "/Applications/Xcode.app/Contents/Applications/Application\ Loader.app/Contents/Frameworks/ITunesSoftwareService.framework/Versions/A/Support/altool --upload-app -f " + \
            ipa_file + "/" + target + ".ipa" + \
            " -t ios -u "+source.APPSTORE_USER+" -p "+source.APPSTORE_PASSWORD 
            # + "--output-format xml"
        os.system(strCmd)
    else:
        # build target.app
        # strCmd = "xcodebuild -project " + xcode_project + " -target " + "Unity-iPhone"
        # os.system(strCmd)

        # archive
        if isExportIPA == False:
            flag = os.path.exists(archive_file)
            if flag:
                shutil.rmtree(archive_file)

            flag = os.path.exists(ipa_file)
            if flag:
                shutil.rmtree(ipa_file)

            strCmd = "xcodebuild -allowProvisioningUpdates -project " + xcode_project + " -scheme " + \
                target + " -configuration Release clean archive" + " -archivePath " + archive_file
            os.system(strCmd)

        # 导出ipa
        strCmd = "xcodebuild -allowProvisioningUpdates -exportArchive " + " -archivePath " + \
            archive_file + " -exportPath " + ipa_file + \
            " -exportOptionsPlist " + exportOptionPlist_file
        os.system(strCmd)

        #copy ipa 到共享目录
        if common.IsVMWare():
            ipa_file_src = common.GetRootProjectIos() + "/app/" + target+"/" + target + ".ipa"

            #GetRootProjectIosVMVare
            dir_ipa = common.GetProjectOutPutIPA()
            if not os.path.exists(dir_ipa):
                os.makedirs(dir_ipa) 

            ipa_file_dst =dir_ipa + "/" + common.GetOutPutIPAName()
            print "ipa_file_src= "+ipa_file_src
            print "ipa_file_dst= "+ipa_file_dst

            if os.path.isfile(ipa_file_src):
                shutil.copyfile(ipa_file_src,ipa_file_dst)


    print "ipa_build sucess"
