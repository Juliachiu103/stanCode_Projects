"""
File: sierpinski.py
Name: Julia
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6              # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow


# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Recursively prints the Sierpinski triangle on GWindow.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int, the order of Sierpinski Triangle
	:param length: int, the length of order-1 Sierpinski Triangle
	:param upper_left_x: int, the upper left x coordinate of order-1 Sierpinski Triangle
	:param upper_left_y: int, the upper left y coordinate of order-1 Sierpinski Triangle
	:return: image, draw one big inverted triangle with three smaller triangles in each corner
	"""
	if order == 0:  # Base case
		return
	else:
		# Draw the triangle
		# Draw upper edge
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		# Draw left edge
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + 0.886 * length)
		# Draw right edge
		line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length / 2, upper_left_y + 0.886 * length)
		window.add(line1)
		window.add(line2)
		window.add(line3)

		# Draw the three smaller triangle recursively
		# Upper left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# Upper right
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# Bottom
		sierpinski_triangle(order-1, length/2, upper_left_x+length/4, upper_left_y+0.886 * length/2)


if __name__ == '__main__':
	main()