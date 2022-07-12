"""
File: draw_line.py
Name: Julia
-------------------------
let every two points form a line, and use circle represent single point
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the circle
SIZE = 20

# Global Variable
window = GWindow()
count = 1
x1 = 0
y1 = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    """
    if count is odd, draw a circle and then record mouse.x and mouse.y as x1 and y1.
    else remove previous circle and draw a line from last click to this click.
    """
    global count, x1, y1  # let count, x1, x2 be Global Variable
    if count % 2 != 0:
        circle = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)  # let mouse be the center of circle
        circle.filled = False
        circle.color = "navy"
        window.add(circle)
        x1 = mouse.x
        y1 = mouse.y
        count += 1
    else:
        circle_obj = window.get_object_at(x1, y1)
        window.remove(circle_obj)
        line = GLine(x1, y1, mouse.x, mouse.y)
        line.color = "navy"
        window.add(line)
        count += 1


if __name__ == "__main__":
    main()
