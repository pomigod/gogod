# 🎓 AI 학습 도우미

**건양대학교 AI 부트캠프 6팀 프로젝트**

프로젝트 기간: 2024.11.02 ~ 2024.11.30

---

## 📋 프로젝트 소개

AI 학습 도우미는 AWS Bedrock의 Claude AI를 활용하여 학생들의 학습을 돕는 웹 애플리케이션입니다.

### 주요 기능

- 💬 **AI 챗봇**: Claude AI를 활용한 실시간 학습 질문 답변
- 🎯 **학교 특화**: 학교 학습에 최적화된 답변 제공
- 🚀 **간편한 사용**: 직관적인 웹 인터페이스
- ☁️ **클라우드 기반**: AWS 서비스를 활용한 안정적인 서비스

### 기술 스택

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **AI**: AWS Bedrock (Claude 3 Haiku)
- **Deployment**: AWS EC2
- **Authentication**: AWS IAM Role

---

## 🚀 빠른 시작

### 1. 로컬 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 애플리케이션 실행
python app.py
```

브라우저에서 `http://localhost:5000` 접속

### 2. AWS EC2 배포

#### EC2 인스턴스 생성

1. AWS Console 로그인
   - URL: https://nxtcloud.signin.aws.amazon.com/console
   - IAM Username: `kyuniv-pj-06`
   - Region: **버지니아 북부 (us-east-1)**

2. EC2 인스턴스 생성
   - AMI: Amazon Linux 2023
   - 인스턴스 타입: `t3.small` (권장) 또는 `t3.micro`
   - 인스턴스 프로필: `SafeInstanceProfileForUser-kyuniv-pj-06` ⚠️ **필수!**
   - 보안 그룹: 포트 5000 인바운드 허용

3. 인스턴스 접속 후 배포

```bash
# 프로젝트 파일 업로드 (git clone 또는 scp 사용)
git clone <repository-url>
cd ai-learning-assistant

# 배포 스크립트 실행
chmod +x deploy.sh
./deploy.sh
```

#### 중요 설정 사항

⚠️ **반드시 확인하세요!**

- EC2 인스턴스에 IAM 인스턴스 프로필 `SafeInstanceProfileForUser-kyuniv-pj-06` 연결 필수
- 보안 그룹에서 포트 5000 인바운드 규칙 추가
- 리전은 **버지니아 북부 (us-east-1)** 사용 (Bedrock 사용 가능 리전)

---

## 🏗️ 프로젝트 구조

```
ai-learning-assistant/
├── app.py                 # Flask 메인 애플리케이션
├── templates/
│   └── index.html        # 웹 인터페이스
├── requirements.txt      # Python 의존성
├── deploy.sh            # AWS EC2 배포 스크립트
├── README.md            # 프로젝트 문서
└── AWS DeepRacer code   # AWS DeepRacer 관련 코드 (참고용)
```

---

## 🔧 AWS 설정 정보

### IAM 사용자 정보
- **IAM Username**: `kyuniv-pj-06`
- **EC2 Instance Profile**: `SafeInstanceProfileForUser-kyuniv-pj-06`
- **Lambda/기타 Role**: `SafeRoleForUser-kyuniv-pj-06`

### 사용 가능 서비스
- Cloud9, EC2, Lambda, RDS, DynamoDB, S3
- API Gateway, Amplify, SQS, SNS
- **Bedrock** (버지니아 북부, 오하이오, 오레곤)

### 제약 사항
- EC2 인스턴스 타입: `t3.nano` ~ `t3.medium`
- 리전: 버지니아 북부 (us-east-1) 권장
- Access Key 발급 불가 (IAM Role 사용)

---

## 📱 사용 방법

1. 웹 브라우저에서 서비스 접속
2. 질문 입력창에 학습 관련 질문 입력
3. "질문하기" 버튼 클릭 또는 Enter 키 입력
4. AI의 답변 확인

### 질문 예시

- "파이썬에서 리스트와 튜플의 차이점은?"
- "2차 방정식을 푸는 방법을 설명해줘"
- "영어 문법에서 현재완료와 과거형의 차이는?"
- "광합성 과정을 간단히 설명해줘"

---

## 🔍 서비스 관리

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

## 🛠️ 트러블슈팅

### Bedrock 연결 오류
- EC2 인스턴스에 올바른 IAM 인스턴스 프로필이 연결되어 있는지 확인
- 리전이 버지니아 북부 (us-east-1)인지 확인

### 웹 페이지 접속 불가
- EC2 보안 그룹에서 포트 5000 인바운드 규칙 확인
- 서비스 상태 확인: `sudo systemctl status ai-assistant`

### 권한 오류
- IAM 역할 `SafeRoleForUser-kyuniv-pj-06`에 Bedrock 권한이 있는지 확인

---

## 👥 팀 정보

**건양대학교 AI 부트캠프 6팀**

프로젝트 기간: 2024.11.02 ~ 2024.11.30

---

## 📄 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

---

## 📞 문의

프로젝트 관련 문의사항이 있으시면 팀원에게 연락해주세요.

---

## 🔗 참고 자료

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

## AWS DeepRacer Code

이 레포지토리에는 AWS DeepRacer 챌린지를 위한 보상 함수(Reward Functions)도 포함되어 있습니다.

### 주요 모델

1. **기본 모델**: 트랙 완주 중심
2. **Waypoints 추적 모델**: 방향 정확도 기반
3. **회피 최적화 모델**: 장애물 회피 중심

자세한 내용은 `AWS DeepRacer code` 파일을 참조하세요.
