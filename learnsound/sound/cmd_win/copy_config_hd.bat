 
@set filepath = %~dp0 

cd ../../../script

c:/Python27/python copy_config.py %~dp0 iconhd
c:/Python27/python clean_screenshot.py %~dp0

@Pause

 

 
 