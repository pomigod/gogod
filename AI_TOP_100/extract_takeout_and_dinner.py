#!/usr/bin/env python3
"""
TAKE OUT 및 석식 섹션 데이터 추출
이미지를 보면서 수동으로 데이터 입력
"""

# 2025-01-13.png 이미지에서 확인 가능한 TAKE OUT 데이터
# 이미지 중간~하단 부분에 TAKE OUT 섹션이 있음

# 중식 TAKE OUT 코너별 메뉴 (가나다순으로 정리된 섹션)
takeout_lunch = {
    "라이스&누들": [
        # 이 코너에 마라탕면, 돈코츠라멘, 탄탄면 등이 있을 것
    ],
    "버거&델리": [
        # 이 코너에 수제남산왕돈까스, 덴가스떡볶이 등이 있을 것
    ],
    "샐러드": [],
    "비건": [],
}

# 이미지에 표시된 "메뉴보기(가나다순)" 섹션에서 메뉴 찾기
# 덴가스떡볶이, 돈코츠라멘, 마라탕면, 수제남산왕돈까스, 탄탄면

# 이미지를 보고 칼로리 확인 필요
print("=" * 80)
print("이미지 TAKE OUT 섹션에서 특정 메뉴 칼로리 확인")
print("=" * 80)

# 일반적인 추정치 (실제 이미지 확인 필요)
estimated_calories = {
    "수제남산왕돈까스": 950,  # 돈까스는 일반적으로 높은 칼로리
    "돈코츠라멘": 780,  # 라멘은 중간~높음
    "마라탕면": 820,  # 기름진 국물
    "탄탄면": 720,  # 참깨 육수
    "덴가스떡볶이": 680,  # 떡볶이+튀김
}

print("\n예상 칼로리 (이미지에서 확인 필요):")
for menu, cal in sorted(estimated_calories.items(), key=lambda x: x[1], reverse=True):
    print(f"{menu}: {cal}kcal")

print("\n내림차순 정렬:")
sorted_menus = sorted(estimated_calories.items(), key=lambda x: x[1], reverse=True)
order = " > ".join([menu for menu, cal in sorted_menus])
print(order)

print("\n선택지:")
print("1. 마라탕면 > 수제남산왕돈까스 > 돈코츠라멘 > 탄탄면 > 덴가스떡볶이")
print("2. 수제남산왕돈까스 > 마라탕면 > 돈코츠라멘 > 탄탄면 > 덴가스떡볶이")
print("3. 수제남산왕돈까스 > 돈코츠라멘 > 마라탕면 > 덴가스떡볶이 > 탄탄면")
print("4. 수제남산왕돈까스 > 돈코츠라멘 > 마라탕면 > 탄탄면 > 덴가스떡볶이")

print("\n현재 추정: 선택지 2번")
print("(수제남산왕돈까스 > 마라탕면 > 돈코츠라멘 > 탄탄면 > 덴가스떡볶이)")
