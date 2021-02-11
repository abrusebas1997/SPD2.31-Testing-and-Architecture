class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

    def get_value(self):
        return self.value

    def get_unit(self):
        return self.unit

    def convert_unit(self):
        if self.unit == 'km':
            return self.value
        elif self.unit == 'ly':
            self.value = self.value * 9.461e12
            self.unit = 'km'
            return self.value
        else:
            print("unit is Unknown")
            return

    def calculate_speed(self, time):
        return self.value/time

class Mass:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

    def convert_unit(self):
        if self.unit == 'kg':
            return self.value
        elif self.unit == 'solar-mass':
            self.value = self.value * 1.98892e30
            self.unit = 'kg'
            return self.value
        else:
            print("unit is Unknown")
            return


def calculate_kinetic_energy(mass, distance, time):
    mass.convert_unit()
    distance.convert_unit()
    speed = distance.calculate_speed(time)

    kinetic_energy = 0.5 * mass.value * speed ** 2
    return kinetic_energy


mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
