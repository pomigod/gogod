from flask import Flask, render_template, request, jsonify, session
import boto3
import json
import re
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'daily-harmony-secret-key-2024'  # 세션 암호화를 위한 비밀키

# AWS Bedrock 클라이언트 설정
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

# 모델 ID (Claude 3.5 Haiku로 업그레이드)
MODEL_ID = "us.anthropic.claude-3-5-haiku-20241022-v1:0"

# 시스템 프롬프트
SYSTEM_PROMPT = """당신은 'Daily Harmony' 수강신청 도우미입니다.
사용자가 수강신청 과목 목록을 입력하면 다음 작업을 수행합니다:

1. 과목명, 요일, 시간을 파싱
2. 시간표 형태로 정리
3. 시간 충돌 여부 확인
4. 최적의 시간표 추천

입력 예시:
- "컴퓨터과학개론 월수 10:00-11:30"
- "자료구조 화목 13:00-14:30"

사용자의 이전 대화 내용을 기억하고 문맥에 맞게 응답하세요.
친절하고 명확하게 답변해주세요."""


def parse_courses(text):
    """과목 정보를 파싱하는 함수"""
    courses = []
    lines = text.strip().split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 간단한 파싱 로직 (예: "컴퓨터과학개론 월수 10:00-11:30")
        parts = line.split()
        if len(parts) >= 3:
            course_name = parts[0]
            days_text = parts[1]
            time_text = ' '.join(parts[2:])

            # 요일 매핑
            day_map = {'월': 'Mon', '화': 'Tue', '수': 'Wed', '목': 'Thu', '금': 'Fri'}
            days = [day_map.get(d, d) for d in days_text if d in day_map]

            courses.append({
                'name': course_name,
                'days': days,
                'time': time_text
            })

    return courses


def generate_timetable(courses):
    """시간표를 생성하는 함수"""
    days_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    timetable = {day: [] for day in days_order}

    for course in courses:
        for day in course['days']:
            if day in timetable:
                timetable[day].append({
                    'name': course['name'],
                    'time': course['time']
                })

    return timetable


def check_conflicts(courses):
    """시간 충돌을 확인하는 함수"""
    conflicts = []

    # 간단한 충돌 검사 로직
    for i, course1 in enumerate(courses):
        for j, course2 in enumerate(courses):
            if i >= j:
                continue

            # 같은 요일이 있는지 확인
            common_days = set(course1['days']) & set(course2['days'])
            if common_days:
                conflicts.append(f"{course1['name']}와 {course2['name']}가 {', '.join(common_days)}에 겹칩니다.")

    return conflicts


@app.route('/')
def index():
    """메인 페이지"""
    # 세션 초기화 (새로운 방문 시)
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    """챗봇 대화 처리"""
    try:
        data = request.json
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({'error': '메시지가 비어있습니다.'}), 400

        # 세션에서 대화 기록 가져오기
        chat_history = session.get('chat_history', [])

        # 사용자 메시지를 기록에 추가
        chat_history.append({
            'role': 'user',
            'content': user_message
        })

        # Claude API에 전송할 메시지 구성
        messages = []
        for msg in chat_history:
            messages.append({
                'role': msg['role'],
                'content': msg['content']
            })

        # AWS Bedrock API 호출
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 2000,
            "system": SYSTEM_PROMPT,
            "messages": messages
        }

        response = bedrock_runtime.invoke_model(
            modelId=MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(request_body)
        )

        # 응답 파싱
        response_body = json.loads(response['body'].read())
        assistant_message = response_body['content'][0]['text']

        # 어시스턴트 응답을 기록에 추가
        chat_history.append({
            'role': 'assistant',
            'content': assistant_message
        })

        # 세션에 대화 기록 저장 (최근 20개만 유지)
        session['chat_history'] = chat_history[-20:]

        return jsonify({
            'response': assistant_message,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        print(f"Error in chat: {str(e)}")
        return jsonify({'error': f'오류가 발생했습니다: {str(e)}'}), 500


@app.route('/clear_history', methods=['POST'])
def clear_history():
    """대화 기록 초기화"""
    session['chat_history'] = []
    return jsonify({'message': '대화 기록이 초기화되었습니다.'})


@app.route('/timetable', methods=['POST'])
def create_timetable():
    """시간표 생성 API"""
    try:
        data = request.json
        courses_text = data.get('courses', '')

        # 과목 파싱
        courses = parse_courses(courses_text)

        # 시간표 생성
        timetable = generate_timetable(courses)

        # 충돌 확인
        conflicts = check_conflicts(courses)

        return jsonify({
            'timetable': timetable,
            'conflicts': conflicts,
            'total_courses': len(courses)
        })

    except Exception as e:
        print(f"Error in timetable: {str(e)}")
        return jsonify({'error': f'시간표 생성 중 오류가 발생했습니다: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
