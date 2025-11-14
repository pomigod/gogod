#!/bin/bash
# 문제 4 답안을 텍스트 뷰어로 여는 스크립트

# 결과 파일 경로
ANSWER_FILE="/home/user/gogod/problem4_answers.txt"

# 파일이 존재하는지 확인
if [ ! -f "$ANSWER_FILE" ]; then
    echo "Error: 답안 파일을 찾을 수 없습니다."
    exit 1
fi

# 화면에 출력
cat "$ANSWER_FILE"

echo ""
echo "=========================================="
echo "상세 분석 문서: CLAUDE_CODE_ANSWERS.md"
echo "예측 결과: battle_predictions.json"
echo "=========================================="
