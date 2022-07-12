from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Julia
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Pre-condition: Karel is at the Northwest side in the house
    Post-condition: Karel goes outside to get the newspaper, and then go back to the original location
    """
    move_to_newspaper()
    go_back_home()


def move_to_newspaper():
    # Karel walks out the door and picks up the newspaper
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()
    pick_beeper()


def go_back_home():
    # Karel takes the newspaper home and go back to the original location
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
