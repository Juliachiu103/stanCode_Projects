from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Julia
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    Pre-condition: Karel is stand at location (1,1) in a k*k square
    Post-condition: Karel put the beepers at intervals, so the inside is like a checkerboard.

    Idea: use facing_east() and facing_west() to decide when to turn_left() and turn_right()

    """
    while front_is_clear():
        fill_one_line()
        # If Karel touch the wall on the right side, then turn left up. Otherwise turn right up.
        if facing_east():
            turn_left()
            if front_is_clear():
                if on_beeper():
                    move()
                    turn_left()
                    move()
                else:
                    move()
                    turn_left()
        else:
            turn_right()
            if front_is_clear():
                if on_beeper():
                    move()
                    turn_right()
                    move()
                else:
                    move()
                    turn_right()


def fill_one_line():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
