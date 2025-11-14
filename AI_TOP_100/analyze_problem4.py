#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
문제 4: 전투 시뮬레이션 분석
train_battles.json 데이터를 분석하여 문제 해결
"""

import json
from collections import Counter, defaultdict
import statistics

# JSON 데이터 로드
print("데이터 로딩 중...")
with open("ai_top_100_modeling 4번/train_battles.json", "r") as f:
    train_data = json.load(f)

print(f"훈련 데이터: {len(train_data)}개 전투")
print()

# ============================================================================
# 문제 4-1: 1v1 최강자
# ============================================================================

def analyze_1v1_battles():
    """1대1 전투에서 각 유닛의 승률 분석"""
    print("=" * 60)
    print("문제 4-1: 1v1 최강자")
    print("=" * 60)

    # 1v1 전투만 필터링
    one_v_one = [b for b in train_data if len(b["blue"]) == 1 and len(b["red"]) == 1]
    print(f"1v1 전투: {len(one_v_one)}개")

    # 각 유닛 타입별 승/패 카운트
    unit_stats = defaultdict(lambda: {"wins": 0, "total": 0})

    for battle in one_v_one:
        blue_type = battle["blue"][0]["type"]
        red_type = battle["red"][0]["type"]
        winner = battle["winner"]

        # blue 유닛 처리
        unit_stats[blue_type]["total"] += 1
        if winner == "blue":
            unit_stats[blue_type]["wins"] += 1

        # red 유닛 처리
        unit_stats[red_type]["total"] += 1
        if winner == "red":
            unit_stats[red_type]["wins"] += 1

    # 승률 계산 및 정렬
    win_rates = {}
    for unit_type, stats in unit_stats.items():
        win_rate = stats["wins"] / stats["total"] * 100
        win_rates[unit_type] = win_rate

    sorted_units = sorted(win_rates.items(), key=lambda x: x[1], reverse=True)

    print()
    print("유닛별 1v1 승률:")
    for unit, rate in sorted_units:
        print(f"  {unit}: {rate:.2f}% ({unit_stats[unit]['wins']}/{unit_stats[unit]['total']})")

    print()
    print(f"답: {sorted_units[0][0]}")
    print()

    return sorted_units[0][0]

# ============================================================================
# 문제 4-2: 배치 효과
# ============================================================================

def analyze_position_effect():
    """전방/후방 배치에 따른 승률 차이 분석"""
    print("=" * 60)
    print("문제 4-2: 배치 효과")
    print("=" * 60)

    # 전방: y 좌표가 작을 때 (적에게 가까움)
    # 후방: y 좌표가 클 때 (적에게 멀리)

    # 각 유닛 타입별로 전방/후방 승률 계산
    unit_position_stats = defaultdict(lambda: {
        "front": {"wins": 0, "total": 0},
        "back": {"wins": 0, "total": 0}
    })

    for battle in train_data:
        # blue 팀 분석 (y 좌표 기준)
        for unit in battle["blue"]:
            y = int(unit["at"].split(",")[1])
            unit_type = unit["type"]

            # 중앙(10.5) 기준 전방/후방 판단
            position = "front" if y < 10.5 else "back"

            unit_position_stats[unit_type][position]["total"] += 1
            if battle["winner"] == "blue":
                unit_position_stats[unit_type][position]["wins"] += 1

        # red 팀 분석 (y 좌표 반대로)
        for unit in battle["red"]:
            y = int(unit["at"].split(",")[1])
            unit_type = unit["type"]

            # red는 반대로
            position = "back" if y < 10.5 else "front"

            unit_position_stats[unit_type][position]["total"] += 1
            if battle["winner"] == "red":
                unit_position_stats[unit_type][position]["wins"] += 1

    # 전방/후방 승률 차이 계산
    position_diffs = {}
    print()
    print("유닛별 전방/후방 승률 차이:")

    for unit_type, stats in unit_position_stats.items():
        front_rate = 0
        back_rate = 0

        if stats["front"]["total"] > 0:
            front_rate = stats["front"]["wins"] / stats["front"]["total"] * 100

        if stats["back"]["total"] > 0:
            back_rate = stats["back"]["wins"] / stats["back"]["total"] * 100

        diff = abs(front_rate - back_rate)
        position_diffs[unit_type] = diff

        print(f"  {unit_type}: 전방 {front_rate:.2f}%, 후방 {back_rate:.2f}%, 차이 {diff:.2f}%")

    sorted_diffs = sorted(position_diffs.items(), key=lambda x: x[1], reverse=True)

    print()
    print(f"답: {sorted_diffs[0][0]}")
    print()

    return sorted_diffs[0][0]

# ============================================================================
# 문제 4-3: 진형 우세
# ============================================================================

def analyze_formation():
    """x 방향 vs y 방향 진형 승률 분석"""
    print("=" * 60)
    print("문제 4-3: 진형 우세")
    print("=" * 60)

    x_wide_wins = 0
    y_wide_wins = 0
    x_wide_total = 0
    y_wide_total = 0

    for battle in train_data:
        # blue 팀 진형 분석
        if len(battle["blue"]) > 1:
            blue_coords = [unit["at"].split(",") for unit in battle["blue"]]
            blue_x = [int(c[0]) for c in blue_coords]
            blue_y = [int(c[1]) for c in blue_coords]

            x_range = max(blue_x) - min(blue_x)
            y_range = max(blue_y) - min(blue_y)

            if x_range > y_range:  # x 방향으로 긴 진형
                x_wide_total += 1
                if battle["winner"] == "blue":
                    x_wide_wins += 1
            elif y_range > x_range:  # y 방향으로 긴 진형
                y_wide_total += 1
                if battle["winner"] == "blue":
                    y_wide_wins += 1

        # red 팀 진형 분석
        if len(battle["red"]) > 1:
            red_coords = [unit["at"].split(",") for unit in battle["red"]]
            red_x = [int(c[0]) for c in red_coords]
            red_y = [int(c[1]) for c in red_coords]

            x_range = max(red_x) - min(red_x)
            y_range = max(red_y) - min(red_y)

            if x_range > y_range:  # x 방향으로 긴 진형
                x_wide_total += 1
                if battle["winner"] == "red":
                    x_wide_wins += 1
            elif y_range > x_range:  # y 방향으로 긴 진형
                y_wide_total += 1
                if battle["winner"] == "red":
                    y_wide_wins += 1

    x_wide_rate = x_wide_wins / x_wide_total * 100 if x_wide_total > 0 else 0
    y_wide_rate = y_wide_wins / y_wide_total * 100 if y_wide_total > 0 else 0

    print()
    print(f"x 방향 진형: {x_wide_rate:.2f}% ({x_wide_wins}/{x_wide_total})")
    print(f"y 방향 진형: {y_wide_rate:.2f}% ({y_wide_wins}/{y_wide_total})")
    print()

    answer = "x 방향으로 긴 진형" if x_wide_rate > y_wide_rate else "y 방향으로 긴 진형"
    print(f"답: {answer}")
    print()

    return answer

# ============================================================================
# 메인 실행
# ============================================================================

if __name__ == "__main__":
    analyze_1v1_battles()
    analyze_position_effect()
    analyze_formation()

    print("=" * 60)
    print("문제 4-4, 4-5, 4-6은 추가 분석 필요")
    print("=" * 60)
