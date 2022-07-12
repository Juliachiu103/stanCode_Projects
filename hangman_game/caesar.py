"""
File: caesar.py
Name: Julia
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Decipher the ciphered information
    """
    num = int(input("Secret number: "))
    ciphered_string = input("What's the ciphered string? ").upper()
    ans = deciphered(ciphered_string, num)
    print("The deciphered string is: " + ans)


def deciphered(ciphered_string, num):
    """
    According to the position of each letter in new_alphabet, find the corresponding letter in ALPHABET in order.
    """
    new_alphabet = ALPHABET[(26 - num):] + ALPHABET[:(26 - num)]
    ans = ""
    space = ""
    for ch in ciphered_string:
        if ch in new_alphabet:
            i = new_alphabet.find(ch)
            ans += ALPHABET[i]
        else:
            ans += ch
    return ans







#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
