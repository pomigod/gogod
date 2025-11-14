@echo off
REM Windows용 답안 보기 스크립트
REM 사용법: view_answer.bat

echo ================================================================================
echo AI_TOP_100 문제 4: 전투 시뮬레이션의 힘 - 정답 요약
echo ================================================================================
echo.

REM 답안 파일을 메모장으로 열기
start notepad.exe problem4_answers.txt

REM 콘솔에도 출력
type problem4_answers.txt

echo.
echo ==========================================
echo 메모장에서 답안을 확인하세요!
echo 상세 분석: CLAUDE_CODE_ANSWERS.md
echo 예측 결과: battle_predictions.json
echo ==========================================
pause
