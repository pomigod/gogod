#!/bin/bash

# Daily Harmony 배포 스크립트

echo "🚀 Daily Harmony 배포 시작..."

# 작업 디렉토리로 이동
cd /home/ec2-user/daily-harmony || exit 1

# Git pull (선택사항)
# git pull origin main

# 의존성 설치
echo "📦 의존성 설치 중..."
pip install -r requirements.txt --user

# 서비스 재시작
echo "🔄 서비스 재시작 중..."
sudo systemctl restart daily-harmony

# 서비스 상태 확인
echo "✅ 서비스 상태 확인..."
sudo systemctl status daily-harmony --no-pager

echo "🎉 배포 완료!"
echo "접속 주소: http://18.217.233.121:5000"
