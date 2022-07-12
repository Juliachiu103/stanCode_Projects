"""
File: anagram.py
Name: Julia
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
dict_list = []
word_list = []


def main():
    """
    Finds all the anagrams which is exit in the dictionary for the word input by user
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit) ")
    read_dictionary()
    print(dict_list)

    while True:
        input_word = str(input("Find anagrams for: "))
        if input_word == EXIT:
            break
        else:

            start = time.time()

            print("Searching...")
            find_anagrams(input_word)

        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dict_list
    with open(FILE, "r") as f:
        for data in f:
            # print(data.split()[0])
            dict_list.append(data.split()[0])


def find_anagrams(s):
    """
    :param s: str, the input word
    :return: list, print all exited anagrams
    """
    word_lst = []
    find_anagrams_helper(s, "", word_lst)
    print(f"{len(word_lst)} anagrams: {word_lst}")


def find_anagrams_helper(input_word, current_word, word_lst):
    global count, word_list
    # if len(current_word) == len(input_word):
    if len(input_word) == 0 and current_word not in word_lst:
        if current_word in dict_list:
            word_lst.append(current_word)
            count += 1
            print("Found: ", current_word)
            print("Searching...")

    else:
        for i in range(len(input_word)):
            # choose
            current_word += input_word[i]
            if has_prefix(current_word):
                # explore
                rest_word = input_word[:i]+input_word[i+1:]
                find_anagrams_helper(rest_word, current_word, word_lst)
            # un-choose
            current_word = current_word[:len(current_word)-1]

        # for letter in input_word:
        #     if letter not in current_word:
        #         # choose
        #         current_word += letter
        #         if has_prefix(current_word):
        #             # explore
        #             find_anagrams_helper(input_word, current_word, word_lst)
        #         # un-choose
        #         current_word = current_word[:len(current_word)-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, sub composition of the input word
    :return: boolean, whether the sub_s is in the dictionary
    """
    for word in dict_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
