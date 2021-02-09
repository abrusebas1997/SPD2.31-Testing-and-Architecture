# by Kami Bigdely
# PEP8 - whitespaces and variable names.
# This is a guess game. Guess what number the computer has chosen!

import random

lower_limit = 0
upper_limit = 100
random_number = random.randint(lower_limit, upper_limit)

print("The computer has selected a number between 0 \
    and 100. Use your supernatural superpowers to \
    guess what the number is.")

while True:
    user_guess = int(input("Enter a number between 0 \
            and 100 (including): "))
    if user_guess > random_number:
        print("Guess a smaller number.")
    elif user_guess < random_number:
        print("Guess a larger number.")
    else:  # UserGuess == randomNumber:
        print("You Won!")
        break
