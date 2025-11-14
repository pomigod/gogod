#!/usr/bin/env python3
"""
AI 학습 도우미 - 건양대 6팀
AWS Bedrock을 활용한 학교 학습 지원 서비스
"""

from flask import Flask, render_template, request, jsonify
import boto3
import json
import os

app = Flask(__name__)

# AWS Bedrock 클라이언트 설정
def get_bedrock_client():
    """AWS Bedrock 클라이언트 생성"""
    try:
        # 리전 설정 (환경 변수로 변경 가능)
        # Bedrock 사용 가능 리전: us-east-1(버지니아 북부), us-east-2(오하이오), us-west-2(오레곤)
        region = os.environ.get('AWS_REGION', 'us-east-2')  # 기본값: 오하이오

        # EC2에서 IAM Role을 통해 자동으로 인증됩니다
        bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region
        )
        return bedrock
    except Exception as e:
        print(f"Bedrock 클라이언트 생성 실패: {e}")
        return None

def ask_ai(question):
    """AI에게 질문하고 답변 받기"""

    # 로컬 테스트 모드 확인
    if os.environ.get('LOCAL_TEST_MODE') == 'true':
        return f"""[로컬 테스트 모드]

질문: {question}

안녕하세요! 현재 로컬 환경에서 실행 중이라 실제 AI 답변은 제공되지 않습니다.

✅ 웹 인터페이스는 정상 작동합니다!
❌ AI 기능은 AWS EC2 배포 후 사용 가능합니다.

AWS EC2에 배포하시면:
- 실제 Claude AI가 질문에 답변합니다
- 학습에 필요한 모든 내용을 물어볼 수 있습니다
- 24시간 언제든 사용 가능합니다

배포 가이드: STEP_BY_STEP_GUIDE.md 파일을 참조하세요!"""

    try:
        bedrock = get_bedrock_client()
        if not bedrock:
            return "AI 서비스에 연결할 수 없습니다."

        # Claude 모델에 질문
        prompt = f"""당신은 학교 학습을 돕는 친절한 AI 선생님입니다.
학생의 질문에 명확하고 이해하기 쉽게 답변해주세요.

학생 질문: {question}

답변:"""

        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })

        response = bedrock.invoke_model(
            modelId='anthropic.claude-3-haiku-20240307-v1:0',
            body=body
        )

        response_body = json.loads(response['body'].read())
        answer = response_body['content'][0]['text']
        return answer

    except Exception as e:
        print(f"AI 질문 처리 실패: {e}")
        return f"죄송합니다. 오류가 발생했습니다: {str(e)}"

@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    """AI 질문 API"""
    try:
        data = request.get_json()
        question = data.get('question', '')

        if not question:
            return jsonify({'error': '질문을 입력해주세요'}), 400

        answer = ask_ai(question)
        return jsonify({'answer': answer})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """헬스체크 엔드포인트"""
    return jsonify({'status': 'healthy', 'service': 'AI 학습 도우미'})

if __name__ == '__main__':
    # 모든 IP에서 접근 가능하도록 설정
    app.run(host='0.0.0.0', port=5000, debug=False)
