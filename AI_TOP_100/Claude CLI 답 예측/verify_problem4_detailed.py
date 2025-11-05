#!/usr/bin/env python3
"""
문제 4 상세 검증: 전투 데이터 분석
특히 배치 효과(전방/후방 승률 차이)를 정확히 재계산
"""

import json
from collections import defaultdict

# 훈련 데이터 로드
with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

print("="*80)
print("문제 4: 전투 데이터 상세 검증")
print("="*80)

# 4-1. 1v1 승률 재계산
print("\n[4-1] 1v1 최강자 검증")
unit_1v1_stats = defaultdict(lambda: {'wins': 0, 'total': 0})

for battle in battles:
    if len(battle['blue']) == 1 and len(battle['red']) == 1:
        blue_unit = battle['blue'][0]['type']
        red_unit = battle['red'][0]['type']
        winner = battle['winner']

        if winner == 'blue':
            unit_1v1_stats[blue_unit]['wins'] += 1
            unit_1v1_stats[blue_unit]['total'] += 1
            unit_1v1_stats[red_unit]['total'] += 1
        else:
            unit_1v1_stats[red_unit]['wins'] += 1
            unit_1v1_stats[red_unit]['total'] += 1
            unit_1v1_stats[blue_unit]['total'] += 1

winrates_1v1 = {}
for unit, stats in unit_1v1_stats.items():
    if stats['total'] > 0:
        winrates_1v1[unit] = (stats['wins'] / stats['total']) * 100

sorted_1v1 = sorted(winrates_1v1.items(), key=lambda x: x[1], reverse=True)
print("1v1 승률 순위:")
for unit, wr in sorted_1v1:
    print(f"  {unit}: {wr:.2f}%")

print(f"\n최강자: {sorted_1v1[0][0]}")
print(f"내 답안: dgreg")
print(f"결과: {'✓' if sorted_1v1[0][0] == 'dgreg' else '✗'}")

# 4-2. 배치 효과 재계산 (중요!)
print("\n[4-2] 배치 효과 상세 검증")
position_stats = defaultdict(lambda: {
    'front_wins': 0, 'front_total': 0,
    'back_wins': 0, 'back_total': 0
})

for battle in battles:
    for team_name in ['blue', 'red']:
        team = battle[team_name]
        if len(team) == 0:
            continue

        won = battle['winner'] == team_name

        for unit in team:
            pos = unit['at'].split(',')
            y = int(pos[1])
            unit_type = unit['type']

            # 전방/후방 기준: y < 11 = 전방, y >= 11 = 후방
            is_front = y < 11

            if is_front:
                position_stats[unit_type]['front_total'] += 1
                if won:
                    position_stats[unit_type]['front_wins'] += 1
            else:
                position_stats[unit_type]['back_total'] += 1
                if won:
                    position_stats[unit_type]['back_wins'] += 1

print("\n유닛별 전방/후방 승률:")
position_diffs = {}
for unit, stats in position_stats.items():
    f_total = stats['front_total']
    b_total = stats['back_total']

    if f_total == 0 or b_total == 0:
        continue

    front_wr = (stats['front_wins'] / f_total) * 100
    back_wr = (stats['back_wins'] / b_total) * 100
    diff = abs(front_wr - back_wr)

    position_diffs[unit] = diff
    print(f"  {unit}:")
    print(f"    전방: {front_wr:.2f}% ({stats['front_wins']}/{f_total})")
    print(f"    후방: {back_wr:.2f}% ({stats['back_wins']}/{b_total})")
    print(f"    차이: {diff:.2f}%p")

sorted_diffs = sorted(position_diffs.items(), key=lambda x: x[1], reverse=True)
print(f"\n배치 효과 최대: {sorted_diffs[0][0]} ({sorted_diffs[0][1]:.2f}%p)")
print(f"내 답안: eyanoo")
print(f"Gemini 답안: eyanoo")
print(f"결과: {'✓' if sorted_diffs[0][0] == 'eyanoo' else '✗ 재검토 필요'}")

# 4-3. 진형 우세
print("\n[4-3] 진형 우세 검증")
x_form_wins = 0
x_form_total = 0
y_form_wins = 0
y_form_total = 0

for battle in battles:
    for team_name in ['blue', 'red']:
        team = battle[team_name]
        if len(team) < 2:
            continue

        xs = [int(u['at'].split(',')[0]) for u in team]
        ys = [int(u['at'].split(',')[1]) for u in team]

        x_range = max(xs) - min(xs)
        y_range = max(ys) - min(ys)

        won = battle['winner'] == team_name

        if x_range > y_range:
            x_form_total += 1
            if won:
                x_form_wins += 1
        elif y_range > x_range:
            y_form_total += 1
            if won:
                y_form_wins += 1

x_wr = (x_form_wins / x_form_total * 100) if x_form_total > 0 else 0
y_wr = (y_form_wins / y_form_total * 100) if y_form_total > 0 else 0

print(f"x 방향 진형: {x_wr:.2f}% ({x_form_wins}/{x_form_total})")
print(f"y 방향 진형: {y_wr:.2f}% ({y_form_wins}/{y_form_total})")
print(f"\n우세 진형: {'x 방향' if x_wr > y_wr else 'y 방향'}")
print(f"내 답안: x 방향으로 긴 진형")
print(f"결과: {'✓' if x_wr > y_wr else '✗'}")

print("\n"+"="*80)
print("검증 완료!")
print("="*80)
