
# Blood test analysis program

class Levels:
    def __init__(self, good, borderline, high):
        self.good = good
        self.borderline = borderline
        self.high = high

    def is_high(self, result):
        if result >= self.high:
            return True
        return False

    def is_good(self, result):
        if result < self.good:
            return True
        return False

    def is_borderline(self, result):
        if result in self.borderline:
            return True
        return False

TOTAL_CHOLESTEROL = Levels(200, range(200, 240), 240)
LDL = Levels(100, range(130, 160), 160)
TRIGLYCERIDES = Levels(150, range(150, 200), 200)
class Bloodwork:

    def __init__(self, total_cholesterol, ldl, triglycerides):
        self.tc = total_cholesterol
        self.ldl = ldl
        self.trig = triglycerides

    def levels_high(self):
        return TOTAL_CHOLESTEROL.is_high(self.tc) or LDL.is_high(self.ldl) or TRIGLYCERIDES.is_high(self.trig)

    def levels_good(self):
        return TOTAL_CHOLESTEROL.is_good(self.tc) and LDL.is_good(self.ldl) and TRIGLYCERIDES.is_good(self.trig)

    def levels_borderline(self):
        return TOTAL_CHOLESTEROL.is_borderline(self.tc) or LDL.is_borderline(self.ldl) or TRIGLYCERIDES.is_borderline(self.trig)

    def show_TLC_diet(self):
        print("\nStart TLC diet")
        print(" - Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
        print(' - Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
        print(' - oats, barley, and other whole grains.')
        print(' - fruits such as apples, pears, bananas, and oranges.')

    def summary(self):
        # High cholestrol level
        if self.levels_high():
            print('\n*** High cholestrol level ***')
            print('start taking pills such as statins')
            self.show_TLC_diet()
        # good level
        elif self.levels_good():
            print('\n*** Good level of cholestrol ***')
        # Borderline
        elif self.levels_borderline():
            print('\n*** Borderline to moderately elevated ***')
            self.show_TLC_diet()
        else:
            print('Error: unhandled case.')

tc = 70
ldl = 30
trig = 160
Bloodwork(tc, ldl, trig).summary()
