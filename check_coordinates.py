import json

# Load the training data
with open('/home/user/gogod/AI_TOP_100/ai_top_100_modeling 4번/train_battles.json', 'r') as f:
    battles = json.load(f)

def parse_coords(at_str):
    x, y = at_str.split(',')
    return int(x), int(y)

# Check coordinate ranges
all_x = []
all_y = []

for battle in battles[:1000]:  # Sample first 1000 battles
    for unit in battle['blue'] + battle['red']:
        x, y = parse_coords(unit['at'])
        all_x.append(x)
        all_y.append(y)

print(f"X range: {min(all_x)} - {max(all_x)}")
print(f"Y range: {min(all_y)} - {max(all_y)}")

# Show some sample battles
print("\nSample battles:")
for i in range(5):
    battle = battles[i]
    print(f"\nBattle {battle['id']}:")
    print(f"  Blue: {[(u['type'], u['at']) for u in battle['blue']]}")
    print(f"  Red: {[(u['type'], u['at']) for u in battle['red']]}")
    print(f"  Winner: {battle['winner']}")
