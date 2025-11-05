#!/usr/bin/env python3
"""
전장 배치 분석: blue/red 팀의 일반적인 배치 위치 파악
"""

import json

with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

# 처음 20개 전투의 배치 분석
print("전장 배치 패턴 분석 (첫 20개 전투)")
print("="*80)

for i, battle in enumerate(battles[:20]):
    print(f"\n전투 {i+1}: {battle['id']}")
    print(f"승자: {battle['winner']}")

    print("Blue 팀:")
    for unit in battle['blue']:
        pos = unit['at'].split(',')
        print(f"  {unit['type']}: x={pos[0]}, y={pos[1]}")

    print("Red 팀:")
    for unit in battle['red']:
        pos = unit['at'].split(',')
        print(f"  {unit['type']}: x={pos[0]}, y={pos[1]}")

# 전체 좌표 범위 분석
print("\n" + "="*80)
print("전체 좌표 범위 분석")

all_xs = []
all_ys = []
blue_xs = []
blue_ys = []
red_xs = []
red_ys = []

for battle in battles:
    for unit in battle['blue']:
        pos = unit['at'].split(',')
        x, y = int(pos[0]), int(pos[1])
        all_xs.append(x)
        all_ys.append(y)
        blue_xs.append(x)
        blue_ys.append(y)

    for unit in battle['red']:
        pos = unit['at'].split(',')
        x, y = int(pos[0]), int(pos[1])
        all_xs.append(x)
        all_ys.append(y)
        red_xs.append(x)
        red_ys.append(y)

print(f"\n전체 좌표 범위:")
print(f"  x: {min(all_xs)} ~ {max(all_xs)}")
print(f"  y: {min(all_ys)} ~ {max(all_ys)}")

print(f"\nBlue 팀 평균 위치:")
print(f"  x: {sum(blue_xs)/len(blue_xs):.2f}")
print(f"  y: {sum(blue_ys)/len(blue_ys):.2f}")

print(f"\nRed 팀 평균 위치:")
print(f"  x: {sum(red_xs)/len(red_xs):.2f}")
print(f"  y: {sum(red_ys)/len(red_ys):.2f}")

# x 좌표 기준으로 Blue가 왼쪽, Red가 오른쪽인지 확인
print(f"\n결론:")
if sum(blue_xs)/len(blue_xs) < sum(red_xs)/len(red_xs):
    print("Blue 팀이 왼쪽(x 작음), Red 팀이 오른쪽(x 큼)")
    print("→ 전방/후방은 x축 기준일 가능성이 높음")
    print("→ x < 11: 전방 (Blue에 가까움)")
    print("→ x >= 11: 후방 (Red에 가까움)")
else:
    print("x축 기준으로 명확한 패턴 없음")
    print("→ 전방/후방은 y축 기준일 가능성")
