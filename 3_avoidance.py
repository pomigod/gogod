def reward_function(params):
    objects_left_of_center = params['objects_left_of_center']
    closest_objects = params['closest_objects']
    is_left_of_center = params['is_left_of_center']
    
    reward = 1.0

    # 트랙에 장애물이 있는 경우에만 회피 로직 실행
    if len(closest_objects) > 0:
        closest_object_index = closest_objects[0]
        is_object_on_left = objects_left_of_center[closest_object_index]

        # 장애물과 반대 차선에 있으면 보상
        if is_object_on_left != is_left_of_center:
            reward = 2.0  # 회피 성공 시 높은 보상
        else:
            reward = 1e-3 # 충돌 경로에 있을 경우 낮은 보상

    return float(reward)
