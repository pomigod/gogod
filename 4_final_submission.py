import math
import numpy as np

ZONE_1_WAYPOINTS = list(range(15, 45))
ZONE_2_WAYPOINTS = list(range(45, 80))
ZONE_3_WAYPOINTS = list(range(80, 110)) + list(range(0, 15))

def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    is_crashed = params['is_crashed']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    if not all_wheels_on_track or is_crashed:
        return 1e-4

    reward = (progress / 100) ** 1.5
    time_reward = (progress / steps) if steps > 0 else 0
    current_waypoint = closest_waypoints[1]

    if current_waypoint in ZONE_1_WAYPOINTS:
        # Zone 1: 균형
        reward += (0.8 * speed) + time_reward
    elif current_waypoint in ZONE_2_WAYPOINTS:
        # Zone 2: 가속
        reward += (1.5 * (speed**3)) + (2.0 * time_reward)
    elif current_waypoint in ZONE_3_WAYPOINTS:
        # Zone 3: 제어 (로그 함수 적용)
        reward += (0.5 * np.log(speed + 1)) + (0.5 * time_reward)
    else:
        reward += speed + time_reward

    # 주행 품질 보상 (Heading Alignment)
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.degrees(math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]))
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    
    heading_bonus = (1 - (direction_diff / 180.0))**2
    reward *= (1 + heading_bonus)
    
    # 기본 속도 보너스
    reward += (speed / 4.0)
    
    return float(reward)
