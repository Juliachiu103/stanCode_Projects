"""
File: narcissistic_checker.py
Name: Julia
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    (1) repeatedly divided by 10 and keep the remainder can get each individual digits
    (2) use num//10('floor division) can get other digits
    """
    print('Welcome to the narcissistic checker!')
    while True:
        num = int(input('n: '))
        num1 = num
        total = 0
        if num == EXIT:
            print('Have a good one!')
            break
        while num1 != 0:
            sub = num1 % 10
            total += sub**(len(str(num)))
            num1 = num1//10
        if total == num:
            print(str(num)+' is a narcissistic number')
        else:
            print(str(num)+' is not a narcissistic number')


            





if __name__ == '__main__':
    main()
