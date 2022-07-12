"""
File: factioral.py
Name: Julia
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	use 'ans *= num' to multiply the entered number.
	"""
	print('Welcome to stanCode factorial master!')
	num = int(input('Give me a number, and I will list the answer of factorial: '))
	ans = 1
	if num == EXIT:
		print('------ See ya! -------')
	else:
		print('Answer: ' + str(ans))
		while True:
			num = int(input('Give me a number, and I will list the answer of factorial: '))
			if num == EXIT:
				print('------ See ya! -------')
				break
			else:
				ans *= num
				print('Answer: ' + str(ans))






if __name__ == '__main__':
	main()