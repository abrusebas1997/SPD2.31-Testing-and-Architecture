import math

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14
    in the sample conpared to the amount in living
    tissue (unitless).
    """
    err = 'Enter a value between 0 and 1'
    if type(carbon_14_ratio) == str:
        raise TypeError(err)
    if carbon_14_ratio > 1:
        raise ValueError(err)
    if carbon_14_ratio <= 0:
        print('No carbon-14 detected.')
        return 0
    return math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
