@echo  build_all_android
@set filepath = %~dp0 

:: �Զ�����"�����������"https://zhidao.baidu.com/question/403369786.html

@echo off
echo.| call copy_resource.bat
echo.| call unity_build_android.bat
echo. | call update_appname_auto.bat
echo.| call apk_build_all.bat
@Pause


