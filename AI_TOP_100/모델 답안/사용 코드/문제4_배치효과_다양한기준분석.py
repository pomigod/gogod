#!/usr/bin/env python3
"""
문제 4-2 배치 효과 재검증
다양한 기준으로 전방/후방 정의하여 재계산
"""

import json
from collections import defaultdict

with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

print("="*80)
print("문제 4-2: 배치 효과 다양한 기준으로 재검증")
print("="*80)

# 방법 1: 절대 y 좌표 기준 (y < 11 = 전방)
print("\n[방법 1] 절대 y 좌표 기준 (y < 11 = 전방)")
position_stats_v1 = defaultdict(lambda: {
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

            is_front = y < 11

            if is_front:
                position_stats_v1[unit_type]['front_total'] += 1
                if won:
                    position_stats_v1[unit_type]['front_wins'] += 1
            else:
                position_stats_v1[unit_type]['back_total'] += 1
                if won:
                    position_stats_v1[unit_type]['back_wins'] += 1

diffs_v1 = {}
for unit, stats in position_stats_v1.items():
    if stats['front_total'] > 0 and stats['back_total'] > 0:
        front_wr = (stats['front_wins'] / stats['front_total']) * 100
        back_wr = (stats['back_wins'] / stats['back_total']) * 100
        diffs_v1[unit] = abs(front_wr - back_wr)
        print(f"{unit}: 전방 {front_wr:.2f}% vs 후방 {back_wr:.2f}% = 차이 {diffs_v1[unit]:.2f}%p")

sorted_v1 = sorted(diffs_v1.items(), key=lambda x: x[1], reverse=True)
print(f"최대 차이: {sorted_v1[0][0]} ({sorted_v1[0][1]:.2f}%p)")

# 방법 2: 팀 내 상대적 위치 (팀의 평균 y보다 작으면 전방)
print("\n[방법 2] 팀 내 상대적 위치 기준")
position_stats_v2 = defaultdict(lambda: {
    'front_wins': 0, 'front_total': 0,
    'back_wins': 0, 'back_total': 0
})

for battle in battles:
    for team_name in ['blue', 'red']:
        team = battle[team_name]
        if len(team) <= 1:
            continue

        won = battle['winner'] == team_name

        # 팀의 평균 y 좌표 계산
        ys = [int(u['at'].split(',')[1]) for u in team]
        avg_y = sum(ys) / len(ys)

        for unit in team:
            pos = unit['at'].split(',')
            y = int(pos[1])
            unit_type = unit['type']

            is_front = y < avg_y

            if is_front:
                position_stats_v2[unit_type]['front_total'] += 1
                if won:
                    position_stats_v2[unit_type]['front_wins'] += 1
            else:
                position_stats_v2[unit_type]['back_total'] += 1
                if won:
                    position_stats_v2[unit_type]['back_wins'] += 1

diffs_v2 = {}
for unit, stats in position_stats_v2.items():
    if stats['front_total'] > 0 and stats['back_total'] > 0:
        front_wr = (stats['front_wins'] / stats['front_total']) * 100
        back_wr = (stats['back_wins'] / stats['back_total']) * 100
        diffs_v2[unit] = abs(front_wr - back_wr)
        print(f"{unit}: 전방 {front_wr:.2f}% vs 후방 {back_wr:.2f}% = 차이 {diffs_v2[unit]:.2f}%p")

sorted_v2 = sorted(diffs_v2.items(), key=lambda x: x[1], reverse=True)
print(f"최대 차이: {sorted_v2[0][0]} ({sorted_v2[0][1]:.2f}%p)")

# 방법 3: x 좌표 기준 (x < 11 = 전방, 전투가 좌우로 진행된다면)
print("\n[방법 3] x 좌표 기준 (x < 11 = 전방)")
position_stats_v3 = defaultdict(lambda: {
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
            x = int(pos[0])
            unit_type = unit['type']

            is_front = x < 11

            if is_front:
                position_stats_v3[unit_type]['front_total'] += 1
                if won:
                    position_stats_v3[unit_type]['front_wins'] += 1
            else:
                position_stats_v3[unit_type]['back_total'] += 1
                if won:
                    position_stats_v3[unit_type]['back_wins'] += 1

diffs_v3 = {}
for unit, stats in position_stats_v3.items():
    if stats['front_total'] > 0 and stats['back_total'] > 0:
        front_wr = (stats['front_wins'] / stats['front_total']) * 100
        back_wr = (stats['back_wins'] / stats['back_total']) * 100
        diffs_v3[unit] = abs(front_wr - back_wr)
        print(f"{unit}: 전방 {front_wr:.2f}% vs 후방 {back_wr:.2f}% = 차이 {diffs_v3[unit]:.2f}%p")

sorted_v3 = sorted(diffs_v3.items(), key=lambda x: x[1], reverse=True)
print(f"최대 차이: {sorted_v3[0][0]} ({sorted_v3[0][1]:.2f}%p)")

print("\n" + "="*80)
print("결론:")
print(f"방법 1 (절대 y): {sorted_v1[0][0]}")
print(f"방법 2 (상대 y): {sorted_v2[0][0]}")
print(f"방법 3 (절대 x): {sorted_v3[0][0]}")
print(f"\nGemini 답안: eyanoo")
print(f"내 답안: eyanoo")
print("="*80)
