"""
File: number_checker.py
Name: Julia
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    (1) determine if the entered number is equal to the EXIT number
    (2) find out the entered number's true factors (not include itself), and sum up
    (3) determine it's a Perfect, Abundant or Deficient number.
    """
    print('Welcome to the number checker!')
    while True:
        num = int(input('n: '))
        total = 0
        # (1)
        if num == EXIT:
            print('Have a good one!')
            break
        # (2)
        for i in range(1, num):
            # find out the true factor
            if num % i == 0:
                total += i
        # (3)
        if total == num:
            print(str(num) + ' is a perfect number')
        elif total > num:
            print(str(num) + ' is an abundant number')
        else:
            print(str(num) + ' is a deficient number')








### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
