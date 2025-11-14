import json
from collections import defaultdict
import math

# Load the data
with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    train_battles = json.load(f)

with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/test_battles.json', 'r') as f:
    test_battles = json.load(f)

def parse_coords(at_str):
    x, y = at_str.split(',')
    return int(x), int(y)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Build 1v1 matchup win rates from training data
print("Building 1v1 matchup statistics...")
matchup_results = defaultdict(lambda: {'wins': 0, 'total': 0})

one_v_one = [b for b in train_battles if len(b['blue']) == 1 and len(b['red']) == 1]
for battle in one_v_one:
    blue_type = battle['blue'][0]['type']
    red_type = battle['red'][0]['type']
    winner = battle['winner']

    matchup = f"{blue_type}_vs_{red_type}"
    matchup_results[matchup]['total'] += 1

    if winner == 'blue':
        matchup_results[matchup]['wins'] += 1

# Build overall unit win rates
unit_wins = defaultdict(int)
unit_total = defaultdict(int)

for battle in train_battles:
    for team_name in ['blue', 'red']:
        for unit in battle[team_name]:
            unit_type = unit['type']
            unit_total[unit_type] += 1
            if battle['winner'] == team_name:
                unit_wins[unit_type] += 1

# Extract features from a battle
def extract_features(battle, include_winner=False):
    blue_units = battle['blue']
    red_units = battle['red']

    features = {}

    # Unit counts
    features['blue_count'] = len(blue_units)
    features['red_count'] = len(red_units)

    # Unit type counts
    for unit_type in ['aleo', 'bras', 'cbene', 'dgreg', 'eyanoo']:
        features[f'blue_{unit_type}'] = sum(1 for u in blue_units if u['type'] == unit_type)
        features[f'red_{unit_type}'] = sum(1 for u in red_units if u['type'] == unit_type)

    # Get coordinates
    blue_coords = [parse_coords(u['at']) for u in blue_units]
    red_coords = [parse_coords(u['at']) for u in red_units]

    # Team centers
    if blue_coords:
        blue_center_x = sum(c[0] for c in blue_coords) / len(blue_coords)
        blue_center_y = sum(c[1] for c in blue_coords) / len(blue_coords)
    else:
        blue_center_x = blue_center_y = 10.5

    if red_coords:
        red_center_x = sum(c[0] for c in red_coords) / len(red_coords)
        red_center_y = sum(c[1] for c in red_coords) / len(red_coords)
    else:
        red_center_x = red_center_y = 10.5

    features['blue_center_x'] = blue_center_x
    features['blue_center_y'] = blue_center_y
    features['red_center_x'] = red_center_x
    features['red_center_y'] = red_center_y

    # Distance to center
    features['blue_dist_to_center'] = distance((blue_center_x, blue_center_y), (10.5, 10.5))
    features['red_dist_to_center'] = distance((red_center_x, red_center_y), (10.5, 10.5))

    # Formation shape (x-spread vs y-spread)
    if len(blue_coords) > 1:
        blue_x_range = max(c[0] for c in blue_coords) - min(c[0] for c in blue_coords)
        blue_y_range = max(c[1] for c in blue_coords) - min(c[1] for c in blue_coords)
        features['blue_x_range'] = blue_x_range
        features['blue_y_range'] = blue_y_range
    else:
        features['blue_x_range'] = 0
        features['blue_y_range'] = 0

    if len(red_coords) > 1:
        red_x_range = max(c[0] for c in red_coords) - min(c[0] for c in red_coords)
        red_y_range = max(c[1] for c in red_coords) - min(c[1] for c in red_coords)
        features['red_x_range'] = red_x_range
        features['red_y_range'] = red_y_range
    else:
        features['red_x_range'] = 0
        features['red_y_range'] = 0

    # Average unit power (based on overall win rate)
    blue_power = sum(unit_wins[u['type']] / unit_total[u['type']] if unit_total[u['type']] > 0 else 0.5
                     for u in blue_units) / len(blue_units) if blue_units else 0.5
    red_power = sum(unit_wins[u['type']] / unit_total[u['type']] if unit_total[u['type']] > 0 else 0.5
                    for u in red_units) / len(red_units) if red_units else 0.5

    features['blue_avg_power'] = blue_power
    features['red_avg_power'] = red_power

    # 1v1 matchup advantage (if applicable)
    if len(blue_units) == 1 and len(red_units) == 1:
        blue_type = blue_units[0]['type']
        red_type = red_units[0]['type']
        matchup = f"{blue_type}_vs_{red_type}"

        if matchup_results[matchup]['total'] > 0:
            features['matchup_blue_winrate'] = matchup_results[matchup]['wins'] / matchup_results[matchup]['total']
        else:
            features['matchup_blue_winrate'] = 0.5
    else:
        features['matchup_blue_winrate'] = 0.5

    if include_winner:
        features['winner'] = 1 if battle['winner'] == 'blue' else 0

    return features

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

    # Units closer to enemy (aggressive positioning) get slight bonus
    if blue_center_x > 10.5:  # Blue pushing forward
        blue_power *= 1.05
    if red_center_x < 10.5:  # Red pushing forward
        red_power *= 1.05

    return 'blue' if blue_power > red_power else 'red'

# Make predictions
print("\nMaking predictions...")
predictions = []

for battle in test_battles:
    winner = predict_winner_simple(battle)
    predictions.append({
        "battle_id": battle['id'],
        "winner": winner
    })

# Save predictions
output = json.dumps(predictions, ensure_ascii=False, indent=2)
with open('/home/user/gogod/battle_predictions.json', 'w') as f:
    f.write(output)

print(f"Predictions saved to battle_predictions.json")
print(f"Total predictions: {len(predictions)}")

# Show sample predictions
print("\nSample predictions:")
for i in range(min(10, len(predictions))):
    print(f"  {predictions[i]['battle_id']}: {predictions[i]['winner']}")

# Count distribution
blue_wins = sum(1 for p in predictions if p['winner'] == 'blue')
red_wins = sum(1 for p in predictions if p['winner'] == 'red')
print(f"\nPrediction distribution:")
print(f"  Blue wins: {blue_wins} ({blue_wins/len(predictions)*100:.1f}%)")
print(f"  Red wins: {red_wins} ({red_wins/len(predictions)*100:.1f}%)")
