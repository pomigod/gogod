# 🚀 빠른 시작 가이드

**건양대 6팀 AI 학습 도우미 - 5분 안에 배포하기!**

---

## 📌 이 프로젝트는 무엇인가요?

AWS Bedrock의 Claude AI를 활용한 학교 학습 지원 웹 서비스입니다.
학생들이 질문을 입력하면 AI가 실시간으로 답변해줍니다!

**예시 질문**:
- "파이썬에서 리스트와 튜플의 차이점은?"
- "2차 방정식을 푸는 방법을 설명해줘"
- "광합성 과정을 간단히 설명해줘"

---

## ⚡ 가장 빠른 배포 방법 (5분)

### Step 1: AWS Console 로그인 (1분)

1. 브라우저에서 열기: https://nxtcloud.signin.aws.amazon.com/console
2. 입력:
   - IAM 사용자: `kyuniv-pj-06`
   - 비밀번호: (제공받은 비밀번호)
3. 우측 상단 리전: **버지니아 북부 (us-east-1)** 선택

### Step 2: EC2 인스턴스 생성 (2분)

1. 상단 검색: "EC2" 입력 → EC2 클릭
2. "인스턴스 시작" 버튼 클릭
3. 빠른 설정:
   ```
   이름: ai-assistant
   AMI: Amazon Linux 2023 (기본값)
   인스턴스 타입: t3.small
   키 페어: 새로 생성 (이름: my-key, 다운로드 필수!)
   ```
4. "고급 세부 정보" 펼치기 → **IAM 인스턴스 프로필: SafeInstanceProfileForUser-kyuniv-pj-06** 선택
5. 보안 그룹:
   - SSH (포트 22): 내 IP
   - 사용자 지정 TCP (포트 5000): 0.0.0.0/0
6. "인스턴스 시작" 클릭!

### Step 3: 배포 (2분)

EC2 인스턴스 접속:
```bash
# 키 파일 권한 설정
chmod 400 my-key.pem

# SSH 접속 (<퍼블릭-IP>는 EC2 콘솔에서 확인)
ssh -i my-key.pem ec2-user@<퍼블릭-IP>
```

한 번에 배포:
```bash
# 프로젝트 클론 및 배포 실행
git clone https://github.com/pomigod/gogod.git ai-learning-assistant && \
cd ai-learning-assistant && \
chmod +x deploy.sh && \
./deploy.sh
```

### Step 4: 접속! (즉시)

웹 브라우저에서:
```
http://<EC2-퍼블릭-IP>:5000
```

**축하합니다! 🎉 배포 완료!**

---

## 📖 자세한 가이드가 필요하다면?

- **AWS 배포 상세 가이드**: `AWS_DEPLOYMENT_GUIDE.md` 참조
- **로컬 테스트**: `LOCAL_TEST_GUIDE.md` 참조
- **프로젝트 문서**: `README.md` 참조
- **진행 현황**: `PROJECT_PROGRESS.md` 참조

---

## 🛠️ 서비스 관리

### 서비스 상태 확인
```bash
sudo systemctl status ai-assistant
```

### 로그 확인
```bash
sudo journalctl -u ai-assistant -f
```

### 서비스 재시작
```bash
sudo systemctl restart ai-assistant
```

---

## ❓ 문제 해결

### 웹 페이지 접속이 안돼요!
1. EC2 보안 그룹에서 포트 5000 확인
2. 서비스 상태 확인: `sudo systemctl status ai-assistant`

### AI 답변이 안나와요!
1. IAM 인스턴스 프로필이 설정되어 있는지 확인
2. 리전이 버지니아 북부(us-east-1)인지 확인

### 배포 스크립트가 실패해요!
1. 인터넷 연결 확인
2. Python 3 설치 확인: `python3 --version`

---

## 💰 사용 후 비용 절감

**사용하지 않을 때는 인스턴스 중지!**

EC2 콘솔 > 인스턴스 선택 > 인스턴스 상태 > 중지

---

## 🎓 프로젝트 구조

```
ai-learning-assistant/
├── app.py                    # Flask 백엔드
├── templates/index.html      # 웹 인터페이스
├── deploy.sh                 # 배포 스크립트
├── requirements.txt          # Python 패키지
├── README.md                 # 프로젝트 문서
├── AWS_DEPLOYMENT_GUIDE.md   # 상세 배포 가이드
├── LOCAL_TEST_GUIDE.md       # 로컬 테스트 가이드
└── PROJECT_PROGRESS.md       # 진행 현황
```

---

## 📞 도움이 필요하신가요?

- AWS 관련: 999 채널 또는 @NxtCloud_김유림
- 프로젝트 관련: 팀원에게 문의

---

**건양대학교 AI 부트캠프 6팀**

즐거운 학습 되세요! 😊
