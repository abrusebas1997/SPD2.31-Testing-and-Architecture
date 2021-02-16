class Recipe:
    def __init__(self, ingredients):
        self.__ingredients = tuple(ingredients)

    @property
    def ingredients(self):
        return self.__ingredients

    def dice(self, ingredients):
        print("diced all ingredients.")
    def mix_all(self, diced_ingredients):
        print("mixed all.")
    def add_salt(self):
        print('added salt.')
    def pour(self, liquid):
        print('poured', liquid + '.',)

class Shirazi(Recipe):
    def __init__(self, ingredients):
        super().__init__(ingredients)

    def check_ingredients(self, user_ingredients):
        return set(user_ingredients) == set(self.ingredients)

    def prep_salad(self):
        self.dice(self.ingredients)
        self.mix_all(self.ingredients)
        self.add_salt()
        self.pour('lemon juice')
        print('Your yummy shirazi salad is ready!')

    def make_salad(self, user_ingredients):
        if not self.check_ingredients(user_ingredients):
            print('lacks ingredients.')
            return
        self.prep_salad()

shirazi = Shirazi(['cucumber', 'tomato', 'lemon juice', 'onion'])
print(shirazi.make_salad(['cucumber', 'lemon juice', 'tomato']))
