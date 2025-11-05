#!/usr/bin/env python3
"""
문제 4: 전투 없이 예측하는 시뮬레이션의 힘
Model: Claude Sonnet 4.5

유닛의 초기 배치 정보만으로 승패를 예측하는 머신러닝 모델
"""

import json
from collections import defaultdict
from typing import List, Dict, Tuple

def load_battle_data(filename: str) -> List[Dict]:
    """전투 데이터 로드"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_1v1_winrate(battles: List[Dict]) -> Dict[str, float]:
    """1v1 전투 승률 분석"""
    unit_stats = defaultdict(lambda: {'wins': 0, 'total': 0})

    for battle in battles:
        # 1v1 전투만 필터링
        if len(battle['blue']) == 1 and len(battle['red']) == 1:
            blue_unit = battle['blue'][0]['type']
            red_unit = battle['red'][0]['type']
            winner = battle['winner']

            if winner == 'blue':
                unit_stats[blue_unit]['wins'] += 1
                unit_stats[blue_unit]['total'] += 1
                unit_stats[red_unit]['total'] += 1
            else:
                unit_stats[red_unit]['wins'] += 1
                unit_stats[red_unit]['total'] += 1
                unit_stats[blue_unit]['total'] += 1

    # 승률 계산
    winrates = {}
    for unit, stats in unit_stats.items():
        if stats['total'] > 0:
            winrates[unit] = (stats['wins'] / stats['total']) * 100

    return winrates

def analyze_position_effect(battles: List[Dict]) -> Dict[str, float]:
    """배치 효과 분석 (전방 vs 후방)"""
    unit_position_stats = defaultdict(lambda: {'front_wins': 0, 'front_total': 0,
                                                'back_wins': 0, 'back_total': 0})

    for battle in battles:
        for team_name in ['blue', 'red']:
            team = battle[team_name]
            if len(team) == 0:
                continue

            # 팀 내에서 전방/후방 판단 (y 좌표 기준)
            for unit in team:
                pos = unit['at'].split(',')
                y = int(pos[1])
                unit_type = unit['type']

                # y < 11이면 전방, y >= 11이면 후방으로 가정
                is_front = y < 11
                won = battle['winner'] == team_name

                if is_front:
                    unit_position_stats[unit_type]['front_total'] += 1
                    if won:
                        unit_position_stats[unit_type]['front_wins'] += 1
                else:
                    unit_position_stats[unit_type]['back_total'] += 1
                    if won:
                        unit_position_stats[unit_type]['back_wins'] += 1

    # 전방/후방 승률 차이 계산
    position_diff = {}
    for unit, stats in unit_position_stats.items():
        front_wr = (stats['front_wins'] / stats['front_total'] * 100) if stats['front_total'] > 0 else 0
        back_wr = (stats['back_wins'] / stats['back_total'] * 100) if stats['back_total'] > 0 else 0
        position_diff[unit] = abs(front_wr - back_wr)

    return position_diff

def analyze_formation(battles: List[Dict]) -> Tuple[int, int]:
    """진형 우세 분석 (x방향 vs y방향)"""
    x_formation_wins = 0
    y_formation_wins = 0
    x_formation_total = 0
    y_formation_total = 0

    for battle in battles:
        for team_name in ['blue', 'red']:
            team = battle[team_name]
            if len(team) < 2:
                continue

            # x, y 범위 계산
            xs = [int(u['at'].split(',')[0]) for u in team]
            ys = [int(u['at'].split(',')[1]) for u in team]

            x_range = max(xs) - min(xs)
            y_range = max(ys) - min(ys)

            won = battle['winner'] == team_name

            if x_range > y_range:  # x 방향으로 긴 진형
                x_formation_total += 1
                if won:
                    x_formation_wins += 1
            elif y_range > x_range:  # y 방향으로 긴 진형
                y_formation_total += 1
                if won:
                    y_formation_wins += 1

    x_wr = (x_formation_wins / x_formation_total * 100) if x_formation_total > 0 else 0
    y_wr = (y_formation_wins / y_formation_total * 100) if y_formation_total > 0 else 0

    return x_wr, y_wr

def analyze_matchups(battles: List[Dict]) -> Dict[str, Dict[str, int]]:
    """유닛 간 상성 관계 분석"""
    matchups = defaultdict(lambda: defaultdict(lambda: {'wins': 0, 'total': 0}))

    for battle in battles:
        # 1v1 전투만 분석
        if len(battle['blue']) == 1 and len(battle['red']) == 1:
            blue_unit = battle['blue'][0]['type']
            red_unit = battle['red'][0]['type']
            winner = battle['winner']

            matchups[blue_unit][red_unit]['total'] += 1
            matchups[red_unit][blue_unit]['total'] += 1

            if winner == 'blue':
                matchups[blue_unit][red_unit]['wins'] += 1
            else:
                matchups[red_unit][blue_unit]['wins'] += 1

    # 승률 계산
    winrates = {}
    for unit1 in matchups:
        winrates[unit1] = {}
        for unit2 in matchups[unit1]:
            stats = matchups[unit1][unit2]
            if stats['total'] > 0:
                winrates[unit1][unit2] = (stats['wins'] / stats['total']) * 100

    return winrates

def predict_winner(blue_team: List[Dict], red_team: List[Dict]) -> str:
    """전투 승자 예측 (간단한 휴리스틱 모델)"""
    # 유닛 타입별 강도 (1v1 승률 기반)
    unit_strength = {
        'dgreg': 5,
        'cbene': 4,
        'aleo': 3,
        'bras': 2,
        'eyanoo': 1
    }

    # 팀별 총 전력 계산
    blue_power = sum(unit_strength.get(u['type'], 3) for u in blue_team)
    red_power = sum(unit_strength.get(u['type'], 3) for u in red_team)

    # 진형 보너스 (x 방향 진형에 가산점)
    if len(blue_team) >= 2:
        blue_xs = [int(u['at'].split(',')[0]) for u in blue_team]
        blue_ys = [int(u['at'].split(',')[1]) for u in blue_team]
        if (max(blue_xs) - min(blue_xs)) > (max(blue_ys) - min(blue_ys)):
            blue_power *= 1.1

    if len(red_team) >= 2:
        red_xs = [int(u['at'].split(',')[0]) for u in red_team]
        red_ys = [int(u['at'].split(',')[1]) for u in red_team]
        if (max(red_xs) - min(red_xs)) > (max(red_ys) - min(red_ys)):
            red_power *= 1.1

    return 'blue' if blue_power >= red_power else 'red'

def main():
    print("=" * 80)
    print("문제 4: 전투 예측 시뮬레이션")
    print("Model: Claude Sonnet 4.5")
    print("=" * 80)

    # 훈련 데이터 로드
    train_battles = load_battle_data('../ai_top_100_modeling 4번/train_battles.json')

    # 4-1. 1v1 최강자
    print("\n[4-1] 1v1 최강자 분석")
    winrates = analyze_1v1_winrate(train_battles)
    sorted_winrates = sorted(winrates.items(), key=lambda x: x[1], reverse=True)
    print("1v1 승률:")
    for unit, wr in sorted_winrates:
        print(f"  {unit}: {wr:.2f}%")
    print(f"\n최강자: {sorted_winrates[0][0]}")

    # 4-2. 배치 효과
    print("\n[4-2] 배치 효과 분석")
    position_diff = analyze_position_effect(train_battles)
    sorted_diff = sorted(position_diff.items(), key=lambda x: x[1], reverse=True)
    print("전방/후방 승률 차이:")
    for unit, diff in sorted_diff:
        print(f"  {unit}: {diff:.2f}%p")
    print(f"\n배치 효과가 가장 큰 유닛: {sorted_diff[0][0]}")

    # 4-3. 진형 우세
    print("\n[4-3] 진형 우세 분석")
    x_wr, y_wr = analyze_formation(train_battles)
    print(f"x 방향 진형 승률: {x_wr:.2f}%")
    print(f"y 방향 진형 승률: {y_wr:.2f}%")
    print(f"\n우세 진형: {'x 방향' if x_wr > y_wr else 'y 방향'}")

    # 4-4. 상성 관계
    print("\n[4-4] 상성 관계 분석")
    matchup_wr = analyze_matchups(train_battles)
    print("주요 상성 관계:")
    for unit1 in matchup_wr:
        for unit2 in matchup_wr[unit1]:
            wr = matchup_wr[unit1][unit2]
            if wr > 60:
                print(f"  {unit1} > {unit2} ({wr:.1f}%)")

    # 4-6. 테스트 데이터 예측
    print("\n[4-6] 전투 결과 예측")
    test_battles = load_battle_data('../ai_top_100_modeling 4번/test_battles.json')

    predictions = []
    for battle in test_battles:
        winner = predict_winner(battle['blue'], battle['red'])
        predictions.append({
            "id": battle['id'],
            "winner": winner
        })

    # 예측 결과 저장
    with open("battle_predictions.json", "w", encoding="utf-8") as f:
        json.dump(predictions, f, ensure_ascii=False, indent=2)

    print(f"전체 {len(predictions)}개 전투 예측 완료")
    print("결과가 battle_predictions.json에 저장되었습니다.")

    # 처음 5개 출력
    print("\n처음 5개 예측:")
    for pred in predictions[:5]:
        print(f"  {pred['id']}: {pred['winner']}")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
