# 🧪 로컬 테스트 가이드

**AI 학습 도우미 - 로컬 환경에서 테스트하기**

---

## ⚠️ 중요 사항

로컬 환경에서는 AWS Bedrock에 접근할 수 없습니다.
- **이유**: Bedrock은 AWS IAM Role을 통한 인증이 필요하며, 로컬 환경에서는 EC2 인스턴스 프로필을 사용할 수 없습니다.
- **해결**: 실제 AI 기능 테스트는 EC2에 배포한 후 진행해야 합니다.

하지만 웹 인터페이스와 기본 동작은 로컬에서도 확인할 수 있습니다!

---

## 🚀 로컬 실행 방법

### 1. 사전 요구사항
- Python 3.8 이상
- pip (Python 패키지 관리자)

### 2. 설치 및 실행

```bash
# 1. 프로젝트 디렉토리로 이동
cd ai-learning-assistant

# 2. 가상환경 생성 (권장)
python3 -m venv venv

# 3. 가상환경 활성화
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. 의존성 설치
pip install -r requirements.txt

# 5. 애플리케이션 실행
python app.py
```

### 3. 웹 브라우저에서 확인

```
주소: http://localhost:5000
```

---

## 🧪 테스트 가능한 항목

### ✅ 정상 작동 확인 가능
1. **웹 페이지 로딩**
   - 메인 페이지 접속
   - UI 디자인 확인
   - 반응형 레이아웃 확인

2. **헬스체크 API**
   ```bash
   curl http://localhost:5000/health
   # 응답: {"status":"healthy","service":"AI 학습 도우미"}
   ```

3. **프론트엔드 기능**
   - 질문 입력
   - 버튼 클릭
   - 메시지 표시

### ❌ 로컬에서 작동하지 않는 항목
1. **Bedrock AI 연동**
   - 질문 답변 기능
   - 실제 AI 응답

---

## 🔧 로컬 테스트용 모의(Mock) 모드

로컬에서도 기능을 테스트하고 싶다면, app.py를 다음과 같이 수정할 수 있습니다:

### app.py 수정

```python
# ask_ai 함수에 모의 모드 추가
def ask_ai(question):
    """AI에게 질문하고 답변 받기"""

    # 로컬 테스트용 모의 모드
    import os
    if os.environ.get('LOCAL_TEST_MODE') == 'true':
        return f"[모의 답변] '{question}'에 대한 답변입니다. 실제 배포 시 AI가 답변합니다."

    try:
        bedrock = get_bedrock_client()
        # ... 나머지 코드
```

### 실행 방법

```bash
# 환경 변수 설정 후 실행
LOCAL_TEST_MODE=true python app.py
```

---

## 📋 체크리스트

### 배포 전 확인사항
- [ ] 코드에 문법 오류가 없는지 확인
- [ ] requirements.txt에 모든 패키지가 포함되어 있는지 확인
- [ ] templates/index.html이 올바른 위치에 있는지 확인
- [ ] deploy.sh 실행 권한이 있는지 확인

### 로컬 테스트 체크리스트
- [ ] Python 버전 3.8 이상 확인
- [ ] 의존성 패키지 설치 완료
- [ ] 포트 5000이 사용 가능한지 확인
- [ ] 웹 페이지가 정상적으로 로드되는지 확인
- [ ] 헬스체크 API가 응답하는지 확인

---

## 🐛 로컬 환경 트러블슈팅

### 문제 1: 포트 5000이 이미 사용 중

**오류 메시지**:
```
OSError: [Errno 48] Address already in use
```

**해결**:
```bash
# Mac/Linux
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID번호> /F
```

또는 app.py에서 포트 변경:
```python
app.run(host='0.0.0.0', port=8080, debug=False)
```

### 문제 2: 모듈을 찾을 수 없음

**오류 메시지**:
```
ModuleNotFoundError: No module named 'flask'
```

**해결**:
```bash
# 가상환경이 활성화되어 있는지 확인
which python  # 가상환경 경로가 표시되어야 함

# 패키지 재설치
pip install -r requirements.txt
```

### 문제 3: Python 버전 문제

**오류 메시지**:
```
SyntaxError: invalid syntax
```

**해결**:
```bash
# Python 버전 확인
python --version

# Python 3.8 이상이어야 함
# 필요시 Python 업그레이드 또는 python3 명령어 사용
python3 app.py
```

---

## 📊 성능 테스트 (로컬)

### 부하 테스트 도구 설치

```bash
pip install locust
```

### 간단한 부하 테스트

```bash
# 헬스체크 엔드포인트 테스트
ab -n 100 -c 10 http://localhost:5000/health
```

---

## 🎯 다음 단계

로컬 테스트가 완료되면:

1. ✅ 코드 검토 및 수정
2. ✅ Git 커밋 및 푸시
3. ✅ AWS EC2에 배포
4. ✅ 실제 환경에서 AI 기능 테스트

---

## 💡 개발 팁

### 디버그 모드 활성화

```python
# app.py 마지막 줄 수정
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # debug=True
```

**주의**: 프로덕션 환경(EC2)에서는 반드시 `debug=False`로 설정!

### 로그 출력 추가

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 사용 예시
logger.info(f"질문 받음: {question}")
```

---

**로컬 테스트 완료 후 EC2에 배포하여 실제 AI 기능을 테스트하세요!**

건양대학교 AI 부트캠프 6팀
