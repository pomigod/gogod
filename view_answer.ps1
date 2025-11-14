# PowerShell용 답안 보기 스크립트
# 사용법: .\view_answer.ps1

$answerFile = "problem4_answers.txt"

Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "AI_TOP_100 문제 4: 전투 시뮬레이션의 힘 - 정답 요약" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host ""

# 파일이 존재하는지 확인
if (Test-Path $answerFile) {
    # 메모장으로 열기 (즉시 실행)
    Start-Process notepad.exe $answerFile

    # 콘솔에도 출력
    Get-Content $answerFile

    Write-Host ""
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host "메모장에서 답안을 확인하세요!" -ForegroundColor Green
    Write-Host "상세 분석: CLAUDE_CODE_ANSWERS.md" -ForegroundColor Yellow
    Write-Host "예측 결과: battle_predictions.json" -ForegroundColor Yellow
    Write-Host "==========================================" -ForegroundColor Green
} else {
    Write-Host "Error: 답안 파일을 찾을 수 없습니다." -ForegroundColor Red
    Write-Host "현재 경로: $(Get-Location)" -ForegroundColor Red
}

Write-Host ""
Write-Host "아무 키나 눌러 종료..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
