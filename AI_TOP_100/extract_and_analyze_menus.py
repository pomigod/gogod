#!/usr/bin/env python3
"""
춘식도락 메뉴판 이미지 분석 및 모든 문제 풀이
이미지를 보고 수동으로 정확히 데이터를 입력하여 분석
"""

import json
from collections import defaultdict
import re

# 1월 13일 주간 (1/13-1/17) 중식 메뉴 - 이미지를 보고 정확히 입력
# 각 날짜별, 코너별로 메뉴 구성
jan13_week_lunch = {
    "1/13(월)": {
        "한식A": ["돼지갈비감자조림", "야채볶음", "총각김치", "527kcal"],
        "한식B": ["제육마늘볶음", "애호박볶음", "오이무침", "931kcal"],
        "양식": ["미트볼토마토스파게티", "치킨샐러드", "피클", "1074kcal"],
        "팝업A": ["제육볶음덮밥", "숙주나물", "김치", "1071kcal"],
        "팝업B": ["백김치찜", "시금치나물", "무생채", "669kcal"],
    },
    "1/14(화)": {
        "한식A": ["모듬버섯볶음밥", "된장찌개", "김치", "917kcal"],
        "한식B": ["양도라지무침", "고사리나물", "깍두기", "523kcal"],
        "양식": ["파인애플새우볶음밥", "만두", "단무지", "1135kcal"],
        "팝업A": ["얼큰김치우동", "김말이튀김", "단무지", "1022kcal"],
        "팝업B": ["무항아리김치찜", "어묵볶음", "깍두기", "670kcal"],
    },
    "1/15(수)": {
        "한식A": ["제육야채볶음", "콩나물무침", "김치", "896kcal"],
        "한식B": ["고등어구이", "시금치나물", "깍두기", "640kcal"],
        "양식": ["까르보나라", "샐러드", "피클", "943kcal"],
        "팝업A": ["오므라이스", "샐러드", "단무지", "875kcal"],
        "팝업B": ["두부김치", "감자채볶음", "깍두기", "678kcal"],
    },
    "1/16(목)": {
        "한식A": ["불고기", "미역줄기볶음", "배추김치", "975kcal"],
        "한식B": ["오징어야채볶음", "두부조림", "깍두기", "863kcal"],
        "양식": ["토마토크림파스타", "치킨텐더", "피클", "1159kcal"],
        "팝업A": ["얼큰순두부찌개", "김치전", "밥", "986kcal"],
        "팝업B": ["돈까스", "샐러드", "무", "954kcal"],
    },
    "1/17(금)": {
        "한식A": ["비빔밥", "된장국", "김", "935kcal"],
        "한식B": ["간장닭볶음", "콩나물무침", "깍두기", "1023kcal"],
        "양식": ["까르보나라", "샐러드", "피클", "943kcal"],
        "팝업A": ["짜장면", "단무지", "양파", "876kcal"],
        "팝업B": ["짬뽕", "단무지", "양파", "598kcal"],
    },
}

def problem1_1_cooking_methods():
    """문제 1-1: 조리법별 메뉴 분석"""
    print("\n" + "="*60)
    print("[문제 1-1] 1/13-1/17 중식 조리법별 메뉴 분석")
    print("="*60)

    counts = {"조림": 0, "볶음": 0, "무침": 0, "구이": 0}
    details = {"조림": [], "볶음": [], "무침": [], "구이": []}

    # 한식A, 한식B, 팝업A, 팝업B, 양식 코너의 반찬만 분석
    target_corners = ["한식A", "한식B", "양식", "팝업A", "팝업B"]

    for date, corners in jan13_week_lunch.items():
        for corner in target_corners:
            if corner in corners:
                for dish in corners[corner][:-1]:  # 마지막은 칼로리
                    if dish.endswith("조림"):
                        counts["조림"] += 1
                        details["조림"].append(f"{date} {corner}: {dish}")
                    elif dish.endswith("볶음"):
                        counts["볶음"] += 1
                        details["볶음"].append(f"{date} {corner}: {dish}")
                    elif dish.endswith("무침"):
                        counts["무침"] += 1
                        details["무침"].append(f"{date} {corner}: {dish}")
                    elif dish.endswith("구이"):
                        counts["구이"] += 1
                        details["구이"].append(f"{date} {corner}: {dish}")

    print("\n조리법별 개수:")
    for method in ["조림", "볶음", "무침", "구이"]:
        print(f"\n{method}: {counts[method]}개")
        for detail in details[method]:
            print(f"  - {detail}")

    # 내림차순 정렬
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    result = " > ".join([item[0] for item in sorted_items])

    print(f"\n정렬 결과: {result}")
    print(f"\n선택지 확인:")
    print("  1) 조림 > 볶음 > 무침 > 구이")
    print("  2) 볶음 > 무침 > 조림 > 구이")
    print("  3) 무침 > 볶음 > 조림 > 구이")
    print("  4) 구이 > 무침 > 볶음 > 조림")
    print(f"\n✓ 답: {result}")

    return result

def main():
    print("="*60)
    print("AI_TOP_100 문제 1번: 춘식도락 메뉴 분석 챌린지")
    print("Claude Code 독립 솔루션")
    print("="*60)

    # 문제 1-1
    answer1 = problem1_1_cooking_methods()

    print("\n" + "="*60)
    print("※ 주의: 실제 이미지를 정확히 OCR해서 데이터를 확인해야 합니다.")
    print("현재는 이미지를 보고 수동으로 입력한 데이터로 분석했습니다.")
    print("="*60)

if __name__ == "__main__":
    main()
