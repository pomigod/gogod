import json
from collections import defaultdict
import math

# Load the training data
with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

def parse_coords(at_str):
    x, y = at_str.split(',')
    return int(x), int(y)

def get_center(units):
    coords = [parse_coords(u['at']) for u in units]
    avg_x = sum(c[0] for c in coords) / len(coords)
    avg_y = sum(c[1] for c in coords) / len(coords)
    return avg_x, avg_y

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

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

print("=== Problem 4-5: 데이터 내용 검증 ===\n")

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
print(f"  검증: {close_rate > far_rate} (가까울수록 높아야 함)")
print(f"  → 올바르지 않음: {close_rate <= far_rate}\n")

# Statement 2: 같은 팀 유닛 간 거리가 가까울수록 승률이 높아지는 경향
print("Statement 2: 같은 팀 유닛 간 거리가 가까울수록 승률이 높아지는 경향을 보인다")

# Only analyze multi-unit battles
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

        if avg_dist < 5:  # Close together
            close_dist_total += 1
            if battle['winner'] == team_name:
                close_dist_wins += 1
        elif avg_dist > 10:  # Far apart
            far_dist_total += 1
            if battle['winner'] == team_name:
                far_dist_wins += 1

close_dist_rate = close_dist_wins / close_dist_total if close_dist_total > 0 else 0
far_dist_rate = far_dist_wins / far_dist_total if far_dist_total > 0 else 0

print(f"  유닛 간 거리 가까운 경우: {close_dist_wins}/{close_dist_total} = {close_dist_rate:.4f}")
print(f"  유닛 간 거리 먼 경우: {far_dist_wins}/{far_dist_total} = {far_dist_rate:.4f}")
print(f"  검증: {close_dist_rate > far_dist_rate} (가까울수록 높아야 함)")
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

            # For blue: higher x = front, for red: lower x = front
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
print(f"  검증: {dgreg_front_rate > dgreg_back_rate} (전방이 높아야 함)")
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
print(f"  검증: {combo_rate >= 0.6} (60% 이상이어야 함)")
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

    # Check both directions
    if blue_types == combo1 and red_types == combo2:
        matchup_total += 1
        if battle['winner'] == 'blue':
            matchup_wins += 1
    elif blue_types == combo2 and red_types == combo1:
        matchup_total += 1
        if battle['winner'] == 'red':
            matchup_wins += 1

print(f"  aleo+dgreg vs bras+eyanoo: {matchup_wins}승 in {matchup_total}전")
print(f"  검증: {matchup_total == 26 and matchup_wins == 25}")
print(f"  → 올바르지 않음: {not (matchup_total == 26 and matchup_wins == 25)}\n")

print("\n=== 최종 검증 결과 ===")
wrong_statements = []

if close_rate <= far_rate:
    wrong_statements.append("Statement 1")
if close_dist_rate <= far_dist_rate:
    wrong_statements.append("Statement 2")
if dgreg_front_rate <= dgreg_back_rate:
    wrong_statements.append("Statement 3")
if combo_rate < 0.6:
    wrong_statements.append("Statement 4")
if not (matchup_total == 26 and matchup_wins == 25):
    wrong_statements.append("Statement 5")

print(f"올바르지 않은 것: {', '.join(wrong_statements) if wrong_statements else '없음'}")
