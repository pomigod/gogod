#!/usr/bin/env python3
"""
문제 1 상세 분석
이미지를 보고 수동으로 입력한 데이터를 기반으로 분석
"""

import json
from collections import defaultdict
import statistics

# 1월 전체 중식 칼로리 데이터 (이미지에서 추출)
# 12/30-1/3, 1/6-1/10, 1/13-1/17, 1/20-1/24

january_lunch_calories = {
    # 12월 30일 주 (12/30-1/3) - 2024-12-30.png
    "12/30-1/3": {
        "한식A": [578, 732, None, 726, 731],  # 월, 화, 수(1/1 휴일), 목, 금
        "한식B": [520, 676, None, 715, 717],
        "양식": [None, 662, None, 669, 645],  # 2025년 표시가 있는 수요일 제외
        "팝업A": [None, None, None, None, None],  # 팝업 정보 확인 필요
        "팝업B": [None, None, None, None, None],
    },
    # 1월 6일 주 (1/6-1/10) - 2025-01-06.png
    "1/6-1/10": {
        "한식A": [731, 715, 745, 878, 876],
        "한식B": [734, 697, 618, 876, 819],
        "양식": [788, 774, 691, 875, 676],
        "팝업A": [None, None, None, None, None],  # 팝업 정보 확인 필요
        "팝업B": [None, None, None, None, None],
    },
    # 1월 13일 주 (1/13-1/17) - 2025-01-13.png
    "1/13-1/17": {
        "한식A": [731, 782, 718, 682, 672],
        "한식B": [678, 726, 661, 680, 632],
        "양식": [718, 695, 796, 701, 616],
        "팝업A": [None, None, None, None, None],  # 이미지에서 확인 필요
        "팝업B": [None, None, None, None, None],
    },
    # 1월 20일 주 (1/20-1/24) - 2025-01-20.png
    "1/20-1/24": {
        "한식A": [632, 508, 720, 679, 701],
        "한식B": [582, 583, 722, 588, 632],
        "양식": [622, 622, 711, 680, 722],
        "팝업A": [None, None, None, None, None],
        "팝업B": [None, None, None, None, None],
    },
}

def calculate_january_average():
    """1월 전체 중식의 코너별 평균 칼로리 계산"""
    print("=" * 80)
    print("문제 1-2: 1월 칼로리 순위 분석")
    print("=" * 80)

    corner_calories = defaultdict(list)

    # 모든 주간 데이터를 수집
    for week, corners in january_lunch_calories.items():
        for corner, calories in corners.items():
            for cal in calories:
                if cal is not None:  # None이 아닌 값만 추가
                    corner_calories[corner].append(cal)

    # 평균 계산
    averages = {}
    for corner, calories in corner_calories.items():
        if calories:
            avg = statistics.mean(calories)
            averages[corner] = avg
            print(f"{corner}: {len(calories)}개 데이터, 평균 {avg:.1f}kcal")

    # 내림차순 정렬
    sorted_corners = sorted(averages.items(), key=lambda x: x[1], reverse=True)

    print("\n결과 (내림차순):")
    result_order = " > ".join([f"{corner}({avg:.1f})" for corner, avg in sorted_corners])
    print(result_order)

    print("\n선택지:")
    print("1. 한식A > 한식B > 양식 > 팝업B > 팝업A")
    print("2. 팝업B > 양식 > 한식A > 한식B > 팝업A")
    print("3. 양식 > 한식A > 팝업B > 한식B > 팝업A")
    print("4. 양식 > 팝업B > 한식A > 한식B > 팝업A")

    answer_order = " > ".join([corner for corner, avg in sorted_corners])
    print(f"\n답안: {answer_order}")

    return answer_order


if __name__ == "__main__":
    answer_1_2 = calculate_january_average()

    print("\n" + "=" * 80)
    print("주의: 팝업A, 팝업B 칼로리 데이터는 이미지에서 추가 확인 필요")
    print("=" * 80)
