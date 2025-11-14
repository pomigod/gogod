#!/bin/bash

echo "=========================================="
echo "AI 학습 도우미 - AWS EC2 배포 스크립트"
echo "건양대 6팀"
echo "=========================================="

# 시스템 업데이트
echo "1. 시스템 패키지 업데이트 중..."
sudo yum update -y

# Python 3 설치
echo "2. Python 3 설치 중..."
sudo yum install -y python3 python3-pip

# Git 설치 (필요시)
echo "3. Git 설치 중..."
sudo yum install -y git

# 프로젝트 디렉토리로 이동 또는 클론
PROJECT_DIR="/home/ec2-user/ai-learning-assistant"

if [ ! -d "$PROJECT_DIR" ]; then
    echo "4. 프로젝트 디렉토리 생성 중..."
    mkdir -p $PROJECT_DIR
fi

cd $PROJECT_DIR

# Python 가상환경 생성
echo "5. Python 가상환경 생성 중..."
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
echo "6. Python 패키지 설치 중..."
pip install --upgrade pip
pip install Flask boto3 Werkzeug

# 방화벽 설정 (포트 5000 오픈)
echo "7. 방화벽 설정 중..."
sudo firewall-cmd --permanent --add-port=5000/tcp 2>/dev/null || echo "방화벽 설정 스킵"
sudo firewall-cmd --reload 2>/dev/null || echo "방화벽 재시작 스킵"

# systemd 서비스 파일 생성
echo "8. 시스템 서비스 설정 중..."
sudo tee /etc/systemd/system/ai-assistant.service > /dev/null <<EOF
[Unit]
Description=AI Learning Assistant
After=network.target

[Service]
Type=simple
User=ec2-user
WorkingDirectory=$PROJECT_DIR
Environment="PATH=$PROJECT_DIR/venv/bin"
ExecStart=$PROJECT_DIR/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# 서비스 활성화 및 시작
echo "9. 서비스 시작 중..."
sudo systemctl daemon-reload
sudo systemctl enable ai-assistant
sudo systemctl restart ai-assistant

# 서비스 상태 확인
echo "=========================================="
echo "배포 완료!"
echo "=========================================="
sudo systemctl status ai-assistant --no-pager

# 접속 정보 출력
PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)
echo ""
echo "=========================================="
echo "접속 정보:"
echo "주소: http://$PUBLIC_IP:5000"
echo "=========================================="
echo ""
echo "서비스 관리 명령어:"
echo "  - 서비스 중지: sudo systemctl stop ai-assistant"
echo "  - 서비스 시작: sudo systemctl start ai-assistant"
echo "  - 서비스 재시작: sudo systemctl restart ai-assistant"
echo "  - 로그 확인: sudo journalctl -u ai-assistant -f"
echo "=========================================="
