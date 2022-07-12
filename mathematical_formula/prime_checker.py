"""
File: prime_checker.py
Name: Julia
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	Use "while True" to repeatedly input numbers to determine if it is a prime number.
	Let 'a' = 2, if the number divide 'a' and its remainder not equal to zero, then 'a' plus one (a+=1),
	number keep divide 'a' until the remainder equal to zero.
	If the final 'a' equal to the number means that the number is a prime number.

	Idea : A prime number has a remainder equal to zero only when divided by itself.
	"""
	print('Welcome to the prime checker!')
	while True:
		a = 2
		number = int(input('n: '))
		if number == EXIT:
			break
		else:
			while True:
				if number % a != 0:
					a += 1
				else:
					break
			if a != number:
				print(str(number)+' is not a prime number.')
			else:
				print(str(number)+' is a prime number')
	print('Have a good one!')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
