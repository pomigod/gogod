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
    closest_waypoints = params['closest_waypoints']
    steering_angle = abs(params['steering_angle'])
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    
    closest_objects = params['closest_objects']
    objects_location = params['objects_location']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']

    if not all_wheels_on_track: return 1e-3
    if is_crashed: return 1e-2

    # 장애물 회피 로직
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
        return (1 - (distance_from_target / (track_width / 2)))**2

    if current_waypoint in ZONE_1_WAYPOINTS:
        in_course_bonus = get_in_course_reward(distance_from_center, track_width)
        reward += (0.8 * speed) + time_reward + (1.2 * in_course_bonus)
    
    elif current_waypoint in ZONE_2_WAYPOINTS:
        reward += (1.5 * (speed**3)) + (2.0 * time_reward)

    elif current_waypoint in ZONE_3_WAYPOINTS:
        sharp_turn_bonus = 2.0 if steering_angle > 20.0 else 0.0
        in_course_bonus = get_in_course_reward(distance_from_center, track_width)
        reward += sharp_turn_bonus + (1.5 * in_course_bonus) + (0.5 * time_reward)
    
    else:
        reward += speed + time_reward

    return float(reward)
