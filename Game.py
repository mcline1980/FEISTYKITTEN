from Function_UserCreator import Player  # Import player class object from file
from Function_UserCreator import user_create
import random

# 1) Pass char_sn -- the secret number
# 2) Pass char_max_health -- the maximum number of chances the character can earn
# 3) Pass char_life -- the starting health of the character
# Define the character for the game
sn = 19
user_create(sn, 10, 5)


# Define Player Input Function with error handling
# Simple error/exception handling using a WHILE loop
def number_input():
    error_condition = True
    while error_condition:
        try:
            error_condition = False
            temp_number = int(
                input(f"Guess the number, you have {Player.char_try} attempts and {Player.char_life} tries remaining:"))
            return temp_number

        except ValueError:
            error_condition = True
            print("Please Try Again")
        except TypeError:
            error_condition = True
            print("Please Try Again")


# Start Game
# While the players health is positive
# If the player guesses above the range, they take a 'hit' and do not gain an attempt.
# If the player guesses below the range, they earn an attempt.
# The game runs until the attempts (Player.char_life) run out or the player guesses the number.

secret_number = Player.char_sn
win = False

while Player.char_life > 0:
    # INPUT
    number = number_input()
    # INPUT
    Player.char_try += 1
    Player.char_life -= 1
    if number < secret_number:
        Player.char_life += 2
        print(
            f"You have guessed below the range, you gain an attempt. You now have {Player.char_life} attempts remaining.")
    if Player.char_life > Player.char_max_health:
        print(f"You have reached the maximum number of attempts. Please keep guessing.")
        Player.char_life = Player.char_max_health
    if number == secret_number:
        print("You win!")
        break
    else:
        print("Try again.")
else:
    print(f"You ran out of chances. {Player.char_try} and {Player.char_life}")
