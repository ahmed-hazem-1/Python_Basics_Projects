# This is "Number Guessing Challenge"
import random

number = random.randint(1, 10)
chance = 3
print("You have 3 chances to predict the random number between 1 and 10.")

while chance > 0:
    user_number = int(input(f"You have {chance} chances left.\nEnter a number: "))
    if user_number == number:
        print("Correct! You guessed the number.\n")
        break
    elif user_number < number:
        print("Incorrect. Your guess is too low.\n")
    elif user_number > number:
        print("Incorrect. Your guess is too high.\n")
    chance -= 1

if chance == 0:
    print(f"Sorry, you've run out of chances. The correct number was {number}.")
