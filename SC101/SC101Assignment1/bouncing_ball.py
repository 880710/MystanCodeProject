"""
File: 
Name: Amber
-------------------------
TODO:
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
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE,SIZE,x = START_X-SIZE/2,y= START_Y-SIZE/2)
ball.filled = True
window.add(ball)
count = 0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    onmouseclicked(bounce)


def bounce(event):
    energy = 0  #0 as y velocity
    while True:
        global VX,GRAVITY,count
        ball.move(VX,energy)
        if count == 3:
            #if the ball bounce three time ,it will restore the original place and not play again.
            ball.x = START_X - SIZE / 2
            ball.y = START_Y - SIZE / 2
        elif ball.x >= window.width:  #if the ball x > window width, it will reset.
            ball.x = START_X-SIZE/2
            ball.y = START_Y-SIZE/2
            energy = 0  #y velocity = 0
            count += 1  #1 bounce,count+1
            break
        elif ball.y +SIZE/2 >= window.height:  #if the ball touch the floor,  it will bounce
            energy = -energy * REDUCE
        elif energy < -0.8:  #the process of bouncing
            energy *= REDUCE
        elif energy == -0.8:  #if y almost is equal to 0, the ball will drop again.
            energy *= -energy
        else:
            energy += GRAVITY
        pause(DELAY)


if __name__ == "__main__":
    main()
