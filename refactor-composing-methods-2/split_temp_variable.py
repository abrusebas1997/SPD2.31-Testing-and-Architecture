class Constant(object):
    '''You can initialize a value but not change it.'''
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, type=None):
        return self.value

class Burger:
    PATTY = Constant(70) # [gr]
    PICKLE = Constant(20) # [gr]
    TOMATO = Constant(25) # [gr]
    LETTUCE = Constant(15) # [gr]
    BUN = Constant(95) # [gr]

    def __init__(self, name):
        self.name = name

    def calc_weight(self):
        return 2 * self.PATTY + 4 * self.PICKLE + 3 * self.TOMATO + 2 * self.LETTUCE + 2 * self.BUN

    def get_info(self):
        print(f'{self.name}: {self.calc_weight()} grams')

class SeoulBurger(Burger):
    KIMCHI = Constant(30) # [gr]
    MAYO = Constant(5) # [gr]

    def __init__(self, name):
        super().__init__(name)

    def calc_weight(self):
        return super().calc_weight() + self.KIMCHI + self.MAYO

ny_burger = Burger('NY Burger').get_info()
seoul_burger = SeoulBurger('Seoul Kimchi Burger').get_info()
