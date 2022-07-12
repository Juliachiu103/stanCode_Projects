"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=((self.window.width - self.paddle.width) / 2),
                        y=(self.window.height - paddle_offset - self.paddle.height))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window.width/2 - ball_radius, y=self.window.height/2)

        # Default initial velocity for the ball
        # self.__dx = 0
        # self.__dy = 0
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        self.bricks_rows = brick_rows
        self.bricks_cols = brick_cols

        # Initialize our mouse listeners
        onmouseclicked(self.click_start)
        onmousemoved(self.paddle_move)

        # Initialize state of the game
        self.__game_active = False

        # Draw bricks (如何把顏色寫進for loop)
        brick_color = ["red", "orange", "yellow", "green", "blue"]
        for col in range(1, brick_cols + 1):
            for row in range(1, brick_rows + 1):
                self.bricks = GRect(width=brick_width, height=brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = brick_color[(row - 1)//2]
                self.bricks.color = brick_color[(row - 1)//2]
                self.window.add(self.bricks, x=col * (brick_width + brick_spacing) - brick_width,
                                y=row * (brick_spacing + brick_height) - brick_height)

        # Create a label of scores
        self.scores_label = GLabel("Score: " + str(0))
        self.scores_label.font = "-20"
        self.scores_label.color = "navy"

        # Create a label of lives
        self.lives_label = GLabel("Life: " + "   ")
        self.lives_label.font = "-20"
        self.lives_label.color = "navy"

    # The paddle's animation
    def paddle_move(self, event):
        if not(self.ball.x == (self.window.width - self.ball.width) / 2 and self.ball.y == (
                self.window.height / 2) and self.__dx == 0 and self.__dy == 0):
            if event.x < self.paddle.width/2:
                paddle_x = 0
            elif event.x > self.window.width-self.paddle.width/2:
                paddle_x = self.window.width-self.paddle.width
            else:
                paddle_x = event.x - self.paddle.width / 2
            self.window.add(self.paddle, x=paddle_x, y=self.paddle.y)

    # Mouse click to active game
    def click_start(self, event):
        if 0 < event.x < self.window.width and 0 < event.y < self.window.height:
            if self.__game_active:
                self.set_ball_velocity()
            self.__game_active = True

    # Get the state of the game
    def get_state(self):
        return self.__game_active

    # Set the ball's velocity
    def set_ball_velocity(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # reset ball's position
    def reset_ball_position(self):
        self.__game_active = False
        self.ball.x = (self.window.width - self.ball.width)/2
        self.ball.y = (self.window.height - self.ball.height)/2
        self.window.add(self.ball)

    def get_x_speed(self):
        return self.__dx

    def get_y_speed(self):
        return self.__dy

    def check_ball_hit_paddle(self):
        maybe_obj_1 = self.window.get_object_at(x=self.ball.x, y=self.ball.y)
        maybe_obj_2 = self.window.get_object_at(x=self.ball.x + self.ball.width, y=self.ball.y)
        maybe_obj_3 = self.window.get_object_at(x=self.ball.x, y=self.ball.y + self.ball.height)
        maybe_obj_4 = self.window.get_object_at(x=self.ball.x + self.ball.width, y=self.ball.y + self.ball.height)
        if maybe_obj_1 is not None and maybe_obj_1 is self.paddle and maybe_obj_1 is not self.scores_label and \
                maybe_obj_1 is not self.lives_label:
            return True
        elif maybe_obj_3 is not None and maybe_obj_3 is self.paddle and maybe_obj_3 is not self.scores_label and \
                maybe_obj_3 is not self.lives_label:
            return True
        elif maybe_obj_2 is not None and maybe_obj_2 is self.paddle and maybe_obj_2 is not self.scores_label and \
                maybe_obj_2 is not self.lives_label:
            return True
        elif maybe_obj_4 is not None and maybe_obj_4 is self.paddle and maybe_obj_4 is not self.scores_label and \
                maybe_obj_4 is not self.lives_label:
            return True

        # for i in range(2):
        #     for j in range(2):
        #         maybe_obj = self.window.get_object_at(x=self.ball.x + self.ball.width * i,
        #                                               y=self.ball.y + self.ball.height * j)
        #         if maybe_obj is not None:
        #             if maybe_obj is self.paddle and maybe_obj is not self.scores_label and maybe_obj is not self.lives_label:
        #                 return True

    def check_ball_hit_bricks(self):
        for i in range(2):
            for j in range(2):
                maybe_obj = self.window.get_object_at(self.ball.x + self.ball.width * i,
                                                      self.ball.y + self.ball.height * j)
                if maybe_obj is not None and maybe_obj is not self.scores_label and maybe_obj is not self.lives_label and maybe_obj is not self.paddle:
                    self.window.remove(maybe_obj)
                    return True

    def win_the_game(self):
        background = GRect(self.window.width, self.window.height)
        background.filled = True
        background.fill_color = "white"
        background.color = "white"
        label_win = GLabel("YOU WIN!")
        label_win.font = "-50"
        label_win.color = "navy"
        self.window.clear()
        self.window.add(label_win, x=(self.window.width-label_win.width)/2, y=self.window.height/2)
        self.window.add(self.scores_label, (self.window.width-self.scores_label.width)/2, label_win.y + 80)

    def lose_the_game(self):
        label_lose = GLabel("Game Over!")
        label_lose.font = "-40"
        label_lose.color = "black"
        self.window.clear()
        self.window.add(label_lose, x=(self.window.width-label_lose.width)/2+90, y=(self.window.height+label_lose.height)/2)
        self.window.add(self.lives_label, (self.window.width - self.lives_label.width)/2+10, label_lose.y + 40)







