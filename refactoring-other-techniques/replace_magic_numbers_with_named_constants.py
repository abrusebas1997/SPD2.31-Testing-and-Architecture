COULOMB_CONST = 8.9875517923*1e9

def calculate_force(c1, c2, distance):
    # [Newton]
    return COULOMB_CONST * c1 * c2 / (distance**2)

q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance be10tween two charges: "))

force = calculate_force(q1, q2, distance)
print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section
# uhh which part is the magic here 🥸
num = int(input('Enter an integer number: '))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
