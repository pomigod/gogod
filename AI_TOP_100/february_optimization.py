#!/usr/bin/env python3
"""
문제 1-5: 2월 식단 최적화
2월 한 달간 칼로리 기준으로 최적 조합 찾기
"""

import json
from itertools import product

# 2월 데이터 (이미지에서 추출 필요)
# 2025-02-03.png: 2/3-2/7
# 2025-02-10.png: 2/10-2/14
# 2025-02-17.png: 2/17-2/21
# 2025-02-24.png: 2/24-2/28

# 각 날짜의 코너별 칼로리 데이터
# 코너: 한식A, 한식B, 양식, 팝업A, 팝업B, 샐러드, 비건, 라이스&누들, 버거&델리

february_data = {
    # 2/3 주 (월-금)
    "2025-02-03": {  # 월
        "중식": {
            "한식A": 731, "한식B": 715, "양식": 679, "팝업A": None, "팝업B": None,
            "샐러드": None, "비건": None, "라이스&누들": None, "버거&델리": None,
        },
        "석식": {
            "한식A": None, "한식B": None, "양식": None, "팝업A": None, "팝업B": None,
            "샐러드": None, "비건": None, "라이스&누들": None, "버거&델리": None,
        },
    },
    # ... 2월의 모든 날짜 데이터 필요
}

def find_optimal_combination(lunch_cals, dinner_cals, target=1550):
    """
    중식과 석식의 최적 조합 찾기
    target 칼로리에 가장 근접한 조합 반환
    """
    best_combo = None
    best_diff = float('inf')

    for lunch_corner, lunch_cal in lunch_cals.items():
        if lunch_cal is None:
            continue
        for dinner_corner, dinner_cal in dinner_cals.items():
            if dinner_cal is None:
                continue
            total = lunch_cal + dinner_cal
            diff = abs(total - target)
            if diff < best_diff:
                best_diff = diff
                best_combo = {
                    "lunch": lunch_corner,
                    "dinner": dinner_corner,
                    "total": total,
                    "diff": diff
                }

    return best_combo

def find_lowest_lunch(lunch_cals):
    """가장 낮은 칼로리의 중식 코너 찾기"""
    valid_corners = {k: v for k, v in lunch_cals.items() if v is not None}
    if not valid_corners:
        return None
    return min(valid_corners.items(), key=lambda x: x[1])

# 예제 계산
print("=" * 80)
print("문제 1-5: 2월 식단 최적화")
print("=" * 80)
print("\n2월 전체 데이터 수집이 필요합니다.")
print("각 날짜마다:")
print("- 월~목: 중식 + 석식 = 1550kcal에 가장 근접한 조합")
print("- 금: 가장 낮은 칼로리의 중식 코너")
print("\n" + "=" * 80)
print("답안 형식:")
print("""
[
  {"date": "2025-02-03", "lunch": "한식B", "dinner": "샐러드"},
  {"date": "2025-02-04", "lunch": "비건", "dinner": "한식A"},
  ...
  {"date": "2025-02-28", "lunch": "팝업A"}
]
""")
print("=" * 80)
