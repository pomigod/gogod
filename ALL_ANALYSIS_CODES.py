"""
================================================================================
AI_TOP_100 문제 4: 전투 시뮬레이션 분석 - 전체 코드 모음
================================================================================
파일 구성:
1. 문제 4-1 ~ 4-4: 1v1 최강자, 배치 효과, 진형, 상성 분석
2. 문제 4-5: 데이터 내용 검증
3. 문제 4-6: 승자 예측 모델
================================================================================
"""

# ============================================================================
# 코드 1: 문제 4-1 ~ 4-4 분석 (analyze_battles_v2.py)
# ============================================================================

import json
from collections import defaultdict

# Load the training data
with open('AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

print(f"Total battles: {len(battles)}")

# Helper function to parse coordinates
def parse_coords(at_str):
    x, y = at_str.split(',')
    return int(x), int(y)

# Get unit types
unit_types = set()
for battle in battles:
    for unit in battle['blue'] + battle['red']:
        unit_types.add(unit['type'])

print(f"Unit types: {sorted(unit_types)}\n")

# ====== Problem 4-1: 1v1 최강자 ======
print("=== Problem 4-1: 1v1 최강자 ===")
one_v_one_battles = [b for b in battles if len(b['blue']) == 1 and len(b['red']) == 1]
print(f"1v1 battles: {len(one_v_one_battles)}")

unit_wins = defaultdict(int)
unit_total = defaultdict(int)

for battle in one_v_one_battles:
    blue_type = battle['blue'][0]['type']
    red_type = battle['red'][0]['type']
    winner = battle['winner']

    unit_total[blue_type] += 1
    unit_total[red_type] += 1

    if winner == 'blue':
        unit_wins[blue_type] += 1
    else:
        unit_wins[red_type] += 1

print("\n1v1 Win rates:")
win_rates = {}
for unit_type in sorted(unit_types):
    if unit_total[unit_type] > 0:
        win_rate = unit_wins[unit_type] / unit_total[unit_type]
        win_rates[unit_type] = win_rate
        print(f"  {unit_type}: {unit_wins[unit_type]}/{unit_total[unit_type]} = {win_rate:.4f}")

best_1v1 = max(win_rates.items(), key=lambda x: x[1])
print(f"\n답: {best_1v1[0]} (승률: {best_1v1[1]:.4f})")

# ====== Problem 4-2: 배치 효과 분석 ======
print("\n=== Problem 4-2: 배치 효과 분석 ===")

# For each unit, track wins when positioned front vs back
# Front = closer to enemy, Back = farther from enemy
unit_front_wins = defaultdict(int)
unit_front_total = defaultdict(int)
unit_back_wins = defaultdict(int)
unit_back_total = defaultdict(int)

for battle in battles:
    blue_units = battle['blue']
    red_units = battle['red']
    winner = battle['winner']

    # Calculate average positions
    if len(blue_units) > 0:
        blue_avg_x = sum(parse_coords(u['at'])[0] for u in blue_units) / len(blue_units)
    if len(red_units) > 0:
        red_avg_x = sum(parse_coords(u['at'])[0] for u in red_units) / len(red_units)

    # For blue team (lower x = toward left, higher x = toward right)
    # If red is on the right (higher x), then blue's front is higher x
    for unit in blue_units:
        x, y = parse_coords(unit['at'])
        unit_type = unit['type']

        # Front for blue = closer to red (higher x if red is on right)
        if x > blue_avg_x:  # front
            unit_front_total[unit_type] += 1
            if winner == 'blue':
                unit_front_wins[unit_type] += 1
        elif x < blue_avg_x:  # back
            unit_back_total[unit_type] += 1
            if winner == 'blue':
                unit_back_wins[unit_type] += 1

    # For red team
    for unit in red_units:
        x, y = parse_coords(unit['at'])
        unit_type = unit['type']

        # Front for red = closer to blue (lower x if blue is on left)
        if x < red_avg_x:  # front
            unit_front_total[unit_type] += 1
            if winner == 'red':
                unit_front_wins[unit_type] += 1
        elif x > red_avg_x:  # back
            unit_back_total[unit_type] += 1
            if winner == 'red':
                unit_back_wins[unit_type] += 1

print("\nFront vs Back placement win rates:")
placement_diffs = {}
for unit_type in sorted(unit_types):
    front_rate = unit_front_wins[unit_type] / unit_front_total[unit_type] if unit_front_total[unit_type] > 0 else 0
    back_rate = unit_back_wins[unit_type] / unit_back_total[unit_type] if unit_back_total[unit_type] > 0 else 0
    diff = abs(front_rate - back_rate)
    placement_diffs[unit_type] = diff
    print(f"  {unit_type}: Front {front_rate:.4f} ({unit_front_total[unit_type]}회) vs Back {back_rate:.4f} ({unit_back_total[unit_type]}회), Diff: {diff:.4f}")

max_diff_unit = max(placement_diffs.items(), key=lambda x: x[1])
print(f"\n답: {max_diff_unit[0]} (차이: {max_diff_unit[1]:.4f})")

# ====== Problem 4-3: 진형 우세 분석 ======
print("\n=== Problem 4-3: 진형 우세 분석 ===")

x_formation_wins = 0
y_formation_wins = 0
x_formation_total = 0
y_formation_total = 0

for battle in battles:
    for team, winner_name in [('blue', 'blue'), ('red', 'red')]:
        units = battle[team]
        if len(units) < 2:
            continue

        coords = [parse_coords(u['at']) for u in units]
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]

        x_range = max(xs) - min(xs)
        y_range = max(ys) - min(ys)

        if x_range > y_range:  # x방향으로 긴 진형
            x_formation_total += 1
            if battle['winner'] == winner_name:
                x_formation_wins += 1
        elif y_range > x_range:  # y방향으로 긴 진형
            y_formation_total += 1
            if battle['winner'] == winner_name:
                y_formation_wins += 1

x_rate = x_formation_wins / x_formation_total if x_formation_total > 0 else 0
y_rate = y_formation_wins / y_formation_total if y_formation_total > 0 else 0

print(f"X-formation (가로로 넓음): {x_formation_wins}/{x_formation_total} = {x_rate:.4f}")
print(f"Y-formation (세로로 긴): {y_formation_wins}/{y_formation_total} = {y_rate:.4f}")
print(f"\n답: {'x 방향으로 긴 진형' if x_rate > y_rate else 'y 방향으로 긴 진형'}")

# ====== Problem 4-4: 상성 관계 분석 ======
print("\n=== Problem 4-4: 상성 관계 분석 ===")

matchup_results = defaultdict(lambda: {'wins': 0, 'total': 0})

for battle in one_v_one_battles:
    blue_type = battle['blue'][0]['type']
    red_type = battle['red'][0]['type']
    winner = battle['winner']

    matchup = f"{blue_type}_vs_{red_type}"
    reverse_matchup = f"{red_type}_vs_{blue_type}"

    matchup_results[matchup]['total'] += 1
    matchup_results[reverse_matchup]['total'] += 1

    if winner == 'blue':
        matchup_results[matchup]['wins'] += 1
    else:
        matchup_results[reverse_matchup]['wins'] += 1

print("\n선택지 검증 (A > B는 A가 B를 이긴다는 의미):")
test_counters = [
    ('cbene', 'aleo'),
    ('eyanoo', 'dgreg'),
    ('dgreg', 'aleo'),
    ('bras', 'cbene'),
    ('aleo', 'eyanoo'),
    ('eyanoo', 'bras'),
    ('bras', 'dgreg'),
    ('cbene', 'eyanoo'),
    ('aleo', 'bras'),
    ('dgreg', 'cbene')
]

wrong_statements = []
for a, b in test_counters:
    matchup = f"{a}_vs_{b}"
    if matchup_results[matchup]['total'] > 0:
        win_rate = matchup_results[matchup]['wins'] / matchup_results[matchup]['total']
        is_correct = win_rate > 0.5
        status = "O" if is_correct else "X"
        print(f"  {a} > {b}: {status} (승률: {win_rate:.4f}, {matchup_results[matchup]['wins']}/{matchup_results[matchup]['total']})")
        if not is_correct:
            wrong_statements.append(f"{a} > {b}")

print(f"\n답 (옳지 않은 것): {', '.join(wrong_statements)}")

print("\n=== 분석 1단계 완료 ===")


# ============================================================================
# 코드 2: 문제 4-5 데이터 검증 (analyze_problem_4_5.py)
# ============================================================================

import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_center(units):
    coords = [parse_coords(u['at']) for u in units]
    avg_x = sum(c[0] for c in coords) / len(coords)
    avg_y = sum(c[1] for c in coords) / len(coords)
    return avg_x, avg_y

def get_avg_distance_between_units(units):
    if len(units) < 2:
        return 0
    coords = [parse_coords(u['at']) for u in units]
    total = 0
    count = 0
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            total += distance(coords[i], coords[j])
            count += 1
    return total / count if count > 0 else 0

print("\n=== Problem 4-5: 데이터 내용 검증 ===\n")

# Statement 1: 팀의 중심이 좌표의 중심(10.5, 10.5)에 가까울수록 승률이 높다
print("Statement 1: 팀의 중심이 좌표의 중심(10.5, 10.5)에 가까울수록 승률이 높다")

center_point = (10.5, 10.5)
close_wins = 0
close_total = 0
far_wins = 0
far_total = 0

for battle in battles:
    for team_name in ['blue', 'red']:
        units = battle[team_name]
        if len(units) == 0:
            continue

        center = get_center(units)
        dist = distance(center, center_point)

        if dist < 5:  # Close to center
            close_total += 1
            if battle['winner'] == team_name:
                close_wins += 1
        elif dist > 10:  # Far from center
            far_total += 1
            if battle['winner'] == team_name:
                far_wins += 1

close_rate = close_wins / close_total if close_total > 0 else 0
far_rate = far_wins / far_total if far_total > 0 else 0

print(f"  중심에 가까운 경우: {close_wins}/{close_total} = {close_rate:.4f}")
print(f"  중심에서 먼 경우: {far_wins}/{far_total} = {far_rate:.4f}")
print(f"  → 올바르지 않음: {close_rate <= far_rate}\n")

# Statement 2: 같은 팀 유닛 간 거리가 가까울수록 승률이 높아지는 경향
print("Statement 2: 같은 팀 유닛 간 거리가 가까울수록 승률이 높아지는 경향을 보인다")

multi_unit_battles = [b for b in battles if len(b['blue']) > 1 or len(b['red']) > 1]
close_dist_wins = 0
close_dist_total = 0
far_dist_wins = 0
far_dist_total = 0

for battle in multi_unit_battles:
    for team_name in ['blue', 'red']:
        units = battle[team_name]
        if len(units) < 2:
            continue

        avg_dist = get_avg_distance_between_units(units)

        if avg_dist < 5:
            close_dist_total += 1
            if battle['winner'] == team_name:
                close_dist_wins += 1
        elif avg_dist > 10:
            far_dist_total += 1
            if battle['winner'] == team_name:
                far_dist_wins += 1

close_dist_rate = close_dist_wins / close_dist_total if close_dist_total > 0 else 0
far_dist_rate = far_dist_wins / far_dist_total if far_dist_total > 0 else 0

print(f"  유닛 간 거리 가까운 경우: {close_dist_wins}/{close_dist_total} = {close_dist_rate:.4f}")
print(f"  유닛 간 거리 먼 경우: {far_dist_wins}/{far_dist_total} = {far_dist_rate:.4f}")
print(f"  → 올바르지 않음: {close_dist_rate <= far_dist_rate}\n")

# Statement 3: dgreg는 전방에 위치할 때가 후방에 위치할 때보다 승률이 높다
print("Statement 3: dgreg는 전방에 위치할 때가 후방에 위치할 때보다 승률이 높다")

dgreg_front_wins = 0
dgreg_front_total = 0
dgreg_back_wins = 0
dgreg_back_total = 0

for battle in battles:
    for team_name in ['blue', 'red']:
        units = battle[team_name]
        if len(units) == 0:
            continue

        avg_x = sum(parse_coords(u['at'])[0] for u in units) / len(units)

        for unit in units:
            if unit['type'] != 'dgreg':
                continue

            x, y = parse_coords(unit['at'])

            is_front = False
            if team_name == 'blue' and x > avg_x:
                is_front = True
            elif team_name == 'red' and x < avg_x:
                is_front = True

            if is_front:
                dgreg_front_total += 1
                if battle['winner'] == team_name:
                    dgreg_front_wins += 1
            else:
                dgreg_back_total += 1
                if battle['winner'] == team_name:
                    dgreg_back_wins += 1

dgreg_front_rate = dgreg_front_wins / dgreg_front_total if dgreg_front_total > 0 else 0
dgreg_back_rate = dgreg_back_wins / dgreg_back_total if dgreg_back_total > 0 else 0

print(f"  dgreg 전방: {dgreg_front_wins}/{dgreg_front_total} = {dgreg_front_rate:.4f}")
print(f"  dgreg 후방: {dgreg_back_wins}/{dgreg_back_total} = {dgreg_back_rate:.4f}")
print(f"  → 올바르지 않음: {dgreg_front_rate <= dgreg_back_rate}\n")

# Statement 4: 4대4 전투에서, aleo+bras+dgreg+eyanoo 조합의 승률은 60% 이상이다
print("Statement 4: 4대4 전투에서, aleo+bras+dgreg+eyanoo 조합의 승률은 60% 이상이다")

four_v_four = [b for b in battles if len(b['blue']) == 4 and len(b['red']) == 4]
target_combo = {'aleo', 'bras', 'dgreg', 'eyanoo'}

combo_wins = 0
combo_total = 0

for battle in four_v_four:
    for team_name in ['blue', 'red']:
        units = battle[team_name]
        unit_types = {u['type'] for u in units}

        if unit_types == target_combo:
            combo_total += 1
            if battle['winner'] == team_name:
                combo_wins += 1

combo_rate = combo_wins / combo_total if combo_total > 0 else 0

print(f"  aleo+bras+dgreg+eyanoo 조합: {combo_wins}/{combo_total} = {combo_rate:.4f}")
print(f"  → 올바르지 않음: {combo_rate < 0.6}\n")

# Statement 5: 2대2 전투에서 aleo+dgreg 조합은 bras+eyanoo 조합에게 26전 25승을 기록했다
print("Statement 5: 2대2 전투에서 aleo+dgreg 조합은 bras+eyanoo 조합에게 26전 25승을 기록했다")

two_v_two = [b for b in battles if len(b['blue']) == 2 and len(b['red']) == 2]
combo1 = {'aleo', 'dgreg'}
combo2 = {'bras', 'eyanoo'}

matchup_wins = 0
matchup_total = 0

for battle in two_v_two:
    blue_types = {u['type'] for u in battle['blue']}
    red_types = {u['type'] for u in battle['red']}

    if blue_types == combo1 and red_types == combo2:
        matchup_total += 1
        if battle['winner'] == 'blue':
            matchup_wins += 1
    elif blue_types == combo2 and red_types == combo1:
        matchup_total += 1
        if battle['winner'] == 'red':
            matchup_wins += 1

print(f"  aleo+dgreg vs bras+eyanoo: {matchup_wins}승 in {matchup_total}전")
print(f"  → 올바르지 않음: {not (matchup_total == 26 and matchup_wins == 25)}\n")


# ============================================================================
# 코드 3: 문제 4-6 승자 예측 (predict_battles.py)
# ============================================================================

# Load test data
with open('AI_TOP_100/ai_top_100_modeling 4번/test_battles.json', 'r') as f:
    test_battles = json.load(f)

print("\n=== Problem 4-6: 전투 결과 예측 ===\n")

# Simple rule-based prediction
def predict_winner_simple(battle):
    blue_units = battle['blue']
    red_units = battle['red']

    # For 1v1, use matchup data
    if len(blue_units) == 1 and len(red_units) == 1:
        blue_type = blue_units[0]['type']
        red_type = red_units[0]['type']
        matchup = f"{blue_type}_vs_{red_type}"

        if matchup_results[matchup]['total'] > 0:
            blue_winrate = matchup_results[matchup]['wins'] / matchup_results[matchup]['total']
            return 'blue' if blue_winrate > 0.5 else 'red'

    # Calculate team power
    blue_power = sum(unit_wins[u['type']] / unit_total[u['type']] if unit_total[u['type']] > 0 else 0.5
                     for u in blue_units)
    red_power = sum(unit_wins[u['type']] / unit_total[u['type']] if unit_total[u['type']] > 0 else 0.5
                    for u in red_units)

    # Add positional advantage
    blue_coords = [parse_coords(u['at']) for u in blue_units]
    red_coords = [parse_coords(u['at']) for u in red_units]

    if blue_coords:
        blue_center_x = sum(c[0] for c in blue_coords) / len(blue_coords)
    else:
        blue_center_x = 10.5

    if red_coords:
        red_center_x = sum(c[0] for c in red_coords) / len(red_coords)
    else:
        red_center_x = 10.5

    # Units closer to enemy get slight bonus
    if blue_center_x > 10.5:
        blue_power *= 1.05
    if red_center_x < 10.5:
        red_power *= 1.05

    return 'blue' if blue_power > red_power else 'red'

# Make predictions
print("Making predictions...")
predictions = []

for battle in test_battles:
    winner = predict_winner_simple(battle)
    predictions.append({
        "battle_id": battle['id'],
        "winner": winner
    })

# Save predictions
output = json.dumps(predictions, ensure_ascii=False, indent=2)
with open('battle_predictions.json', 'w') as f:
    f.write(output)

print(f"Predictions saved to battle_predictions.json")
print(f"Total predictions: {len(predictions)}")

# Count distribution
blue_wins = sum(1 for p in predictions if p['winner'] == 'blue')
red_wins = sum(1 for p in predictions if p['winner'] == 'red')
print(f"\nPrediction distribution:")
print(f"  Blue wins: {blue_wins} ({blue_wins/len(predictions)*100:.1f}%)")
print(f"  Red wins: {red_wins} ({red_wins/len(predictions)*100:.1f}%)")

print("\n=== 전체 분석 완료 ===")
