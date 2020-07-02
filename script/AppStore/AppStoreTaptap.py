# 导入selenium的浏览器驱动接口


import sys
import os
import json
o_path = os.getcwd()  # 返回当前工作目录
sys.path.append(o_path)  # 添加自己指定的搜索路径
 
import appname
import win32con
import win32gui
import sqlite3
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from common import source
from common import common
from AppStoreBase import AppStoreBase

# 要想调用键盘按键操作需要引入keys包

# 导入chrome选项


# pip3 install pywin32

# sys.path.append('../common')


class AppStoreTaptap(AppStoreBase):  


    def GoHome(self,isHD): 
        # self.driver.get("https://www.taptap.com/developer") 
        # self.driver.get("https://www.taptap.com/developer/dashboard/14628/apps") 
        # app
        # https://www.taptap.com/developer/dashboard/14628?app_id=56016
        appid = appname.GetAppId(isHD, source.TAPTAP)
        url = "https://www.taptap.com/developer/dashboard/14628?app_id="+appid
        print(url)
        self.driver.get(url)
        time.sleep(1)

        # <div class="icon-font ic_qq"></div>
        # 跳转qq登录
        item = self.driver.find_element( By.XPATH, "//div[@class='icon-font ic_qq']")
        item.click()
        time.sleep(1)


    
# 3452644866 qq31415926
    def CreateApp(self, isHD):
        # ad.GoHome(isHD)
        time.sleep(1)

        # Android平台
        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='mediumTypeSelector']")
        item.click()

        time.sleep(1)

        list = self.driver.find_elements(
            By.XPATH, "//a[@role='option']")

        if self.osApp == source.ANDROID:
            list[0].click()

        if self.osApp == source.IOS:
            list[1].click()

        # 应用商店

        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='appStoreSelector']")
        item.click()

        time.sleep(1)

        ul_list = self.driver.find_elements(
            By.XPATH, "//ul[@class='dropdown-menu inner']")

        list = ul_list[1].find_elements(
            By.XPATH, "//a[@role='option']")
        
        if self.osApp == source.ANDROID:
            list[7].click()

        if self.osApp == source.IOS:
            list[0].click()


    # 应用分类
        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='industryOneSelector']")
        item.click()
        time.sleep(1)
        ul_list = self.driver.find_elements(
            By.XPATH, "//ul[@class='dropdown-menu inner']")
        list = ul_list[2].find_elements(
            By.XPATH, "//a[@role='option']")
        list[12].click()

        item = self.driver.find_element(
            By.XPATH, "//button[@data-id='industrySecondSelector']")
        item.click()
        time.sleep(1)
        ul_list = self.driver.find_elements(
            By.XPATH, "//ul[@class='dropdown-menu inner']")
        list = ul_list[3].find_elements(
            By.XPATH, "//a[@role='option']")
        list[3].click()

        # url
        item = self.driver.find_element(
            By.XPATH, "//input[@class='form-control size-410 form-control']")
        
        
        url = ""
        if self.osApp == source.ANDROID:
            appid = appname.GetAppId(isHD, source.HUAWEI)
            url = "http://appstore.huawei.com/C"+appid

        if self.osApp == source.IOS:
            appid = appname.GetAppId(isHD, source.APPSTORE)
            # https://itunes.apple.com/cn/app/id1303020002
            url = "https://itunes.apple.com/cn/app/id"+appid
        
        item.send_keys(url)

        # name
        name = self.GetAppName(isHD)
        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[0].send_keys(name)

        list = self.driver.find_elements(
            By.XPATH, "//input[@id='placementName']")
        list[1].send_keys(name)

        item = self.driver.find_element_by_id('formControlsTextarea')
        name += name
        name += name
        name += name
        name += name
        item.send_keys(name)

        item = self.driver.find_element(
            By.XPATH, "//input[@id='packageName']")
        package = appname.GetPackage(source.ANDROID, isHD)
        item.send_keys(package)

        # 创建

        item = self.driver.find_element(
            By.XPATH, "//a[@class='btn btn-primary btn-160']")
        item.click()

    def UpdateApp(self, isHD): 
        appid = appname.GetAppId(isHD, source.TAPTAP)
        # https://www.taptap.com/developer/app-update/56016/14628
        time.sleep(4)
        item = self.driver.find_element(By.XPATH, "//a[@data-taptap-btn='updateAppData']")
        item.click()
        time.sleep(4)
 
        # url = "https://www.taptap.com/developer/app-update/"+appid+"/14628"
        # self.driver.get(url) 
        # time.sleep(2)

        # <a data-toggle="modal" data-target=".confirm-upload-apk" class="btn btn-primary">上传APK</a>
        # item = self.driver.find_element(By.XPATH, "//a[@data-target='.confirm-upload-apk']")
        # item = self.driver.find_element(By.XPATH, "//a[@data-toggle='modal']")
        # item.click()
        # time.sleep(2)
     

        # <a id="selectfiles" href="javascript:void(0);" class="btn btn-primary" style="position: relative; z-index: 1;">开始上传APK</a>
        # item = self.driver.find_element(By.XPATH, "//a[@id='selectfiles']")
        # item.click()
        # time.sleep(1)

        self.urlold = self.driver.current_url
        print("urlold=",self.urlold)
        # 手动点击上传
        
        time.sleep(10)

        rootdir = "F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut"
        apk = common.GetOutPutApkPathWin32(rootdir,source.TAPTAP,isHD)
        # F:\\sourcecode\\unity\\product\\kidsgame\\ProjectOutPut\\xiehanzi\\hanziyuan\\screenshot\\shu\\cn\\480p\\1.jpg
        self.OpenFileBrowser(apk,True)

        search_window = self.driver.current_window_handle
        while True:
            time.sleep(2)
            # self.driver.switch_to.window(self.driver.window_handles[0])  
            self.urlnew = self.driver.current_url
            print("urlnew=",self.urlnew)
            if self.urlnew!=self.urlold:
                break

        # <div class="progress"><div class="progress-bar" style="width: 82%;" aria-valuenow="82"></div></div>
        # while True:
        #     item = self.driver.find_element(By.XPATH, "//div[@class='progress']")
        #     if item is not None:
        #         value = item.get_attribute('aria-valuenow')
        #         int_v = int(value)
        #         if int_v>=100:
        #             break
        
        # time.sleep(1)

        # 手动等待上传
        time.sleep(60*2)


        # https://www.taptap.com/developer/fill-form/14628?apk_id=496448&app_id=56016


        # 未成年人防沉迷
        # <input required="" type="radio" name="anti_addiction_read" value="1">
        item = self.driver.find_element(By.XPATH, "//input[@name='anti_addiction_read']")
        item.click()
        time.sleep(1)
        # <input required="required" type="radio" name="anti_addiction_status" value="1">
        item = self.driver.find_element(By.XPATH, "//input[@name='anti_addiction_status']")
        item.click()
        time.sleep(1)

        # 提交审核
        # <button id="postAppSubmitV2" type="submit" value="submit" class="leave_current_page btn btn-primary btn-lg">保存并提交审核</button>
        item = self.driver.find_element(By.XPATH, "//button[@id='postAppSubmitV2']")
        item.click()
        time.sleep(1)


    def GetAppName(self, ishd):
        name = appname.GetAppName(self.osApp, ishd)
        # if self.osApp == source.IOS:
        #     appname.GetAppName(self.osApp, ishd)+self.osApp

        return name
 
    def SearchApp(self, ishd):
        name = self.GetAppName(ishd)
        self.driver.get("https://adnet.qq.com/medium/list")
        time.sleep(2)
        item = self.driver.find_element(
            By.XPATH, "//input[@class='form-control']")
        time.sleep(1)

        item.send_keys(name)
        # item.send_keys("儿童写汉字")

        time.sleep(1)

        # search
        self.driver.find_element_by_id('search_medium_id').click()
        time.sleep(2)
 
        # 筛选
        item = self.driver.find_element(By.XPATH, "//button[@class='btn filter-operate']")
        # item = self.driver.find_element(By.XPATH, "//div[@class='filter-parent-control']")

        # error
        # item.click()  
        self.driver.execute_script("arguments[0].click();", item)
        time.sleep(2)

# <input type="checkbox" class="check" name="" value="IOS"> 
        if self.osApp == source.ANDROID:
            item = self.driver.find_element(By.XPATH, "//input[@value='Android']")
            # item.click()
            self.driver.execute_script("arguments[0].click();", item)
            time.sleep(1)

        if self.osApp == source.IOS:
            item = self.driver.find_element(By.XPATH, "//input[@value='IOS']")
            # item.click()
            self.driver.execute_script("arguments[0].click();", item)
            time.sleep(1)
         
        # 确定
        item = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        # item.click()
        self.driver.execute_script("arguments[0].click();", item)
        time.sleep(2)


        # 点击第一个
        item = self.driver.find_element(By.XPATH, "//div[@class='media']")
        item.click()
        time.sleep(1)
 



    


# 主函数的实现
if __name__ == "__main__":
    # 设置为utf8编码
    # reload(sys)
    # sys.setdefaultencoding("utf-8")

    # 入口参数：http://blog.csdn.net/intel80586/article/details/8545572
    cmdPath = common.cur_file_dir()
    count = len(sys.argv)
    isHD = False
    for i in range(1, count):
        print("参数", i, sys.argv[i])
        if i == 1:
            cmdPath = sys.argv[i]

        if i == 3:
            if sys.argv[i] == "hd":
                isHD = True

    # cmdPath = cmdPath.replace("ad\\", "")

    dir = common.getLastDirofDir(cmdPath)
    # dir = common.getLastDirofDir(dir)
    common.SetCmdPath(dir)
  

    ad = AppStoreTaptap()
    ad.SetCmdPath(cmdPath)
    ad.Init()
    ad.GoHome(False)
    ad.LoginQQ("651577315","qq31415926")

    argv1 = sys.argv[2]
    # ad.osApp = sys.argv[3]
    if argv1 == "createapp":
        ad.CreateApp(False)
        time.sleep(3)
        ad.CreateApp(True)
 
    if argv1 == "update":
        ad.UpdateApp(isHD)
        time.sleep(3)
        # ad.UpdateApp(True)

    print("AppStoreTaptap sucess")
