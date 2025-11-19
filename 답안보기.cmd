@echo off
chcp 65001 >nul
echo ========================================
echo AI_TOP_100 문제 1 답안 확인
echo ========================================
echo.
echo 답안 파일을 메모장으로 엽니다...
echo.

REM 파일이 존재하는지 확인
if exist "CLAUDE_CODE_ANSWERS.md" (
    notepad CLAUDE_CODE_ANSWERS.md
) else (
    echo [오류] CLAUDE_CODE_ANSWERS.md 파일을 찾을 수 없습니다.
    echo.
    echo 현재 디렉토리: %CD%
    echo.
    pause
)
