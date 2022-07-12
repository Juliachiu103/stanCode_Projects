"""
File: rocket.py
Name: Julia
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 5


def main():
	"""
	disassemble the whole rocket into six parts: head, belt, upper, lower, belt and head.
	then use "double for loop" to build them.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):
		for j in range(SIZE-i):
			# 印出空白部分
			print(" ", end="")
		for j in range(i+1):
			# 印出 / 部分
			print("/", end="")
		for j in range(i+1):
			print("\\", end="")
		for j in range(i-i):
			# 印出空白部分
			print(" ", end="")
		print("")


def belt():
	print("+", end="")
	for i in range(2*SIZE):
		print("=", end="")
	print("+", end="")
	print("")


def upper():
	for i in range(SIZE):
		print("|", end="")
		for j in range(SIZE-1-i):
			print(".", end="")
		for j in range(i+1):
			print("/", end="")
			print("\\", end="")
		for j in range(SIZE-1-i):
			print(".", end="")
		print("|")


def lower():
	for i in range(SIZE):
		print("|", end="")
		for j in range(i):
			print(".", end="")
		for j in range(SIZE-i):
			print("\\", end="")
			print("/", end="")
		for j in range(i):
			print(".", end="")
		print("|")






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()