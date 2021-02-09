WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    """Checks if the criteria for cooking state is satisfied"""
    states = {
        'well-done': WELL_DONE,
        'medium': MEDIUM,
    }

    cooked_state = time * temperature * pressure * COOKED_CONSTANT

    if cooked_state >= states[desired_state]:
        return True
    return False

print(is_cookeding_criteria_satisfied(60,375,600, 'medium'))
