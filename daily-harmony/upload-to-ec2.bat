@echo off
echo ====================================
echo   Daily Harmony Upload to EC2
echo ====================================
echo.
echo Uploading files to EC2: 18.217.233.121
echo.

REM 현재 스크립트가 있는 디렉토리 경로 가져오기
set SCRIPT_DIR=%~dp0

echo Source: %SCRIPT_DIR%
echo Target: ec2-user@18.217.233.121:/home/ec2-user/
echo.

scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r "%SCRIPT_DIR%." ec2-user@18.217.233.121:/home/ec2-user/daily-harmony

echo.
echo ====================================
echo   Upload Completed!
echo ====================================
echo.
pause
