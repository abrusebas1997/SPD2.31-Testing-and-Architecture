def change_gear(str_gear):
    print("Gear changed to", str_gear)

def display_gear(str_gear):
    print("displayed gear:", str_gear)

def set_gear(gear):
    change_gear(gear)
    display_gear(gear)

def process_speed(speed):
    gears = {
        'R': (0, 0),
        '1': (0, 30),
        '2' : (30,50),
        '3': (50,90),
        '4': (90, 90)
    }

    if speed < 0:
        display_gear('R')
        return
    elif speed > gears['4'][0]:
        set_gear('4')
        return

    for gear, speeds in gears.items():
        if speed in range(int(speeds[0]), int(speeds[1])):
            set_gear(gear)
            return

if __name__ == "__main__":
    process_speed(40)
