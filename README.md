
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
