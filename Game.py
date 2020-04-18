# DEFAULTS
secret_number = 19
character_try = 0
character_life = 5
character_max_health = 10
secret_number1 = 0


# Define Player Attributes
class Player:
    def __init__(character, name, char_try, char_life, char_max_health, char_sn):
        character.name = name
        character.char_try = character_try
        character.char_life = character_life
        character.char_max_health = character_max_health
        character.char_sn = secret_number1




# Set Player Attributes to Default (TEMPORARY)
Player.char_try = character_try
Player.char_life = character_life
Player.char_max_health = character_max_health
Player.char_sn = secret_number1

# Character Creation
Player.name = input("Please enter your character name: ")
print(Player.name)
print(f"You have {Player.char_life} health.")


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
        Player.char_life = 10
    if number == secret_number:
        print("You win!")
        break
    else:
        print("Try again.")
else:
    print(f"You ran out of chances. {Player.char_try} and {Player.char_life}")
