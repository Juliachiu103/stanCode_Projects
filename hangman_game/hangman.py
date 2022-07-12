"""
File: hangman.py
Name: Julia
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Guess the correct word in a limited number of times.
    """
    answer = random_word()
    word = print_dash(answer)
    turn = N_TURNS
    print("The word looks like: " + word)
    print("You have " + str(turn) + " guesses left.")
    while turn > 0:
        input_ch = input("Your guess: ").upper()
        if len(input_ch) == 1 and input_ch.isalpha():
            if not word.isalpha():
                turn, word = start_guess(answer, input_ch, turn, word)
                if word.isalpha() and turn > 0:
                    print("You win!!")
                    print("The word was: " + answer)
                    turn = -1
                elif not word.isalpha() and turn > 0:
                    print("The word looks like: " + word)
                    print("You have " + str(turn) + " guesses left.")
                elif turn <= 0:
                    print("You are completely hung : (")
                    print("The word was: " + answer)
        else:
            print("illegal format.")


def start_guess(answer, input_ch, turn, word):
    """
    Determine if the guessed is correct, and show its correct position.
    """
    ans_word = ""
    if input_ch in answer:
        print("You are correct!")
        for i in range(len(answer)):
            if answer[i] == input_ch:
                ans_word += input_ch
            else:
                ans_word += word[i]
        word = ans_word
    else:
        turn -= 1
        print("There is no " + input_ch + "'s in the word.")
    return turn, word


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def print_dash(ans):
    dash = ""
    for i in range(len(ans)):
        dash += "-"
    return dash










#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
