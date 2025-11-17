#!/usr/bin/env python3
"""
문제 1-3: 지역 특색 메뉴 (2회 이상 등장)
1, 2월의 모든 메뉴명에서 지역명 추출
"""

from collections import Counter
import re

# 이미지에서 확인한 메뉴명 (샘플)
# 실제로는 모든 이미지의 모든 메뉴를 확인해야 함

menus = [
    # 2025-01-13.png에서 확인한 메뉴들
    "춘천닭갈비제육볶음",
    "베트남쌀국수(후로온누들)",
    "베트남롤",
    "일본식커리닭고기덮밥",
    "반미샌드위치",  # 베트남
    "알리오올리오파스타",  # 이탈리아
    "일본식카츠카레",
    "멕시칸치킨덮밥",
    "토스카나식함박스테이크",
    "홍콩식크리스피치킨",
    "일본소바",
    "멕시코풍매콤한시즌비빔밥",
    # 더 많은 메뉴들...
]

# 찾아야 할 지역명
target_regions = ["베트남", "나가사키", "안동", "태국", "전주"]

# 메뉴명에서 지역명 추출
def extract_regions(menus, regions):
    region_count = Counter()

    for menu in menus:
        for region in regions:
            if region in menu:
                region_count[region] += 1
                print(f"{region} 발견: {menu}")

    return region_count

print("=" * 80)
print("문제 1-3: 지역 특색 메뉴 (2회 이상 등장)")
print("=" * 80)
print("\n현재 수집된 메뉴에서 지역명 검색:")
print("-" * 80)

region_count = extract_regions(menus, target_regions)

print("\n" + "=" * 80)
print("결과:")
for region in target_regions:
    count = region_count.get(region, 0)
    print(f"{region}: {count}회")

print("\n2회 이상 등장한 지역:")
result = [region for region in target_regions if region_count.get(region, 0) >= 2]
print(result if result else "아직 확인 중...")

print("\n" + "=" * 80)
print("주의: 모든 이미지(1월, 2월)의 모든 메뉴를 확인해야 정확한 답을 얻을 수 있습니다")
print("=" * 80)
