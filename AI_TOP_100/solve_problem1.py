#!/usr/bin/env python3
"""
AI_TOP_100 문제 1번: 춘식도락 메뉴 분석 챌린지
Claude Code 독립 솔루션
"""

import re
from collections import defaultdict, Counter
import json

# 1월 13일 주간 (1/13-1/17) 중식 메뉴 데이터
# 이미지를 보고 정확하게 추출 (한식A, 한식B, 양식, 팝업A, 팝업B의 중식 반찬만)
jan13_17_lunch = {
    "월요일": {
        "한식A": ["들기름김치청경채볶음", "주꾸미야채볶음", "배추김치", "총각김치"],
        "한식B": ["제육채소볶음", "애호박볶음", "배추김치", "오이무침"],
        "양식": ["토마토리소스치킨파이야기", "깻잎장아찌", "양파절임", "토마토소스"],
        "팝업A": ["제육굴소스볶음", "상추겉절이", "깍두기", "배추김치"],
        "팝업B": ["매콤제육야채볶음", "시래기무침", "배추김치", "깍두기"],
    },
    "화요일": {
        "한식A": ["꽃빵바지락조개탕", "메추리알곤약조림", "어묵볶음", "배추김치"],
        "한식B": ["서울식순두부찌개", "가자미구이", "연근조림", "배추김치"],
        "양식": ["페퍼로니야끼만두볶음", "피클샐러드", "핫소스", "칠리소스"],
        "팝업A": ["달콤닭갈비구이", "수제치킨너겟", "배추김치", "깍두기"],
        "팝업B": ["비엔나감자볶음", "숙주나물", "무생채", "배추김치"],
    },
    "수요일": {
        "한식A": ["수제비장칼국수", "숙주미나리무침", "자반고등어구이", "배추김치"],
        "한식B": ["얼갈이된장국", "베이컨야채볶음", "계란후라이", "배추김치"],
        "양식": ["치즈불닭볶음면", "단무지채무침", "양파절임", "할라피뇨"],
        "팝업A": ["닭다리야채조림", "가지볶음", "배추김치", "깍두기"],
        "팝업B": ["새송이버섯불고기", "두부조림", "배추김치", "깍두기"],
    },
    "목요일": {
        "한식A": ["경상식소고기무국", "땡초베이컨볶음", "진미채무침", "배추김치"],
        "한식B": ["콩나물국", "동태전", "가지무침", "배추김치"],
        "양식": ["야채토마토커리덮밥", "단무지무침", "양파절임", "칠리소스"],
        "팝업A": ["수제상하이교자", "새콤무침", "배추김치", "깍두기"],
        "팝업B": ["떡볶이주꾸미볶음소스", "진미채부추무침", "배추김치", "깍두기"],
    },
    "금요일": {
        "한식A": ["떡라볶이국수구이", "햄콩나물볶음", "시금치무침", "배추김치"],
        "한식B": ["콩나물국", "생선가스", "공미채무침", "배추김치"],
        "양식": ["토스트카나페구이", "나폴리파스타샐러드", "버터파인애플", "허니머스타드"],
        "팝업A": ["고기잡채", "계란후라이", "배추김치", "깍두기"],
        "팝업B": ["덴까스카레라이스", "콜슬로샐러드", "단무지", "깍두기"],
    }
}

def count_cooking_methods_1_1():
    """문제 1-1: 1/13-1/17 중식 조리법별 메뉴 분석"""
    counts = {"조림": 0, "볶음": 0, "무침": 0, "구이": 0}

    dishes_by_method = {"조림": [], "볶음": [], "무침": [], "구이": []}

    for day, corners in jan13_17_lunch.items():
        for corner_name in ["한식A", "한식B", "양식", "팝업A", "팝업B"]:
            dishes = corners[corner_name]
            for dish in dishes:
                if dish.endswith("조림"):
                    counts["조림"] += 1
                    dishes_by_method["조림"].append(f"{day}-{corner_name}: {dish}")
                elif dish.endswith("볶음"):
                    counts["볶음"] += 1
                    dishes_by_method["볶음"].append(f"{day}-{corner_name}: {dish}")
                elif dish.endswith("무침"):
                    counts["무침"] += 1
                    dishes_by_method["무침"].append(f"{day}-{corner_name}: {dish}")
                elif dish.endswith("구이"):
                    counts["구이"] += 1
                    dishes_by_method["구이"].append(f"{day}-{corner_name}: {dish}")

    return counts, dishes_by_method

def analyze_january_calories():
    """문제 1-2: 1월 전체 중식 평균 칼로리 분석"""
    # 1월 전체 메뉴 데이터 필요 (2024-12-30, 2025-01-06, 01-13, 01-20)
    # 칼로리 정보를 이미지에서 추출해야 함
    print("\n[문제 1-2] 1월 칼로리 순위 분석")
    print("※ 이미지에서 칼로리 정보를 추출하여 계산 필요")
    return None

def find_regional_names():
    """문제 1-3: 지역명 추출 (2회 이상 등장)"""
    print("\n[문제 1-3] 지역 특색 메뉴 분석")
    print("※ 1, 2월 전체 메뉴에서 지역명 추출 필요")
    return None

def compare_specific_calories():
    """문제 1-4: 특정 메뉴 칼로리 비교"""
    print("\n[문제 1-4] 메뉴별 칼로리 비교")
    print("※ 덴가스떡볶이, 돈코츠라멘, 마라탕면, 수제남산왕돈까스, 탄탄면")
    return None

def optimize_february_meals():
    """문제 1-5: 2월 식단 최적화"""
    print("\n[문제 1-5] 2월 한 달 식단 최적화 챌린지")
    print("※ 2월 메뉴 전체 분석 후 최적 조합 계산 필요")
    return None

def main():
    print("=" * 70)
    print("AI_TOP_100 문제 1번: 춘식도락 메뉴 분석 챌린지")
    print("=" * 70)

    # 문제 1-1: 조리법별 메뉴 분석
    print("\n[문제 1-1] 조리법별 메뉴 분석 (1/13-1/17 중식)")
    print("-" * 70)
    counts, dishes_by_method = count_cooking_methods_1_1()

    # 내림차순 정렬
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    print("\n조리법별 개수:")
    for method, count in sorted_counts:
        print(f"  {method}: {count}개")
        if count > 0:
            print(f"    예시: {dishes_by_method[method][:3]}")

    result = " > ".join([method for method, count in sorted_counts])
    print(f"\n✓ 답: {result}")

    # 나머지 문제들
    analyze_january_calories()
    find_regional_names()
    compare_specific_calories()
    optimize_february_meals()

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
