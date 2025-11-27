# Daily Harmony 프로젝트 인계 프롬프트

다음 내용을 다른 AI 챗봇에게 제공하세요:

---

## 프로젝트 현황

**프로젝트명**: Daily Harmony - AI 수강신청 도우미

**현재 상태**:
- ✅ 기본 프로젝트 구조 완성
- ✅ Flask 앱 구현 완료
- ✅ AI 챗봇 기능 구현 (대화 기억 기능 포함)
- ✅ HTML/CSS UI 완성
- ✅ Git 커밋 및 푸시 완료
- ⏳ EC2 배포 대기 중

---

## 프로젝트 정보

### 파일 위치
- **로컬 경로**: `/home/user/gogod/daily-harmony/`
- **Git 브랜치**: `claude/deploy-ai-learning-assistant-014q5hiGuMRXTWZn5dbsggSW`

### EC2 정보
- **IP**: 18.217.233.121
- **사용자**: ec2-user
- **키 파일**: C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem
- **배포 경로**: /home/ec2-user/daily-harmony
- **포트**: 5000

### 기술 스택
- **Backend**: Python Flask
- **AI 모델**: AWS Bedrock - Claude 3.5 Haiku (us.anthropic.claude-3-5-haiku-20241022-v1:0)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **세션 관리**: Flask Session (대화 기억 기능)

---

## 구현된 기능

### 1. 대화 기억 기능 ✅
- Flask 세션 기반으로 최근 20개 대화 기록 저장
- 사용자가 "내가 방금 뭐라고 했어?"라고 물어도 기억함
- `/clear_history` API로 대화 기록 초기화 가능

### 2. AI 챗봇 ✅
- AWS Bedrock의 Claude 3.5 Haiku 모델 사용
- 수강신청 과목 파싱 및 시간표 생성
- 시간 충돌 감지 기능

### 3. UI ✅
- Bootstrap 5 기반 반응형 디자인
- 카카오톡 스타일 채팅 UI
- 그라데이션 배경 및 현대적인 디자인

### 4. 배포 준비 ✅
- systemd 서비스 파일 (`daily-harmony.service`)
- 배포 스크립트 (`deploy.sh`)
- Windows 배치 파일 (EC2 접속, 파일 업로드)

---

## 다음 작업 (이어서 해야 할 일)

### 우선순위 1: EC2 배포 및 테스트
1. **로컬에서 테스트**
   ```bash
   cd /home/user/gogod/daily-harmony
   pip install -r requirements.txt
   python app.py
   # 브라우저에서 http://localhost:5000 접속하여 테스트
   ```

2. **EC2에 배포** (사용자가 Windows에서 실행)
   - 사용자에게 다음 PowerShell 명령어 제공:
   ```powershell
   scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r C:\Users\LENOVO\gogod\daily-harmony ec2-user@18.217.233.121:/home/ec2-user/
   ```

3. **EC2에서 설정** (SSH 접속 후)
   ```bash
   cd /home/ec2-user/daily-harmony
   pip install -r requirements.txt --user
   sudo cp daily-harmony.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl start daily-harmony
   sudo systemctl enable daily-harmony
   sudo systemctl status daily-harmony
   ```

4. **웹 접속 테스트**
   - http://18.217.233.121:5000
   - 대화 기억 기능 테스트
   - 수강신청 시간표 생성 테스트

### 우선순위 2: 디버깅 및 개선
- 에러 발생 시 로그 확인: `sudo journalctl -u daily-harmony -n 50 -f`
- AWS 자격 증명 오류 해결
- 포트 충돌 문제 해결
- UI/UX 개선 (필요 시)

### 우선순위 3: 추가 기능 구현 (선택사항)
- 할 일 관리 (Todo List) 기능
- 습관 트래커 (Habit Tracker) 기능
- 간단한 가계부 기능
- 사용자 인증 시스템
- 데이터베이스 연동 (SQLite)

---

## 주요 파일 설명

### 1. `app.py` (Flask 메인 앱)
- `/` : 메인 페이지
- `/chat` : AI 챗봇 대화 API (POST)
- `/clear_history` : 대화 기록 초기화 API (POST)
- `/timetable` : 시간표 생성 API (POST) - 현재 미사용

**핵심 기능:**
- `session['chat_history']`: 대화 기록 저장 (최근 20개)
- Claude API 호출 시 전체 대화 기록 전송하여 문맥 유지

### 2. `templates/index.html` (웹 UI)
- 채팅 인터페이스
- 메시지 전송 및 표시
- 대화 초기화 버튼

### 3. `WINDOWS_CMD_GUIDE.md` (명령어 가이드)
- 로컬 테스트 방법
- EC2 배포 전체 프로세스
- 문제 해결 가이드

---

## 문제 해결 팁

### AWS 자격 증명 오류
```bash
# EC2에서 실행
aws configure
# 또는
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

### 포트 5000 이미 사용 중
```bash
sudo lsof -i :5000
sudo kill -9 [PID]
```

### 서비스 로그 확인
```bash
sudo journalctl -u daily-harmony -n 50 -f
```

### 파일 권한 문제
```bash
sudo chown -R ec2-user:ec2-user /home/ec2-user/daily-harmony
chmod +x deploy.sh
```

---

## 테스트 시나리오

### 1. 대화 기억 기능 테스트
1. 사용자: "안녕"
2. AI: "안녕하세요!"
3. 사용자: "내가 방금 뭐라고 했어?"
4. AI: "방금 '안녕'이라고 하셨습니다."

### 2. 수강신청 시간표 테스트
사용자 입력:
```
컴퓨터과학개론 월수 10:00-11:30
자료구조 화목 13:00-14:30
영어회화 월수 13:00-14:00
```

AI가 시간표 형식으로 정리하고 충돌 여부 확인

---

## 사용자 요구사항

사용자가 원하는 것:
1. ✅ 대화 기억 기능 (완료)
2. ✅ 무료 AI 모델 사용 (Claude 3.5 Haiku 완료)
3. ✅ 수강신청 시간표 자동 생성 (완료)
4. ⏳ EC2에 배포 (진행 중)

---

## 명령어 요약

### Windows에서 실행 (사용자용)
```powershell
# EC2 접속
ssh -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem ec2-user@18.217.233.121

# 파일 업로드
scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r C:\Users\LENOVO\gogod\daily-harmony ec2-user@18.217.233.121:/home/ec2-user/
```

### EC2에서 실행
```bash
# 설치 및 시작
cd /home/ec2-user/daily-harmony
./deploy.sh

# 로그 확인
sudo journalctl -u daily-harmony -f
```

---

## 주의사항

1. **AWS 자격 증명**: EC2에서 AWS CLI가 설정되어 있어야 Bedrock API 호출 가능
2. **보안 그룹**: EC2 보안 그룹에서 5000 포트 개방 필요
3. **세션 비밀키**: `app.py`의 `app.secret_key`는 프로덕션에서 변경 권장
4. **HTTPS**: 현재는 HTTP만 지원, HTTPS 필요 시 nginx + Let's Encrypt 추가 필요

---

## Git 정보

- **저장소**: gogod
- **브랜치**: `claude/deploy-ai-learning-assistant-014q5hiGuMRXTWZn5dbsggSW`
- **최근 커밋**: "Add Daily Harmony - AI Course Registration Assistant"

---

## 사용자 환경

- **OS**: Windows
- **로컬 경로**: C:\Users\LENOVO\gogod\daily-harmony
- **EC2 키 경로**: C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem
- **선호 도구**: CMD, PowerShell

---

## 다음 AI에게 전달할 메시지

"Daily Harmony 프로젝트를 EC2에 배포하고 테스트해주세요.
위의 정보를 참고하여 다음 작업을 수행해주세요:

1. 로컬에서 앱이 정상 작동하는지 테스트
2. EC2에 배포하는 방법을 사용자에게 안내 (Windows CMD/PowerShell 명령어 제공)
3. 배포 후 웹사이트 접속 테스트
4. 대화 기억 기능 및 시간표 생성 기능 테스트
5. 문제 발생 시 디버깅 및 해결

사용자는 Windows 환경에서 작업하며, EC2 정보는 위와 같습니다.
모든 파일은 `/home/user/gogod/daily-harmony/` 경로에 있습니다."
