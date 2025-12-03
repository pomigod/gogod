def reward_function(params):
    objects_left_of_center = params['objects_left_of_center']
    closest_objects = params['closest_objects']
    is_left_of_center = params['is_left_of_center']
    
    reward = 1.0

    if len(closest_objects) > 0:
        closest_object_index = closest_objects[0]
        is_object_on_left = objects_left_of_center[closest_object_index]

        if is_object_on_left != is_left_of_center:
            reward = 2.0
        else:
            reward = 1e-3

    return float(reward)
