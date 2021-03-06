@echo off
set regpath=HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
set javahome=C:\Program Files\Unity\Hub\Editor\2019.3.2f1\Editor\Data\PlaybackEngines\AndroidPlayer\OpenJDK\jre
:aliyun  C:\Program Files\Unity\Hub\Editor\2019.3.2f1\Editor\Data\PlaybackEngines\AndroidPlayer\OpenJDK\jre 
:win10  C:\Program Files\Android\Android Studio\jre\jre
rem LPY
echo.
echo ************************************************************
echo *                                                          *
echo *                   JDK 系统环境变量设置                   *
echo *                                                          *
echo ************************************************************
echo.
echo === 准备设置环境变量: JAVA_HOME=%javahome%
echo === 注意: 如果JAVA_HOME存在,会被覆盖,此操作不可逆的,请仔细检查确认!! ===
echo.
echo === 准备设置环境变量(后面有个.): classPath=%%JAVA_HOME%%\lib\tools.jar;%%JAVA_HOME%%\lib\dt.jar;.
echo === 注意: 如果classPath存在,会被覆盖,此操作不可逆的,请仔细检查确认!! ===
echo.
echo === 准备设置环境变量: PATH=%%JAVA_HOME%%\bin
echo === 注意: PATH会追加在最前面,
echo.
:set /P EN=请确认后按 回车键 开始设置!
echo.
echo.
echo.
echo.
echo === 新创建环境变量 JAVA_HOME=%javahome%
setx "JAVA_HOME" "%javahome%" -M
echo.
echo.
echo === 新创建环境变量 classPath=%%JAVA_HOME%%\lib\tools.jar;%%JAVA_HOME%%%\lib\dt.jar;.
setx "classPath" "%%JAVA_HOME%%\lib\tools.jar;%%JAVA_HOME%%%\lib\dt.jar;." -m
echo.
echo.
echo === 新追加环境变量(追加到最前面) PATH=%%JAVA_HOME%%\bin
for /f "tokens=1,* delims=:" %%a in ('reg QUERY "%regpath%" /v "path"') do (
    set "L=%%a"
    set "P=%%b"
)
set "Y=%L:~-1%:%P%"
 
setx path "%%JAVA_HOME%%\bin;%Y%" -m
echo.
echo.
rem LPY Zeus http://write.blog.csdn.net/postedit/9822439
echo === 请按任意键退出! 
pause>nul
