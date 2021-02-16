# class Constant(object):
#     '''You can initialize a value but not change it.'''
#     def __init__(self, value):
#         self.value = value

#     def __get__(self, obj, type=None):
#         return self.value

class Burger:
    PATTY = 70 # [gr]
    PICKLE = 20 # [gr]
    TOMATO = 25 # [gr]
    LETTUCE = 15 # [gr]
    BUN = 95 # [gr]

    def __init__(self, name):
        self.name = name

    def calc_weight(self):
        return 2 * self.PATTY + 4 * self.PICKLE + 3 * self.TOMATO + 2 * self.LETTUCE + 2 * self.BUN

    def get_info(self):
        print(f'{self.name}: {self.calc_weight()} grams')

class SeoulBurger(Burger):
    KIMCHI = 30 # [gr]
    MAYO = 5 # [gr]

    def __init__(self, name):
        super().__init__(name)

    def calc_weight(self):
        return super().calc_weight() + self.KIMCHI + self.MAYO

ny_burger = Burger('NY Burger').get_info()
seoul_burger = SeoulBurger('Seoul Kimchi Burger').get_info()
