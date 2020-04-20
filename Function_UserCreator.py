import random
import inspect


# Player class. Currently contains default values.
class Player(object):
    def __init__(self, char_id, char_sn, char_max_health, char_life, char_try, name):
        self.name = name
        self.char_id = int(char_id)
        self.char_sn = int(char_sn)
        self.char_max_health = int(char_max_health)
        self.char_life = int(char_life)
        self.char_try = int(char_try)


# The primary user creation function. Currently set to arbitrary default values to feed into the game.
# Once game logic is worked out, we can use this to change defaults.
def user_create(char_sn, char_max_health, char_life):
    # User Defaults
    Player.char_sn = char_sn
    Player.char_max_health = char_max_health
    Player.char_life = char_life
    Player.char_try = 0
    Player.name = input("Please enter your character name: ")
    print(Player.name)
    print(f"You have {Player.char_life} health.")
    Player.char_id = random.randint(0, 5000)
    print(f"Your player ID is: {Player.char_id}")
    return Player


# Test user creation function
# Debugging use only
def user_display():
    for i in inspect.getmembers(Player):
        if not i[0].startswith('_'):
            if not inspect.ismethod(i[1]):
                print(i)


# Create a string to feed into a dictionary indexing the player value.
# To be used for follow on processing/features.
def user_create_string():
    string = [Player.name, Player.char_life, Player.char_try, Player.char_max_health, Player.char_sn]
    user_dict = {Player.char_id: [string]}
    return user_dict


# Write the newly created user to a local text file.
# To be used for creating new features in the future.
def user_write_file(user_dict):
    with open("users.txt", "a") as file:
        file_content = file
        file_content.writelines("\n" + user_dict)


# Testing the functions
#user_create()
#user_create_string()
#user_write_file(str(user_create_string()))
