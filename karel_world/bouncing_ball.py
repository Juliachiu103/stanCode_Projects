"""
File: bouncing_ball.py
Name: Julia
-------------------------
Make the ball bounce after clicked the mouse, for only 3 times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
time = 0
vy = 0

# Global Variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(move)


def move(mouse):
    global time, vy
    time += 1
    if time <= 3:
        window.add(ball)
        while ball.x < window.width:
            while (ball.y + SIZE) <= window.height:
                pause(DELAY*1.2)
                vy += GRAVITY
                ball.move(VX, vy)
                pause(DELAY*1.2)
            pause(DELAY * 1.2)
            vy = -REDUCE*vy  # reverse direction and keep only 90%
            while vy < 0:  # vy=0 means reach a relative peak
                pause(DELAY*1.2)
                vy += GRAVITY
                ball.move(VX, vy)
                pause(DELAY*1.2)
        pause(DELAY*1.2)
        window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
