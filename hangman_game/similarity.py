"""
File: similarity.py
Name: Julia
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Find out the most similar segments in long DNA sequence for short DNA sequence we want to match
    """
#     dna = input("Please give me a DNA sequence to search: ").upper()
#     seq = input("What DNA sequence would you like to match? ").upper()
#     match = find_match(dna, seq)
#     print("The best match is " + match)
#
#
# def find_match(dna, seq):
#     """
#     Compare the similarity in order and get the short DNA sequence with the highest ratio.
#     """
#     match = ""
#     best = 0
#     for i in range(len(dna)-len(seq)+1):
#         sub_dna = dna[i:len(seq)+i]
#         count = 0
#         for j in range(len(seq)):
#             long = sub_dna[j]
#             short = seq[j]
#             if short == long:
#                 count += 1
#         ratio = count/len(seq)
#         if ratio > best:
#             best = ratio
#             match = sub_dna
#     return match
    s = 's11tan22code4'
    a = secret(s)
    print(a)


def secret(s):
    ans = ""
    total = 0
    for ch in s:
        if ch .isdigit():
            ans += ch
        else:
            total = total + int(ans)
            ans = ""
    return total


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
