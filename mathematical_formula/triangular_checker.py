"""
File: triangular_checker.py
Name: Julia
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    If any consecutive integer less than the entered number multiplied and divided by two equals itself,
    then the number is a triangular number.
    """
    print('Welcome to the triangular number checker!')
    while True:
        num = int(input('n: '))
        a = 0
        if num == EXIT:
            print('Have a good one!')
            break
        elif num == 0 or num == 1:
            a = 1
            print(str(num) + ' is a triangular number')
        else:
            for i in range(num):
                total = i*(i+1)/2
                if total == num:
                    a = 1
                    print(str(num)+' is a triangular number')
        if a == 0:
            print(str(num)+' is not a triangular number')








### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
