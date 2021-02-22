class Cooked:
    WELL_DONE = 3000
    MEDIUM = 2500
    COOKED_CONSTANT = 0.05

    def __init__(self, desired_state):
        self.desired_state = desired_state

    @classmethod
    def level(cls):
        if desired_state == 'well-done':
            return cls.WELL_DONE
        elif desired_state == 'medium':
            return cls.MEDIUM
        else:
            raise ValueError('this is raw')

    def get_progress(self, time, temperature, pressure):
        self.progress = time * temperature * pressure * self.COOKED_CONSTANT
        return self.is_criteria_satisfied()

    def is_criteria_satisfied(self):
        if self.progress >= self.level():
            print('cooking is done.')
        else:
            print('ongoing cooking.')
        return

time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

cooked = Cooked(desired_state)
cooked.get_progress(time, temp, pressure)
