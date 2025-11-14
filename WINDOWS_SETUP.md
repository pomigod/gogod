# 💻 Windows에서 바로 실행하기

**건양대 6팀 AI 학습 도우미 - Windows CMD 완전 가이드**

---

## ⚡ 가장 빠른 방법 (3단계)

### 1단계: CMD 열기

**방법 A:**
- `Win + R` 누르기
- `cmd` 입력
- Enter!

**방법 B:**
- 시작 메뉴 클릭
- "cmd" 또는 "명령 프롬프트" 검색
- 실행!

### 2단계: 다운로드 폴더로 이동

```cmd
cd %USERPROFILE%\Downloads
```

### 3단계: 한 번에 설치 및 실행

**다음 명령어를 복사해서 CMD에 붙여넣으세요:**

```cmd
curl -o setup.bat https://raw.githubusercontent.com/pomigod/gogod/claude/daily-harmony-final-submission-01PGznatAZW6ssXquA76bouv/setup.bat && setup.bat
```

**Enter 누르면 자동으로 설치됩니다!**

---

## 📋 수동 설치 (curl이 안되는 경우)

### 1단계: Git 설치 확인

```cmd
git --version
```

**오류가 나면?**
1. https://git-scm.com/download/win 접속
2. Git 다운로드 및 설치
3. 컴퓨터 재시작

### 2단계: Python 설치 확인

```cmd
python --version
```

**오류가 나면?**
1. https://www.python.org/downloads/ 접속
2. Python 다운로드 및 설치
3. ⚠️ **중요**: "Add Python to PATH" 체크!
4. 컴퓨터 재시작

### 3단계: 프로젝트 다운로드

```cmd
cd %USERPROFILE%\Downloads
git clone https://github.com/pomigod/gogod.git ai-learning-assistant
cd ai-learning-assistant
git checkout claude/daily-harmony-final-submission-01PGznatAZW6ssXquA76bouv
```

### 4단계: Python 패키지 설치

```cmd
pip install -r requirements.txt
```

### 5단계: 애플리케이션 실행

```cmd
set LOCAL_TEST_MODE=true
python app.py
```

### 6단계: 웹 브라우저에서 확인

주소창에 입력:
```
http://localhost:5000
```

---

## ⚠️ 중요: 로컬 vs AWS

### 로컬 실행 (지금 하는 것)
```
✅ 웹 페이지 확인 가능
✅ UI/UX 테스트 가능
❌ AI 기능 작동 안함 (Bedrock 없음)
```

### AWS EC2 배포 (실제 서비스)
```
✅ 웹 페이지 정상 작동
✅ AI 기능 완전 작동
✅ 인터넷에서 접속 가능
```

**AI 기능을 사용하려면 반드시 AWS EC2에 배포해야 합니다!**

---

## 🐛 문제 해결

### Q: 'git'은(는) 내부 또는 외부 명령이 아닙니다

**A: Git 설치 필요**

1. https://git-scm.com/download/win 접속
2. "Click here to download" 클릭
3. 다운로드된 파일 실행
4. 기본 설정으로 설치 (Next 계속 클릭)
5. **CMD 재시작** (중요!)

### Q: 'python'은(는) 내부 또는 외부 명령이 아닙니다

**A: Python 설치 필요**

1. https://www.python.org/downloads/ 접속
2. "Download Python" 버튼 클릭
3. 다운로드된 파일 실행
4. ⚠️ **"Add Python to PATH" 체크박스 반드시 체크!**
5. "Install Now" 클릭
6. **CMD 재시작** (중요!)

### Q: curl: command not found

**A: Windows 10 이상이면 curl 내장**

Windows 10 미만이면:

**방법 1: 직접 다운로드**
1. https://github.com/pomigod/gogod/archive/refs/heads/claude/daily-harmony-final-submission-01PGznatAZW6ssXquA76bouv.zip
2. ZIP 다운로드
3. 압축 해제
4. CMD에서 해당 폴더로 이동

**방법 2: 수동 설치 섹션 따라하기**

### Q: 포트 5000이 이미 사용 중입니다

**A: 다른 포트 사용**

```cmd
set PORT=8080
python app.py
```

그리고 브라우저에서:
```
http://localhost:8080
```

### Q: ERROR: Could not open requirements file

**A: 프로젝트 폴더에 있는지 확인**

```cmd
dir requirements.txt
```

파일이 없으면:
```cmd
cd %USERPROFILE%\Downloads\ai-learning-assistant
dir requirements.txt
```

---

## 🎯 AWS EC2 배포하기

로컬 테스트가 끝났으면 이제 **실제 AWS에 배포**해야 합니다!

### 배포 가이드 보기

**GitHub에서 가이드 열기:**
```
https://github.com/pomigod/gogod/blob/claude/daily-harmony-final-submission-01PGznatAZW6ssXquA76bouv/STEP_BY_STEP_GUIDE.md
```

또는 다운로드한 폴더에서:
```cmd
notepad STEP_BY_STEP_GUIDE.md
```

---

## 📝 명령어 요약

### 전체 과정 한 번에 (복사-붙여넣기)

```cmd
REM 다운로드 폴더로 이동
cd %USERPROFILE%\Downloads

REM 프로젝트 클론
git clone https://github.com/pomigod/gogod.git ai-learning-assistant

REM 프로젝트 폴더로 이동
cd ai-learning-assistant

REM 브랜치 변경
git checkout claude/daily-harmony-final-submission-01PGznatAZW6ssXquA76bouv

REM Python 패키지 설치
pip install -r requirements.txt

REM 로컬 테스트 모드로 실행
set LOCAL_TEST_MODE=true
python app.py
```

**위 명령어를 순서대로 하나씩 실행하세요!**

---

## 🖥️ 실행 결과 확인

정상적으로 실행되면:

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
```

이 메시지가 보이면 **성공!**

웹 브라우저에서:
```
http://localhost:5000
```

---

## 🎓 다음 단계

1. ✅ 로컬에서 웹 페이지 확인 완료
2. ⏭️ AWS EC2에 배포하기 (STEP_BY_STEP_GUIDE.md 참조)
3. 🎉 AI 기능 완전히 사용하기!

---

## 💡 팁

### CMD에 붙여넣기 방법

1. 명령어 복사 (Ctrl+C)
2. CMD 창 클릭
3. **우클릭** → 자동으로 붙여넣기됨!

또는:

1. CMD 창에서 **Ctrl+V** (Windows 10 이상)

### 여러 줄 한 번에 실행

명령어를 `&&`로 연결:

```cmd
cd Downloads && git clone https://github.com/pomigod/gogod.git && cd gogod
```

### CMD 빠른 종료

```
Ctrl+C
```

또는 창 닫기!

---

## 🆘 여전히 안되면?

### 1. 스크린샷 찍어서 팀원에게 공유
- `Win + Shift + S`: 화면 캡처
- 오류 메시지 전체 복사

### 2. 가이드 다시 확인
```
https://github.com/pomigod/gogod/blob/claude/daily-harmony-final-submission-01PGznatAZW6ssXquA76bouv/STEP_BY_STEP_GUIDE.md
```

### 3. 강사님께 질문
- 999 채널
- @NxtCloud_김유림

---

## ✅ 체크리스트

시작하기 전:
- [ ] Git 설치 확인
- [ ] Python 설치 확인
- [ ] 인터넷 연결 확인
- [ ] CMD 열기

실행 후:
- [ ] 프로젝트 다운로드 완료
- [ ] Python 패키지 설치 완료
- [ ] 웹 브라우저에서 localhost:5000 접속 확인

---

**건양대학교 AI 부트캠프 6팀**

Windows 환경에서도 문제없이 실행됩니다! 💪
