# Daily Harmony 프로젝트 인계 - Gemini용 가이드

## 🎯 목표
Daily Harmony AI 수강신청 도우미를 EC2에 배포하고 테스트하기

---

## 📁 프로젝트 파일 위치

### 현재 파일 위치 (Claude 작업 환경)
```
/home/user/gogod/daily-harmony/
```

### Gemini 작업 환경으로 복사 필요
사용자가 다음 경로로 파일을 복사해야 합니다:
```
C:\Users\LENOVO\.gemini\antigravity\playground\interstellar-nadir\daily-harmony\
```

**복사할 파일 목록:**
```
daily-harmony/
├── app.py                    # Flask 메인 앱
├── templates/
│   └── index.html           # 웹 UI
├── static/                   # (빈 폴더)
│   ├── css/
│   └── js/
├── requirements.txt         # Python 의존성
├── deploy.sh                # 배포 스크립트
├── daily-harmony.service    # systemd 서비스
├── connect-ec2.bat          # EC2 접속 배치
├── upload-to-ec2.bat        # 파일 업로드 배치
├── README.md                # 프로젝트 설명
└── WINDOWS_CMD_GUIDE.md     # Windows 명령어 가이드
```

---

## 🔑 SSH 키 파일

### 키 파일 경로 (사용자가 제공해야 함)
```
원본: C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem
복사: C:\Users\LENOVO\.gemini\antigravity\playground\interstellar-nadir\kyuniv-pj-06-key.pem
```

**⚠️ 중요**: SSH 키 파일은 보안상 중요하므로 사용자가 직접 복사해야 합니다!

---

## 🖥️ EC2 서버 정보

```
IP 주소: 18.217.233.121
사용자명: ec2-user
SSH 키: kyuniv-pj-06-key.pem
포트: 5000
배포 경로: /home/ec2-user/daily-harmony
```

### SSH 접속 명령어
```bash
ssh -i kyuniv-pj-06-key.pem ec2-user@18.217.233.121
```

---

## 🚀 배포 프로세스

### 1단계: 로컬 테스트 (선택사항)
```bash
cd daily-harmony
pip install -r requirements.txt
python app.py
# 브라우저: http://localhost:5000
```

### 2단계: EC2에 파일 업로드
```powershell
scp -i kyuniv-pj-06-key.pem -r daily-harmony ec2-user@18.217.233.121:/home/ec2-user/
```

### 3단계: EC2에서 설정
```bash
# SSH 접속
ssh -i kyuniv-pj-06-key.pem ec2-user@18.217.233.121

# 설정 실행
cd /home/ec2-user/daily-harmony
pip install -r requirements.txt --user
sudo cp daily-harmony.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start daily-harmony
sudo systemctl enable daily-harmony
sudo systemctl status daily-harmony
```

### 4단계: 웹 접속 테스트
```
http://18.217.233.121:5000
```

---

## 💻 기술 정보

### 사용 기술
- **Backend**: Python 3 + Flask 3.0.0
- **AI 모델**: AWS Bedrock - Claude 3.5 Haiku (us.anthropic.claude-3-5-haiku-20241022-v1:0)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **세션 관리**: Flask Session

### AWS 설정
EC2에서 AWS CLI 자격 증명이 설정되어 있어야 합니다:
```bash
aws configure
# 또는
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

---

## ✨ 구현된 핵심 기능

### 1. 대화 기억 기능 ✅
- Flask 세션으로 최근 20개 대화 저장
- 이전 대화 문맥 유지
- 예: "내가 방금 뭐라고 했어?" → AI가 기억하고 답변

**코드 위치**: `app.py:85-100` (session['chat_history'])

### 2. AI 챗봇 ✅
- Claude 3.5 Haiku 모델 사용 (무료)
- 자연어 대화 처리
- 수강신청 도움

**코드 위치**: `app.py:67-125` (/chat 엔드포인트)

### 3. 시간표 자동 생성 ✅
- 수강 과목 파싱
- 시간표 형식 변환
- 시간 충돌 감지

**코드 위치**: `app.py:26-63` (parse_courses, generate_timetable, check_conflicts)

### 4. 웹 UI ✅
- 카카오톡 스타일 채팅 UI
- 반응형 디자인
- 대화 초기화 버튼

**코드 위치**: `templates/index.html`

---

## 🧪 테스트 시나리오

### 테스트 1: 대화 기억
```
사용자: "안녕"
AI: "안녕하세요!"
사용자: "내가 방금 뭐라고 했어?"
AI: "'안녕'이라고 하셨습니다." (대화 기억 성공!)
```

### 테스트 2: 수강신청 시간표
```
사용자 입력:
컴퓨터과학개론 월수 10:00-11:30
자료구조 화목 13:00-14:30
영어회화 월수 13:00-14:00
선형대수학 화목 10:00-12:00

AI 응답:
- 과목 파싱
- 시간표 형식 출력
- 충돌 여부 확인
```

### 테스트 3: 대화 초기화
```
"대화 초기화" 버튼 클릭
→ 세션 리셋
→ 새로운 대화 시작
```

---

## 🔧 문제 해결

### 문제 1: AWS 자격 증명 오류
```bash
aws configure
# 또는
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

### 문제 2: 포트 5000 사용 중
```bash
sudo lsof -i :5000
sudo kill -9 [PID]
```

### 문제 3: 서비스 실행 안 됨
```bash
# 로그 확인
sudo journalctl -u daily-harmony -n 50 -f

# 수동 실행으로 에러 확인
cd /home/ec2-user/daily-harmony
python app.py
```

### 문제 4: 패키지 설치 오류
```bash
pip install -r requirements.txt --user
# 또는
sudo pip install -r requirements.txt
```

### 문제 5: 파일 권한 문제
```bash
sudo chown -R ec2-user:ec2-user /home/ec2-user/daily-harmony
chmod +x deploy.sh
```

---

## 📝 주요 파일 코드 설명

### app.py 핵심 부분
```python
# 1. 대화 기록 관리
@app.route('/chat', methods=['POST'])
def chat():
    chat_history = session.get('chat_history', [])  # 세션에서 기록 가져오기
    chat_history.append({'role': 'user', 'content': user_message})
    # ... Claude API 호출 ...
    chat_history.append({'role': 'assistant', 'content': assistant_message})
    session['chat_history'] = chat_history[-20:]  # 최근 20개만 저장
```

### 서비스 관리 명령어
```bash
# 시작
sudo systemctl start daily-harmony

# 중지
sudo systemctl stop daily-harmony

# 재시작
sudo systemctl restart daily-harmony

# 상태 확인
sudo systemctl status daily-harmony

# 로그 보기
sudo journalctl -u daily-harmony -f
```

---

## 📦 의존성 패키지

```
Flask==3.0.0
boto3==1.34.34
Werkzeug==3.0.1
```

---

## 🎬 작업 시작 체크리스트

- [ ] daily-harmony 폴더를 Gemini 작업 공간으로 복사
- [ ] kyuniv-pj-06-key.pem 파일을 작업 공간으로 복사
- [ ] 로컬에서 앱 테스트 (선택사항)
- [ ] EC2에 파일 업로드
- [ ] EC2에서 서비스 설정
- [ ] 웹 브라우저로 접속 테스트
- [ ] 대화 기억 기능 테스트
- [ ] 시간표 생성 기능 테스트
- [ ] 에러 발생 시 로그 확인 및 디버깅

---

## 🌐 접속 URL

- **로컬**: http://localhost:5000
- **프로덕션**: http://18.217.233.121:5000

---

## 📚 추가 문서

작업 공간에 있는 다른 문서들:
- `README.md`: 프로젝트 전체 설명
- `WINDOWS_CMD_GUIDE.md`: Windows 명령어 상세 가이드
- `HANDOFF_PROMPT.md`: 전체 인계 문서

---

## ⚡ 빠른 시작 (요약)

```bash
# 1. 파일 업로드 (PowerShell)
scp -i kyuniv-pj-06-key.pem -r daily-harmony ec2-user@18.217.233.121:/home/ec2-user/

# 2. EC2 접속
ssh -i kyuniv-pj-06-key.pem ec2-user@18.217.233.121

# 3. 배포 스크립트 실행
cd /home/ec2-user/daily-harmony
./deploy.sh

# 4. 웹 접속
# http://18.217.233.121:5000
```

---

## 💡 작업 팁

1. **Windows 환경**: 사용자가 Windows를 사용하므로 PowerShell 명령어 제공
2. **에러 처리**: 에러 발생 시 `sudo journalctl -u daily-harmony -f`로 로그 확인
3. **보안**: SSH 키 파일은 절대 공유하지 말 것
4. **테스트**: 배포 전 로컬에서 먼저 테스트 추천

---

## 🆘 사용자에게 요청할 것

작업을 시작하기 전에 사용자에게 다음을 요청하세요:

```
1. daily-harmony 폴더 전체를 다음 경로로 복사해주세요:
   C:\Users\LENOVO\.gemini\antigravity\playground\interstellar-nadir\

2. SSH 키 파일도 같은 위치로 복사해주세요:
   C:\Users\LENOVO\.gemini\antigravity\playground\interstellar-nadir\kyuniv-pj-06-key.pem

3. 복사가 완료되면 알려주세요!
```

그러면 바로 작업을 시작할 수 있습니다.
