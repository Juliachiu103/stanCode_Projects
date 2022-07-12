"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

# Global Variables
lives = NUM_LIVES
score = 0



def main():
    global lives, score
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    scores_label = graphics.scores_label
    lives_label = graphics.lives_label

    graphics.window.add(scores_label, 10, graphics.window.height - 10)
    graphics.window.add(lives_label, graphics.window.width - graphics.lives_label.width/2, graphics.window.height-10)
    lives_label.text = "Life: " + str(lives)

    dx = graphics.get_x_speed()
    dy = graphics.get_y_speed()

    while True:
        pause(FRAME_RATE)
        if graphics.get_state():
            graphics.ball.move(dx, dy)

            # Check if the ball hit the bricks or the paddle
            if graphics.check_ball_hit_paddle():
                dy = -dy

            if graphics.check_ball_hit_bricks():
                score += 1
                scores_label.text = "Score: " + str(score)
                # Set up the condition of winning the game
                if score == graphics.bricks_cols * graphics.bricks_rows:
                    graphics.win_the_game()
                    break
                dy = -dy

            # Check the boundary, and if ball is out of the bottom boundary and lose one life
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            if graphics.ball.y <= 0:
                dy = -dy
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.window.remove(graphics.ball)
                graphics.reset_ball_position()
                graphics.set_ball_velocity()
                lives -= 1
                lives_label.text = "Life: " + str(lives)
                if lives == 0:
                    graphics.lose_the_game()
                    break




















if __name__ == '__main__':
    main()
