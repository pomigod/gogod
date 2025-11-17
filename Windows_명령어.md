# AI_TOP_100 문제 3번 답안 보기 - Windows 원라이너 명령어

## PowerShell 명령어 (권장)
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/pomigod/gogod/claude/ai-top-100-problem-3-01JhR13BMW9FNVnqj4sPPShJ/CLAUDE_CODE_ANSWERS.md" -OutFile "$env:TEMP\CLAUDE_CODE_ANSWERS.md"; notepad "$env:TEMP\CLAUDE_CODE_ANSWERS.md"
```

## CMD 명령어
```cmd
powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/pomigod/gogod/claude/ai-top-100-problem-3-01JhR13BMW9FNVnqj4sPPShJ/CLAUDE_CODE_ANSWERS.md' -OutFile '%TEMP%\CLAUDE_CODE_ANSWERS.md'; notepad '%TEMP%\CLAUDE_CODE_ANSWERS.md'"
```

## curl 사용 (Windows 10 이상)
```cmd
curl -o "%TEMP%\CLAUDE_CODE_ANSWERS.md" "https://raw.githubusercontent.com/pomigod/gogod/claude/ai-top-100-problem-3-01JhR13BMW9FNVnqj4sPPShJ/CLAUDE_CODE_ANSWERS.md" && notepad "%TEMP%\CLAUDE_CODE_ANSWERS.md"
```

---

## 사용 방법
1. 위 명령어 중 하나를 복사
2. PowerShell 또는 CMD를 열기
3. 붙여넣기 후 엔터
4. 자동으로 다운로드되고 메모장이 열립니다

파일은 임시 폴더(%TEMP%)에 저장되며, 메모장에서 바로 확인할 수 있습니다.
