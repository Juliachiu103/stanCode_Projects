"""
File: largest_digit.py
Name: Julia
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, enter any integer
	:return: int, return the largest digit of the entered integer
	"""
	ans = 0
	if n < 0:
		n = -n
	return find_largest_digit_helper(n, ans)


def find_largest_digit_helper(n, ans):
	if n == 0:  # Base Case
		return ans
	else:
		digit = n % 10
		if digit > ans:
			ans = digit
		return find_largest_digit_helper(n//10, ans)


if __name__ == '__main__':
	main()
