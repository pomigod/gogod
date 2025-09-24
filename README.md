
DeepRacer 보상 함수 (Reward Functions)
이 문서는 AWS DeepRacer 챌린지를 위해 설계된 세 가지 다른 보상 함수를 설명합니다.

1. 기본 모델 (Baseline Model)
설명: 가장 기본적인 함수입니다. 트랙을 이탈하거나 장애물과 충돌할 경우 매우 낮은 보상을 주고, 트랙 위를 주행하면 기본 보상을 부여하여 완주 자체에 집중하도록 설계되었습니다.

Python

def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    is_crashed = params['is_crashed']

    if not all_wheels_on_track or is_crashed:
        return float(1e-3)
    else:
        return float(1.0)
        
2. Waypoints 추적 모델
설명: Waypoints를 기반으로 차량의 주행 방향 정확도를 보상에 추가했습니다. 차량의 헤딩이 트랙의 진행 방향과 일치할수록 높은 보상을 주어 안정적인 코너링과 주행을 유도합니다.

Python

import math

def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    is_crashed = params['is_crashed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    if not all_wheels_on_track or is_crashed:
        return float(1e-3)

    reward = 0.5
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    direction_diff = abs(track_direction - heading)

    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    DIRECTION_THRESHOLD = 10.0
    if direction_diff < DIRECTION_THRESHOLD:
        reward += 1.0

    return float(reward)
    
3. 회피 최적화 모델
설명: 장애물 회피에 가장 집중하는 모델입니다. 가장 가까운 장애물의 위치(왼쪽/오른쪽)를 파악하고, 차량이 장애물의 반대편 차선으로 주행할 경우 큰 보상을 주어 충돌을 피하도록 직접적으로 유도합니다.

Python

def reward_function(params):
    objects_left_of_center = params['objects_left_of_center']
    closest_objects = params['closest_objects']
    is_left_of_center = params['is_left_of_center']
    
    reward = 1.0

    # 트랙에 장애물이 있는 경우에만 회피 로직 실행
    if len(closest_objects) > 0:
        # 가장 가까운 장애물의 위치 확인 (True: 왼쪽, False: 오른쪽)
        closest_object_index = closest_objects[0]
        is_object_on_left = objects_left_of_center[closest_object_index]

        # 장애물과 반대 차선에 있으면 보상
        # 예: 장애물이 왼쪽에(True) 있을 때, 차량이 오른쪽에(is_left_of_center=False) 있으면 성공
        if is_object_on_left != is_left_of_center:
            reward = 2.0  # 회피 성공 시 높은 보상
        else:
            reward = 1e-3 # 충돌 경로에 있을 경우 낮은 보상

    return float(reward)












대회 최고 기록 코드:

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
    steering_angle = abs(params['steering_angle'])
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    closest_objects = params['closest_objects']
    objects_location = params['objects_location']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']

    if not all_wheels_on_track:
        return 1e-3
    if is_crashed:
        return 1e-2

    if len(closest_objects) > 0:
        closest_object_idx = closest_objects[0]
        object_loc = objects_location[closest_object_idx]
        car_loc = [params['x'], params['y']]
        dist_to_object = math.sqrt((object_loc[0] - car_loc[0])**2 + (object_loc[1] - car_loc[1])**2)
        
        if dist_to_object < 1.0:
            is_object_on_left = objects_left_of_center[closest_object_idx]
            if is_object_on_left != is_left_of_center:
                return 10.0
            else:
                return 1e-2

    reward = (progress / 100) ** 2
    time_reward = (progress / steps) if steps > 0 else 0

    current_waypoint = closest_waypoints[1]

    def get_in_course_reward(distance_from_center, track_width):
        TARGET_LANE_OFFSET = 0.5
        target_lane_center = (track_width / 2) * TARGET_LANE_OFFSET
        distance_from_target = abs(distance_from_center - target_lane_center)
        in_course_bonus = (1 - (distance_from_target / (track_width / 2)))**2
        return in_course_bonus

    if current_waypoint in ZONE_1_WAYPOINTS:
        in_course_bonus = get_in_course_reward(distance_from_center, track_width)
        reward += (0.8 * speed) + time_reward + (1.2 * in_course_bonus)
    
    elif current_waypoint in ZONE_2_WAYPOINTS:
        reward += (1.5 * (speed**3)) + (2.0 * time_reward)

    elif current_waypoint in ZONE_3_WAYPOINTS:
        # --- [핵심 수정] Zone 3: 급격한 조향 보너스 ---
        sharp_turn_bonus = 0.0
        # 조향각이 20도 이상일 때만 높은 보너스를 부여
        if steering_angle > 20.0:
            sharp_turn_bonus = 2.0
            
        in_course_bonus = get_in_course_reward(distance_from_center, track_width)
        
        reward += sharp_turn_bonus + (1.5 * in_course_bonus) + (0.5 * time_reward)
    
    else:
        reward += speed + time_reward

    return float(reward)






    import math
import numpy as np

# --- [1단계: 존(Zone) 정의] ---
ZONE_1_WAYPOINTS = list(range(15, 45))
ZONE_2_WAYPOINTS = list(range(45, 80))
ZONE_3_WAYPOINTS = list(range(80, 110)) + list(range(0, 15))

def reward_function(params):
    # --- 입력 파라미터 ---
    all_wheels_on_track = params['all_wheels_on_track']
    is_crashed = params['is_crashed']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    steering_angle = abs(params['steering_angle'])
    
    # --- [Level 0] 생존 프로토콜 ---
    if not all_wheels_on_track or is_crashed:
        return 1e-4

    # --- [Level 1] 장애물 회피 프로토콜 ---
    # (장애물 모드에서는 이 부분의 주석을 해제하여 사용)
    # closest_objects = params['closest_objects']
    # if len(closest_objects) > 0:
    #     ... (이전 장애물 회피 로직) ...

    # --- [Level 2] 존(Zone) 기반 주행 시스템 ---
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
        # Zone 3: 제어
        reward += (0.5 * np.log(speed + 1)) + (0.5 * time_reward)
    
    else:
        # 기타 구간: 기본 보상
        reward += speed + time_reward

    # --- [핵심 수정] 주행 품질 보상 시스템 ---
    # 3. 부드러운 조향 유도 (페널티 & 보너스)
    
    # a. 방향 일치 보상 (Heading Bonus)
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.degrees(math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]))
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    
    # 방향 차이가 작을수록 1에 가까운 보너스
    heading_bonus = (1 - (direction_diff / 180.0))**2
    
    # 최종 보상에 주행 품질 요소를 곱해줌
    reward *= (1 + heading_bonus)
    
    # 4. 속도 보너스 (tie-breaker 역할)
    # 기본적인 속도를 유지하도록 약간의 추가 보너스
    reward += (speed / 4.0)
    
    return float(reward)
