# Windows CMD/PowerShell 명령어 가이드

Daily Harmony를 EC2에 배포하는 전체 프로세스입니다.

## 목차
1. [로컬에서 테스트](#1-로컬에서-테스트)
2. [EC2에 파일 업로드](#2-ec2에-파일-업로드)
3. [EC2에서 설정](#3-ec2에서-설정)
4. [서비스 관리](#4-서비스-관리)
5. [문제 해결](#5-문제-해결)

---

## 1. 로컬에서 테스트

### CMD에서 프로젝트 폴더로 이동
```cmd
cd /d C:\Users\LENOVO\gogod\daily-harmony
```

### 가상환경 생성 및 활성화 (선택사항)
```cmd
python -m venv venv
venv\Scripts\activate
```

### 의존성 설치
```cmd
pip install -r requirements.txt
```

### AWS 자격 증명 설정 (환경 변수)
```cmd
set AWS_ACCESS_KEY_ID=your_access_key
set AWS_SECRET_ACCESS_KEY=your_secret_key
set AWS_DEFAULT_REGION=us-east-1
```

### 로컬에서 앱 실행
```cmd
python app.py
```

### 브라우저에서 테스트
```
http://localhost:5000
```

---

## 2. EC2에 파일 업로드

### PowerShell에서 실행 (SCP 사용)

**전체 폴더 업로드:**
```powershell
scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r C:\Users\LENOVO\gogod\daily-harmony ec2-user@18.217.233.121:/home/ec2-user/
```

**개별 파일 업로드 (선택사항):**
```powershell
# app.py만 업로드
scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem C:\Users\LENOVO\gogod\daily-harmony\app.py ec2-user@18.217.233.121:/home/ec2-user/daily-harmony/

# templates 폴더 업로드
scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r C:\Users\LENOVO\gogod\daily-harmony\templates ec2-user@18.217.233.121:/home/ec2-user/daily-harmony/
```

---

## 3. EC2에서 설정

### SSH 접속
```cmd
ssh -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem ec2-user@18.217.233.121
```

### EC2에서 실행할 명령어들

#### 1) 프로젝트 폴더로 이동
```bash
cd /home/ec2-user/daily-harmony
```

#### 2) 의존성 설치
```bash
pip install -r requirements.txt --user
```

#### 3) systemd 서비스 파일 복사
```bash
sudo cp daily-harmony.service /etc/systemd/system/
```

#### 4) 서비스 시작
```bash
sudo systemctl daemon-reload
sudo systemctl start daily-harmony
sudo systemctl enable daily-harmony
```

#### 5) 서비스 상태 확인
```bash
sudo systemctl status daily-harmony
```

---

## 4. 서비스 관리

### 서비스 재시작
```bash
sudo systemctl restart daily-harmony
```

### 서비스 중지
```bash
sudo systemctl stop daily-harmony
```

### 서비스 상태 확인
```bash
sudo systemctl status daily-harmony
```

### 로그 확인 (실시간)
```bash
sudo journalctl -u daily-harmony -f
```

### 로그 확인 (최근 50줄)
```bash
sudo journalctl -u daily-harmony -n 50
```

### 로그 확인 (오늘 날짜)
```bash
sudo journalctl -u daily-harmony --since today
```

---

## 5. 문제 해결

### 포트가 이미 사용 중일 때
```bash
# 5000 포트 사용 중인 프로세스 확인
sudo lsof -i :5000

# 프로세스 종료 (PID는 위 명령어에서 확인)
sudo kill -9 [PID]
```

### Python 패키지 권한 문제
```bash
# --user 옵션으로 설치
pip install -r requirements.txt --user

# 또는 sudo 사용
sudo pip install -r requirements.txt
```

### AWS 자격 증명 오류
```bash
# AWS CLI 설정
aws configure

# 또는 환경 변수 설정
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

### 파일 권한 문제
```bash
# 모든 파일 소유자를 ec2-user로 변경
sudo chown -R ec2-user:ec2-user /home/ec2-user/daily-harmony

# 실행 권한 부여
chmod +x deploy.sh
```

### 방화벽/보안 그룹 설정
EC2 보안 그룹에서 5000 포트 개방 확인:
- AWS Console → EC2 → Security Groups
- Inbound Rules에 5000 포트 추가

---

## 6. 빠른 배포 (스크립트 사용)

### EC2에서 배포 스크립트 실행
```bash
cd /home/ec2-user/daily-harmony
./deploy.sh
```

---

## 7. 접속 URL

### 로컬 테스트
```
http://localhost:5000
```

### EC2 프로덕션
```
http://18.217.233.121:5000
```

---

## 8. 유용한 단축 명령어

### Windows에서 SSH 빠른 접속 (배치 파일)

**connect-ec2.bat 파일 생성:**
```batch
@echo off
ssh -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem ec2-user@18.217.233.121
```

사용법: `connect-ec2.bat` 실행

### Windows에서 SCP 빠른 업로드 (배치 파일)

**upload-to-ec2.bat 파일 생성:**
```batch
@echo off
scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r C:\Users\LENOVO\gogod\daily-harmony ec2-user@18.217.233.121:/home/ec2-user/
echo Upload completed!
pause
```

사용법: `upload-to-ec2.bat` 실행

---

## 9. 전체 배포 프로세스 요약

```powershell
# 1. 로컬에서 파일 업로드
scp -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem -r C:\Users\LENOVO\gogod\daily-harmony ec2-user@18.217.233.121:/home/ec2-user/

# 2. EC2 접속
ssh -i C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem ec2-user@18.217.233.121

# 3. EC2에서 설정 (최초 1회만)
cd /home/ec2-user/daily-harmony
pip install -r requirements.txt --user
sudo cp daily-harmony.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start daily-harmony
sudo systemctl enable daily-harmony

# 4. 이후 업데이트 시
cd /home/ec2-user/daily-harmony
./deploy.sh
```

---

## 참고사항

- **키 파일 경로**: `C:\Users\LENOVO\Downloads\kyuniv-pj-06-key.pem`
- **EC2 IP**: `18.217.233.121`
- **프로젝트 경로 (로컬)**: `C:\Users\LENOVO\gogod\daily-harmony`
- **프로젝트 경로 (EC2)**: `/home/ec2-user/daily-harmony`
- **포트**: `5000`
- **모델**: `us.anthropic.claude-3-5-haiku-20241022-v1:0`
