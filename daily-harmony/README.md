# Daily Harmony - 수강신청 도우미

AI 기반 수강신청 도우미 웹 애플리케이션입니다.

## 주요 기능

1. **대화 기억 기능**: 이전 대화 내용을 기억하여 문맥에 맞는 응답 제공
2. **Claude 3.5 Haiku 모델**: AWS Bedrock의 최신 무료 모델 사용
3. **시간표 자동 생성**: 수강 과목 입력 시 자동으로 시간표 생성
4. **충돌 감지**: 겹치는 수업 시간 자동 확인

## 로컬 실행 방법

### 1. 의존성 설치

```bash
cd daily-harmony
pip install -r requirements.txt
```

### 2. AWS 자격 증명 설정

AWS CLI가 설정되어 있어야 합니다:

```bash
aws configure
```

또는 환경 변수로 설정:

```bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

### 3. 앱 실행

```bash
python app.py
```

### 4. 브라우저에서 접속

```
http://localhost:5000
```

## EC2 배포 방법

### 1. EC2 접속

```bash
ssh -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem ec2-user@18.217.233.121
```

### 2. 프로젝트 업로드

```bash
# 로컬에서 실행 (Windows PowerShell)
scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r daily-harmony ec2-user@18.217.233.121:/home/ec2-user/
```

### 3. EC2에서 설정

```bash
# EC2 접속 후
cd /home/ec2-user/daily-harmony
pip install -r requirements.txt

# systemd 서비스 생성
sudo nano /etc/systemd/system/daily-harmony.service
```

**서비스 파일 내용:**

```ini
[Unit]
Description=Daily Harmony Service
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/daily-harmony
Environment="PATH=/home/ec2-user/.local/bin:/usr/local/bin:/usr/bin"
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### 4. 서비스 시작

```bash
sudo systemctl daemon-reload
sudo systemctl start daily-harmony
sudo systemctl enable daily-harmony
sudo systemctl status daily-harmony
```

### 5. 로그 확인

```bash
sudo journalctl -u daily-harmony -n 50 -f
```

## 사용 예시

### 수강신청 과목 입력

```
컴퓨터과학개론 월수 10:00-11:30
자료구조 화목 13:00-14:30
영어회화 월수 13:00-14:00
선형대수학 화목 10:00-12:00
```

### AI 응답 예시

AI가 자동으로:
- 과목명, 요일, 시간을 파싱
- 시간표 형태로 정리
- 시간 충돌 여부 확인
- 최적의 시간표 추천

## 기술 스택

- **Backend**: Python Flask
- **AI**: AWS Bedrock (Claude 3.5 Haiku)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Session**: Flask Session (대화 기록 저장)

## 포트

- **개발**: 5000
- **프로덕션**: 5000 (또는 원하는 포트로 변경 가능)

## 라이선스

MIT License
