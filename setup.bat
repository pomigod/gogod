@echo off
REM ========================================
REM AI 학습 도우미 - Windows 자동 설치
REM 건양대 6팀
REM ========================================

echo.
echo ========================================
echo AI 학습 도우미 설치 시작
echo ========================================
echo.

REM Git 설치 확인
echo [1/5] Git 확인 중...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git이 설치되어 있지 않습니다!
    echo.
    echo Git 설치 방법:
    echo 1. https://git-scm.com/download/win 접속
    echo 2. Git 다운로드 및 설치
    echo 3. 이 스크립트 다시 실행
    echo.
    pause
    exit /b 1
)
echo Git 설치 확인 완료!

REM Python 설치 확인
echo.
echo [2/5] Python 확인 중...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python이 설치되어 있지 않습니다!
    echo.
    echo Python 설치 방법:
    echo 1. https://www.python.org/downloads/ 접속
    echo 2. Python 다운로드 및 설치
    echo 3. 설치 시 "Add Python to PATH" 체크!
    echo 4. 이 스크립트 다시 실행
    echo.
    pause
    exit /b 1
)
echo Python 설치 확인 완료!

REM 프로젝트 클론
echo.
echo [3/5] 프로젝트 다운로드 중...
if exist ai-learning-assistant (
    echo 기존 폴더 발견. 삭제 후 다시 다운로드...
    rmdir /s /q ai-learning-assistant
)
git clone https://github.com/pomigod/gogod.git ai-learning-assistant
if %errorlevel% neq 0 (
    echo ERROR: 프로젝트 다운로드 실패!
    pause
    exit /b 1
)
cd ai-learning-assistant
git checkout claude/daily-harmony-final-submission-01PGznatAZW6ssXquA76bouv
echo 프로젝트 다운로드 완료!

REM Python 패키지 설치
echo.
echo [4/5] Python 패키지 설치 중...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: 패키지 설치 실패!
    pause
    exit /b 1
)
echo 패키지 설치 완료!

REM 로컬 테스트 모드로 실행
echo.
echo [5/5] 애플리케이션 시작 중...
echo.
echo ========================================
echo 설치 완료!
echo ========================================
echo.
echo 주의: 로컬에서는 AI 기능이 작동하지 않습니다!
echo AI 기능을 사용하려면 AWS EC2에 배포해야 합니다.
echo.
echo 웹 브라우저에서 다음 주소로 접속하세요:
echo http://localhost:5000
echo.
echo 종료하려면 Ctrl+C를 누르세요.
echo.
echo ========================================

REM 로컬 테스트 모드 활성화
set LOCAL_TEST_MODE=true
python app.py

pause
