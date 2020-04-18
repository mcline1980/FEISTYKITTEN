import random
import inspect


class Player(object):
    def __init__(self):
        self.char_id = 0
        self.char_sn = 0
        self.char_max_health = 20
        self.char_life = 20
        self.char_try = 20
        self.name = ""


def user_create():
    # User Defaults
    Player.char_sn = 19
    Player.char_max_health = 20
    Player.char_life = 20
    Player.char_try = 0
    Player.name = input("Please enter your character name: ")
    print(Player.name)
    print(f"You have {Player.char_life} health.")
    Player.char_id = random.randint(0, 5000)
    print(f"Your player ID is: {Player.char_id}")
    return Player


# Test user creation function
def user_display():
    for i in inspect.getmembers(Player):
        if not i[0].startswith('_'):
            if not inspect.ismethod(i[1]):
                print(i)
