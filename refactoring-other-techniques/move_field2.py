# Kami Bigdely
# Move Field

class Car:
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)

        self.cabin = cabin
        self.fuel_tank = fuel_tank



class Wheel:

    def __init__(self, car = None, wheel_location = None):
        self.car = self.set_car(car)
        self.wheel_location = wheel_location

    @property
    def wheel_location(self):
        return self.__wheel_location

    @wheel_location.setter
    def wheel_location(self, wheel_location):
        self.__wheel_location = wheel_location

    @property
    def tpms_di(self):
         # Tire Pressure Monitoring System.
        return self.__tpms_di.get_serial_number()

    @tpms_di.setter
    def tpms_di(self, tpms_di):
        self.__tpms_di = tpms_di

    def install_tire(self):
        print('remove old tube.')
        print('cleaned tpms: ',
              self.tpms_di.get_serial_number(),
              '.')
        print('installed new tube.')

    def read_tire_pressure(self):
        return self.tpms_di.get_pressure()

    def set_car(self, car):
        self.car = car


class Tpms:
    """Tire Pressure Monitoring System.
    """
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]

    def __repr__(self):
        return self.get_serial_number()

    def get_pressure(self):
        return 3

    def get_serial_number(self):
        return self.serial_number

class Engine:
    def __init__(self):
        pass

class FuelTank:
    def __init__(self):
        pass

class Cabin:
    def __init__(self):
        pass


engine = Engine()
# TODO: Rewrite the following after moving tpms to the 'Wheel' class.
wheels = [Wheel(None, 'front-right'), Wheel(None, 'front-left'),
          Wheel(None, 'back-right'), Wheel(None, 'back-left')]

cabin  = Cabin()

tpms_di = {'front-right': Tpms(983408543), 'front-left':Tpms(4343083),
               'back-right':Tpms(23654835), 'back-left':Tpms(3498857)}

for wheel in wheels:
    for k, v in tpms_di.items():
        if wheel.wheel_location == k:
            wheel.tpms_di = v
            print(wheel.tpms_di)

fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)
