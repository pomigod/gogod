#!/usr/bin/env python3
"""
문제 4-2 배치 효과 올바른 계산
Blue는 왼쪽, Red는 오른쪽에 배치됨
전방 = 적에게 가까운 쪽
"""

import json
from collections import defaultdict

with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

print("="*80)
print("문제 4-2: 배치 효과 올바른 계산")
print("Blue(왼쪽) vs Red(오른쪽) 구조에서")
print("전방 = 적에게 가까운 쪽 (중간선 10.5 기준)")
print("="*80)

position_stats = defaultdict(lambda: {
    'front_wins': 0, 'front_total': 0,
    'back_wins': 0, 'back_total': 0
})

for battle in battles:
    # Blue 팀: 팀 내 평균 x 계산
    if len(battle['blue']) > 0:
        blue_xs = [int(u['at'].split(',')[0]) for u in battle['blue']]
        blue_avg_x = sum(blue_xs) / len(blue_xs)

        for unit in battle['blue']:
            pos = unit['at'].split(',')
            x = int(pos[0])
            unit_type = unit['type']
            won = battle['winner'] == 'blue'

            # 팀 평균보다 x가 크면 전방 (오른쪽 = 적에 가까움)
            is_front = x > blue_avg_x

            if is_front:
                position_stats[unit_type]['front_total'] += 1
                if won:
                    position_stats[unit_type]['front_wins'] += 1
            elif x < blue_avg_x:  # 같으면 제외
                position_stats[unit_type]['back_total'] += 1
                if won:
                    position_stats[unit_type]['back_wins'] += 1

    # Red 팀: 팀 내 평균 x 계산
    if len(battle['red']) > 0:
        red_xs = [int(u['at'].split(',')[0]) for u in battle['red']]
        red_avg_x = sum(red_xs) / len(red_xs)

        for unit in battle['red']:
            pos = unit['at'].split(',')
            x = int(pos[0])
            unit_type = unit['type']
            won = battle['winner'] == 'red'

            # 팀 평균보다 x가 작으면 전방 (왼쪽 = 적에 가까움)
            is_front = x < red_avg_x

            if is_front:
                position_stats[unit_type]['front_total'] += 1
                if won:
                    position_stats[unit_type]['front_wins'] += 1
            elif x > red_avg_x:  # 같으면 제외
                position_stats[unit_type]['back_total'] += 1
                if won:
                    position_stats[unit_type]['back_wins'] += 1

print("\n유닛별 전방/후방 승률:")
diffs = {}
for unit, stats in sorted(position_stats.items()):
    if stats['front_total'] > 0 and stats['back_total'] > 0:
        front_wr = (stats['front_wins'] / stats['front_total']) * 100
        back_wr = (stats['back_wins'] / stats['back_total']) * 100
        diff = abs(front_wr - back_wr)
        diffs[unit] = diff

        print(f"\n{unit}:")
        print(f"  전방: {front_wr:.2f}% ({stats['front_wins']}/{stats['front_total']})")
        print(f"  후방: {back_wr:.2f}% ({stats['back_wins']}/{stats['back_total']})")
        print(f"  차이: {diff:.2f}%p")

sorted_diffs = sorted(diffs.items(), key=lambda x: x[1], reverse=True)

print("\n" + "="*80)
print("배치 효과 순위:")
for i, (unit, diff) in enumerate(sorted_diffs, 1):
    print(f"{i}. {unit}: {diff:.2f}%p")

if len(sorted_diffs) > 0:
    print("\n최대 배치 효과: " + sorted_diffs[0][0])
else:
    print("\n데이터 없음")
print("Gemini 답안: eyanoo")
print("내 답안: eyanoo")
print(f"결과: {'✓' if sorted_diffs[0][0] == 'eyanoo' else '✗ ' + sorted_diffs[0][0]}")
print("="*80)
