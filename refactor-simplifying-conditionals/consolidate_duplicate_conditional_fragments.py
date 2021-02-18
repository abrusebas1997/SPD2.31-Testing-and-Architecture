class Drink:
    def __init__(self):
        self._mix = []

    @property
    def mix(self):
        return self._mix

    @mix.setter
    def mix(self, addons):
        if len(self.mix) > 1:
            print(f'mixed {self.mix} with {addons}')
        self._mix.extend(addons)

class Menu(Drink):
    def __init__(self, drinks):
        self._drinks = []

        for drink in drinks:
            self._drinks.append(drink)

    def make_drink(self, drink):
        if drink in self._drinks:
            return drink.mix

coffee = Drink()
coffee.mix = ["coffee"]

ice_cream = Drink()
ice_cream.mix = ['ice', 'cream']

strawberry_milkshake = ice_cream
strawberry_milkshake.mix = ['strawberry', 'milk', 'sugar']


menu = Menu([coffee, ice_cream, strawberry_milkshake])

final_drink = menu.make_drink(strawberry_milkshake)
print(final_drink)
