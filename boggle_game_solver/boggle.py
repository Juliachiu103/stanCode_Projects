"""
File: boggle.py
Name: Julia
----------------------------------------
Create a system to find out all exist words in the dictionary with the 4x4 alphabet table input.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Find out possible spellings in the 4x4 alphabet table.
	"""
	start = time.time()
	####################
	dict_list = read_dictionary()

	# enter 16 English letters separated by spaces into four rows
	letter_list = []
	for i in range(4):
		input_letters = input(str(i+1) + " row of letters: ")
		if input_letters[1] == " " and input_letters[3] == " " and input_letters[5] == " ":  # The position of space
			letters = input_letters.lower().split()
			if len(letters) == 4:  # Check if only 4 alphabets
				for letter in letters:
					letter_list.append(letter)
		else:
			print("Illegal input")
			break

	# Start finding boggle
	find_boggles(letter_list, dict_list)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggles(letter_list, dict_list):
	"""
	Find possible spelling words in the list of letters.
	:param letter_list: list, list of the entered alphabets
	:return: str, total number of founded words in the list
	"""
	ans_list = []
	for i in range(len(letter_list)):
		visited_position = [i]
		find_boggles_helper(letter_list, i, letter_list[i], ans_list, visited_position, dict_list)
		visited_position.clear()
	print("There are " + str(len(ans_list)) + " words in total.")


def find_boggles_helper(letter_list, current_position, current_word, answer_list, visited_position, dict_list):
	"""
	:param letter_list: list, list of all entered letters
	:param current_position: int, current letter being executed
	:param current_word: str, current concatenated word
	:param answer_list: list, list of the concatenated words do exist in the dictionary
	:param visited_position: list, store the positions(letters) that has been executed
	:return: list, all founded words
	"""
	# Base case
	if len(current_word) >= 4 and current_word not in answer_list and current_word in dict_list:
		print("Found \"" + current_word + "\"")
		answer_list.append(current_word)

	# set up next position
	if current_position == 0 or current_position == 4 or current_position == 8 or current_position == 12:
		next_step = [-4, -3, 1, 4, 5]
	elif current_position == 3 or current_position == 7 or current_position == 11 or current_position == 15:
		next_step = [-5, -4, -1, 3, 4]
	else:
		next_step = [-5, -4, -3, -1, 1, 3, 4, 5]

	# Recursion
	if has_prefix(current_word, dict_list):
		# choose
		for step in next_step:
			next_position = current_position + step
			if 0 <= next_position <= 15 and next_position not in visited_position:
				next_letter = letter_list[current_position + step]
				current_word += next_letter
				visited_position.append(next_position)
				# explore
				find_boggles_helper(letter_list, next_position, current_word, answer_list, visited_position, dict_list)
				# un-choose
				visited_position.pop()
				current_word = current_word[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dict_list = []
	with open(FILE, "r") as f:
		for word in f:
			dict_list.append(word.split()[0])
	return dict_list


def has_prefix(sub_s, dict_list):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dict_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
