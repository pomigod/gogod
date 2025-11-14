#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
문제 4: 전투 시뮬레이션 완전 분석
4-4: 상성 관계
4-5: 데이터 내용 확인
4-6: 전투 결과 예측
"""

import json
from collections import Counter, defaultdict

# 데이터 로드
print("데이터 로딩 중...")
with open("ai_top_100_modeling 4번/train_battles.json", "r") as f:
    train_data = json.load(f)

with open("ai_top_100_modeling 4번/test_battles.json", "r") as f:
    test_data = json.load(f)

print(f"훈련 데이터: {len(train_data)}개")
print(f"테스트 데이터: {len(test_data)}개")
print()

# ============================================================================
# 문제 4-4: 상성 관계 (옳지 않은 것 찾기)
# ============================================================================

def analyze_matchups():
    """유닛 간 상성 관계 분석"""
    print("=" * 60)
    print("문제 4-4: 상성 관계")
    print("=" * 60)

    # 1v1 전투에서 상성 분석
    matchup_stats = defaultdict(lambda: {"wins": 0, "total": 0})

    one_v_one = [b for b in train_data if len(b["blue"]) == 1 and len(b["red"]) == 1]

    for battle in one_v_one:
        blue_type = battle["blue"][0]["type"]
        red_type = battle["red"][0]["type"]
        winner = battle["winner"]

        # A vs B 매치업
        matchup_key = f"{blue_type} vs {red_type}"
        matchup_stats[matchup_key]["total"] += 1
        if winner == "blue":
            matchup_stats[matchup_key]["wins"] += 1

        # B vs A 매치업 (반대)
        reverse_key = f"{red_type} vs {blue_type}"
        matchup_stats[reverse_key]["total"] += 1
        if winner == "red":
            matchup_stats[reverse_key]["wins"] += 1

    # 상성 판단 (A > B: A의 승률이 50% 이상)
    matchups = {}
    unit_types = ["eyanoo", "dgreg", "aleo", "bras", "cbene"]

    print()
    print("상성 관계 분석:")
    for unit_a in unit_types:
        for unit_b in unit_types:
            if unit_a != unit_b:
                key = f"{unit_a} vs {unit_b}"
                if key in matchup_stats and matchup_stats[key]["total"] > 0:
                    win_rate = matchup_stats[key]["wins"] / matchup_stats[key]["total"] * 100
                    matchups[key] = win_rate

                    if win_rate > 50:
                        print(f"  {unit_a} > {unit_b}: {win_rate:.1f}% ({matchup_stats[key]['wins']}/{matchup_stats[key]['total']})")

    print()

    # 선택지 확인
    options = [
        "cbene > aleo",
        "eyanoo > dgreg",
        "dgreg > aleo",
        "bras > cbene",
        "aleo > eyanoo",
        "eyanoo > bras",
        "bras > dgreg",
        "cbene > eyanoo",
        "aleo > bras",
        "dgreg > cbene"
    ]

    print("선택지 확인 (옳지 않은 것):")
    wrong_options = []
    for opt in options:
        unit_a, unit_b = opt.split(" > ")
        key = f"{unit_a} vs {unit_b}"
        if key in matchups:
            win_rate = matchups[key]
            is_correct = win_rate > 50
            status = "✓" if is_correct else "✗ (옳지 않음)"
            print(f"  {opt}: {win_rate:.1f}% {status}")
            if not is_correct:
                wrong_options.append(opt)
        else:
            print(f"  {opt}: 데이터 없음")

    print()
    print(f"옳지 않은 상성: {wrong_options}")
    print()

# ============================================================================
# 문제 4-5: 데이터 내용 확인 (올바르지 않은 것 찾기)
# ============================================================================

def verify_statements():
    """데이터 내용 확인 문제"""
    print("=" * 60)
    print("문제 4-5: 데이터 내용 확인")
    print("=" * 60)

    # 선택지:
    # 1. 팀의 중심이 좌표의 중심(10.5, 10.5)에 가까울 수록 승률이 높다.
    # 2. 같은 팀 유닛 간 거리가 가까울 수록 승률이 높아지는 경향을 보인다.
    # 3. dgreg는 전방에 위치할 때가 후방에 위치할 때보다 승률이 높다.
    # 4. 4대4 전투에서, aleo+bras+dgreg+eyanoo 조합의 승률은 60% 이상이다.
    # 5. 2대2 전투에서 aleo+dgreg 조합은 bras+eyanoo 조합에게 26전 25승을 기록했다.

    print()
    print("각 선택지 검증:")
    print()

    # TODO: 각 선택지를 데이터로 검증
    print("(상세 검증 필요)")
    print()

# ============================================================================
# 문제 4-6: 전투 결과 예측
# ============================================================================

def predict_battles():
    """test_battles.json의 승자 예측"""
    print("=" * 60)
    print("문제 4-6: 전투 결과 예측")
    print("=" * 60)

    # 간단한 휴리스틱 기반 예측
    # 1v1의 경우 상성 이용
    # 다대다의 경우 유닛 타입별 강도 합산

    unit_strength = {
        "dgreg": 5,
        "cbene": 4,
        "aleo": 3,
        "bras": 2,
        "eyanoo": 1
    }

    predictions = []

    for battle in test_data:
        blue_strength = sum(unit_strength.get(u["type"], 0) for u in battle["blue"])
        red_strength = sum(unit_strength.get(u["type"], 0) for u in battle["red"])

        winner = "blue" if blue_strength >= red_strength else "red"
        predictions.append(winner)

    print()
    print(f"예측 완료: {len(predictions)}개 전투")
    print(f"첫 10개 예측: {predictions[:10]}")
    print()

    # JSON 형식으로 저장
    output = predictions
    output_file = "ai_top_100_modeling 4번/predictions.json"

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"예측 결과 저장: {output_file}")
    print()

# ============================================================================
# 메인 실행
# ============================================================================

if __name__ == "__main__":
    analyze_matchups()
    # verify_statements()  # 추가 분석 필요
    predict_battles()
