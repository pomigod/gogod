def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    is_crashed = params['is_crashed']

    if not all_wheels_on_track or is_crashed:
        return float(1e-3)
    else:
        return float(1.0)
