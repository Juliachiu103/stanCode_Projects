"""
File: complement.py
Name: Julia
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Output the complement of the entered DNA strand.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    com = build_complement(dna)
    print("The complement of " + dna + " is " + com)


def build_complement(dna):
    """
    A and T are complementary base sequences.
    C and G are complementary base sequences.
    """
    com = ""
    for ch in dna:
        if ch == 'A':
            com += 'T'
        elif ch == 'T':
            com += 'A'
        elif ch == 'G':
            com += 'C'
        elif ch == 'C':
            com += 'G'
    return com





###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
