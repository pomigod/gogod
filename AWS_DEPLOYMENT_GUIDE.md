# 🚀 AWS EC2 배포 가이드

**건양대 6팀 - AI 학습 도우미 배포 가이드**

---

## 📋 사전 준비사항

### 1. AWS 계정 정보
- **IAM Username**: `kyuniv-pj-06`
- **Console URL**: https://nxtcloud.signin.aws.amazon.com/console
- **리전**: 버지니아 북부 (us-east-1)
- **EC2 Instance Profile**: `SafeInstanceProfileForUser-kyuniv-pj-06`

### 2. 필요한 도구
- SSH 클라이언트 (Windows: PuTTY, Mac/Linux: 터미널)
- 웹 브라우저

---

## 🔐 Step 1: AWS Console 로그인

1. https://nxtcloud.signin.aws.amazon.com/console 접속
2. IAM 사용자 이름 입력: `kyuniv-pj-06`
3. 비밀번호 입력 (최초 로그인 시 변경 필요)
4. 우측 상단 리전을 **버지니아 북부 (us-east-1)**로 변경

---

## 💻 Step 2: EC2 인스턴스 생성

### 2-1. EC2 대시보드 접속
1. 상단 검색창에 "EC2" 입력
2. "EC2" 서비스 클릭
3. "인스턴스 시작" 버튼 클릭

### 2-2. 인스턴스 설정

#### 이름 및 태그
```
이름: ai-learning-assistant
```

#### 애플리케이션 및 OS 이미지 (AMI)
```
AMI: Amazon Linux 2023 AMI (기본값)
아키텍처: 64비트 (x86)
```

#### 인스턴스 유형
```
인스턴스 유형: t3.small (권장) 또는 t3.micro
```
- t3.micro: 메모리 1GB (테스트용)
- t3.small: 메모리 2GB (권장)

#### 키 페어
```
1. "새 키 페어 생성" 클릭
2. 키 페어 이름: kyuniv-pj-06-key
3. 키 페어 유형: RSA
4. 프라이빗 키 파일 형식: .pem (Mac/Linux) 또는 .ppk (Windows/PuTTY)
5. "키 페어 생성" 클릭
6. ⚠️ 다운로드된 키 파일 안전하게 보관!
```

#### 네트워크 설정
```
VPC: 기본 VPC
서브넷: 기본값
퍼블릭 IP 자동 할당: 활성화
```

**보안 그룹 설정**
```
보안 그룹 이름: ai-assistant-sg
설명: AI Learning Assistant Security Group

인바운드 보안 그룹 규칙:
1. SSH
   - 유형: SSH
   - 프로토콜: TCP
   - 포트: 22
   - 소스: 내 IP (또는 0.0.0.0/0)

2. 웹 애플리케이션
   - 유형: 사용자 지정 TCP
   - 프로토콜: TCP
   - 포트: 5000
   - 소스: 0.0.0.0/0
```

#### 스토리지 구성
```
크기: 8 GiB (기본값)
볼륨 유형: gp3 (기본값)
```

#### 고급 세부 정보
⚠️ **중요: 반드시 설정해야 합니다!**

```
IAM 인스턴스 프로필: SafeInstanceProfileForUser-kyuniv-pj-06
```

이 설정이 없으면 Bedrock에 접근할 수 없습니다!

### 2-3. 인스턴스 시작
```
우측 하단 "인스턴스 시작" 버튼 클릭
```

---

## 🔌 Step 3: EC2 인스턴스 접속

### 3-1. 퍼블릭 IP 확인
1. EC2 대시보드 > 인스턴스
2. 생성한 인스턴스 선택
3. "퍼블릭 IPv4 주소" 복사 (예: 3.xxx.xxx.xxx)

### 3-2. SSH 접속

#### Mac/Linux
```bash
# 키 파일 권한 설정 (최초 1회)
chmod 400 kyuniv-pj-06-key.pem

# SSH 접속
ssh -i kyuniv-pj-06-key.pem ec2-user@<퍼블릭-IP>
```

#### Windows (PuTTY)
1. PuTTY 실행
2. Host Name: `ec2-user@<퍼블릭-IP>`
3. Connection > SSH > Auth > Credentials: .ppk 파일 선택
4. Open 클릭

---

## 📦 Step 4: 프로젝트 배포

### 4-1. 프로젝트 파일 업로드

#### 방법 1: Git Clone (권장)
```bash
# Git 설치
sudo yum install -y git

# 프로젝트 클론
git clone https://github.com/your-username/ai-learning-assistant.git
cd ai-learning-assistant
```

#### 방법 2: 파일 직접 업로드
```bash
# 로컬에서 EC2로 파일 복사 (새 터미널)
scp -i kyuniv-pj-06-key.pem -r ./ai-learning-assistant ec2-user@<퍼블릭-IP>:/home/ec2-user/
```

### 4-2. 배포 스크립트 실행

```bash
# 프로젝트 디렉토리로 이동
cd ai-learning-assistant

# 배포 스크립트 실행 권한 부여
chmod +x deploy.sh

# 배포 실행
./deploy.sh
```

스크립트가 자동으로 다음 작업을 수행합니다:
- ✅ 시스템 패키지 업데이트
- ✅ Python 3 및 pip 설치
- ✅ 가상환경 생성
- ✅ Python 패키지 설치
- ✅ systemd 서비스 등록
- ✅ 서비스 시작

### 4-3. 배포 완료 확인

```bash
# 서비스 상태 확인
sudo systemctl status ai-assistant

# 출력 예시:
# ● ai-assistant.service - AI Learning Assistant
#    Loaded: loaded
#    Active: active (running)
```

---

## ✅ Step 5: 서비스 테스트

### 5-1. 웹 브라우저 접속

```
주소: http://<EC2-퍼블릭-IP>:5000
```

예: `http://3.145.123.456:5000`

### 5-2. 기능 테스트

1. 웹 페이지가 정상적으로 로드되는지 확인
2. 질문 입력창에 질문 입력: "파이썬이란?"
3. "질문하기" 버튼 클릭
4. AI 답변이 정상적으로 표시되는지 확인

---

## 🔧 Step 6: 서비스 관리

### 서비스 명령어

```bash
# 서비스 시작
sudo systemctl start ai-assistant

# 서비스 중지
sudo systemctl stop ai-assistant

# 서비스 재시작
sudo systemctl restart ai-assistant

# 서비스 상태 확인
sudo systemctl status ai-assistant

# 부팅 시 자동 시작 활성화
sudo systemctl enable ai-assistant

# 부팅 시 자동 시작 비활성화
sudo systemctl disable ai-assistant
```

### 로그 확인

```bash
# 실시간 로그 확인
sudo journalctl -u ai-assistant -f

# 최근 100줄 로그 확인
sudo journalctl -u ai-assistant -n 100

# 오늘 날짜 로그만 확인
sudo journalctl -u ai-assistant --since today
```

---

## 🐛 트러블슈팅

### 문제 1: 웹 페이지 접속 안됨

**원인**: 보안 그룹 설정 문제

**해결**:
1. EC2 > 보안 그룹
2. ai-assistant-sg 선택
3. 인바운드 규칙 확인
4. 포트 5000이 0.0.0.0/0으로 오픈되어 있는지 확인

### 문제 2: Bedrock 연결 오류

**원인**: IAM 인스턴스 프로필 미설정

**해결**:
1. EC2 > 인스턴스
2. 인스턴스 선택 > 작업 > 보안 > IAM 역할 수정
3. IAM 역할: `SafeInstanceProfileForUser-kyuniv-pj-06` 선택
4. 저장
5. 서비스 재시작: `sudo systemctl restart ai-assistant`

### 문제 3: 서비스 시작 실패

**원인**: Python 패키지 설치 문제

**해결**:
```bash
# 가상환경 활성화
cd /home/ec2-user/ai-learning-assistant
source venv/bin/activate

# 패키지 재설치
pip install -r requirements.txt

# 서비스 재시작
sudo systemctl restart ai-assistant
```

### 문제 4: Permission Denied 오류

**원인**: 파일 권한 문제

**해결**:
```bash
# 파일 소유자 변경
sudo chown -R ec2-user:ec2-user /home/ec2-user/ai-learning-assistant

# 실행 권한 추가
chmod +x deploy.sh
```

---

## 📊 모니터링

### 시스템 리소스 확인

```bash
# CPU 및 메모리 사용량
top

# 디스크 사용량
df -h

# 네트워크 연결 확인
netstat -tuln | grep 5000
```

### 애플리케이션 상태

```bash
# 프로세스 확인
ps aux | grep python

# 포트 확인
sudo lsof -i :5000
```

---

## 🔒 보안 체크리스트

- ✅ IAM 인스턴스 프로필 설정
- ✅ 보안 그룹 최소 권한 설정
- ✅ SSH 키 페어 안전하게 보관
- ✅ 불필요한 포트 차단
- ✅ 정기적인 시스템 업데이트

---

## 💰 비용 관리

### 사용 중인 리소스
- EC2 t3.small: 시간당 약 $0.0208
- 데이터 전송: GB당 약 $0.09
- Bedrock API 호출: 건당 약 $0.00025

### 비용 절감 팁
1. **사용하지 않을 때 인스턴스 중지**
   ```bash
   # EC2 대시보드에서 인스턴스 선택 > 인스턴스 상태 > 중지
   ```

2. **CloudWatch로 사용량 모니터링**

3. **불필요한 리소스 삭제**

---

## 📞 지원 및 문의

### AWS 관련 문의
- 999 채널을 통해 문의
- @NxtCloud_김유림 멘션

### 프로젝트 관련 문의
- 팀원에게 연락

---

## 🎉 배포 완료!

축하합니다! AI 학습 도우미가 성공적으로 배포되었습니다.

**최종 확인사항**:
- ✅ EC2 인스턴스 실행 중
- ✅ 웹 페이지 접속 가능
- ✅ AI 질문 답변 정상 작동
- ✅ 서비스 자동 재시작 설정

**다음 단계**:
1. 프로젝트 문서 작성 완료
2. 팀원들과 테스트 진행
3. 최종 발표 자료 준비

---

**건양대학교 AI 부트캠프 6팀**

작성일: 2024.11.14
