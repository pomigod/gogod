import json
from collections import defaultdict, Counter

# Load the training data
with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

print(f"Total battles: {len(battles)}")

# Helper function to parse coordinates
def parse_coords(at_str):
    x, y = at_str.split(',')
    return int(x), int(y)

# Analyze the data
unit_types = set()
for battle in battles:
    for unit in battle['blue'] + battle['red']:
        unit_types.add(unit['type'])

print(f"Unit types: {sorted(unit_types)}")

# Problem 4-1: Find the strongest unit in 1v1 battles
print("\n=== Problem 4-1: 1v1 최강자 ===")
one_v_one_battles = [b for b in battles if len(b['blue']) == 1 and len(b['red']) == 1]
print(f"1v1 battles: {len(one_v_one_battles)}")

# Count wins for each unit type in 1v1
unit_wins = defaultdict(int)
unit_total = defaultdict(int)

for battle in one_v_one_battles:
    blue_unit = battle['blue'][0]
    red_unit = battle['red'][0]
    winner = battle['winner']

    blue_type = blue_unit['type']
    red_type = red_unit['type']

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
        print(f"{unit_type}: {unit_wins[unit_type]}/{unit_total[unit_type]} = {win_rate:.4f}")

best_1v1 = max(win_rates.items(), key=lambda x: x[1])
print(f"\n1v1 최강자: {best_1v1[0]} (승률: {best_1v1[1]:.4f})")

# Problem 4-2: Unit with biggest front-back placement difference
print("\n=== Problem 4-2: 배치 효과 분석 ===")

# For each unit, track wins when positioned front vs back
unit_front_wins = defaultdict(int)
unit_front_total = defaultdict(int)
unit_back_wins = defaultdict(int)
unit_back_total = defaultdict(int)

for battle in battles:
    # Calculate center positions for each team
    blue_units = battle['blue']
    red_units = battle['red']
    winner = battle['winner']

    # For blue team (x < 10.5 is front, x > 10.5 is back)
    for unit in blue_units:
        x, y = parse_coords(unit['at'])
        unit_type = unit['type']

        if x < 10.5:  # front
            unit_front_total[unit_type] += 1
            if winner == 'blue':
                unit_front_wins[unit_type] += 1
        else:  # back
            unit_back_total[unit_type] += 1
            if winner == 'blue':
                unit_back_wins[unit_type] += 1

    # For red team (x > 10.5 is front, x < 10.5 is back)
    for unit in red_units:
        x, y = parse_coords(unit['at'])
        unit_type = unit['type']

        if x > 10.5:  # front
            unit_front_total[unit_type] += 1
            if winner == 'red':
                unit_front_wins[unit_type] += 1
        else:  # back
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
    print(f"{unit_type}: Front {front_rate:.4f} vs Back {back_rate:.4f}, Diff: {diff:.4f}")

max_diff_unit = max(placement_diffs.items(), key=lambda x: x[1])
print(f"\n배치 효과가 가장 큰 유닛: {max_diff_unit[0]} (차이: {max_diff_unit[1]:.4f})")

# Problem 4-3: Formation analysis (x-spread vs y-spread)
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
print(f"Y-formation (세로로 김): {y_formation_wins}/{y_formation_total} = {y_rate:.4f}")
print(f"\n우세한 진형: {'X 방향으로 긴 진형' if x_rate > y_rate else 'Y 방향으로 긴 진형'}")

# Problem 4-4: Counter relationships (상성 관계)
print("\n=== Problem 4-4: 상성 관계 분석 ===")

# Count matchup results
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

print("\nMatchup win rates (A > B means A wins more than 50%):")
counter_relations = []
for unit_a in sorted(unit_types):
    for unit_b in sorted(unit_types):
        if unit_a == unit_b:
            continue
        matchup = f"{unit_a}_vs_{unit_b}"
        if matchup_results[matchup]['total'] > 0:
            win_rate = matchup_results[matchup]['wins'] / matchup_results[matchup]['total']
            if win_rate > 0.5:
                counter_relations.append((unit_a, unit_b, win_rate))
                print(f"{unit_a} > {unit_b}: {win_rate:.4f} ({matchup_results[matchup]['wins']}/{matchup_results[matchup]['total']})")

print("\n선택지 검증:")
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

for a, b in test_counters:
    matchup = f"{a}_vs_{b}"
    if matchup_results[matchup]['total'] > 0:
        win_rate = matchup_results[matchup]['wins'] / matchup_results[matchup]['total']
        is_counter = win_rate > 0.5
        print(f"{a} > {b}: {is_counter} (승률: {win_rate:.4f}, {matchup_results[matchup]['wins']}/{matchup_results[matchup]['total']})")
    else:
        print(f"{a} > {b}: No data")

print("\n분석 완료!")
