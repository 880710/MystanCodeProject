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
BRICK_WIDTH = 40       # Width of a brick (in pixels)
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
        self.ball_radius = ball_radius
        # Create a paddle
        self.paddle = GRect(paddle_width,paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle,(self.window.width-self.paddle.width)//2,self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2,ball_radius*2)
        self.ball.filled = True
        self.window.add (self.ball,(self.window.width-self.ball.width)//2,(self.window.height-self.ball.height)//2)

        # Draw bricks
        diff_color = brick_rows/5
        for i in  range(brick_cols):
            for j in range(brick_rows):
                brick = GRect(brick_width,brick_height)
                brick.filled = True
                if  j <diff_color:
                    brick.fill_color = 'red'
                elif diff_color <= j < diff_color*2:
                    brick.fill_color = 'orange'
                elif diff_color * 2 <= j < diff_color * 3:
                    brick.fill_color = 'yellow'
                elif diff_color * 3 <= j < diff_color * 4:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                self.window.add(brick,brick_width*i+brick_spacing*i,brick_height*j+brick_spacing*j)

        self._dx = 0
        self._dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        self.game_start = False
        onmouseclicked(self.start)
    def move_paddle(self,mouse):
        #make peddle move
        if mouse.x <0:
            self.paddle.x =0
        elif mouse.x >self.window.width-self.paddle.width:
            self.paddle.x =self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x -self.paddle.width /2

    @staticmethod
    def get_dy():
        dy = random.randint(1,INITIAL_Y_SPEED)
        if random.random()>0.5:
            dy = - dy
        return dy

    @staticmethod
    def get_dx():
        dx = random.randint(1,MAX_X_SPEED)
        if random.random()>0.5:
            dx = - dx
        return dx

    # Default initial velocity for the ball
    def set_ball_velocity(self):
        self._dx = self.get_dx()
        self._dy = self.get_dy()

    def start(self,event):
        if not self.game_start:
            self.set_ball_velocity()
            self.game_start = True

#As Life -1 the ball position will be reset at the first place
    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball.width) // 2
        self.ball.y = (self.window.height - self.ball.height) // 2
        self._dx = 0
        self._dy = 0



