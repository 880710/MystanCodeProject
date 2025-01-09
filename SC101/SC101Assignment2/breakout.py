"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    vx = graphics.get_dx()
    vy = graphics.get_dy()

    while True:
        pause(FRAME_RATE)
        if graphics.game_start: #AT FIRST: self.game_start = False ,as click the mouse  self.game_start =True
            graphics.ball.move(vx,vy)
        #4 corner of the ball (obj1,obj2,obj3,obj4)
        obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2, graphics.ball.y)
        obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball_radius * 2)
        obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball_radius * 2,
                                             graphics.ball.y + graphics.ball_radius * 2)
        if obj1 or obj2 or obj3 or obj4 == graphics.paddle:
            #  as the ball touch the peddle, the ball will bounce
            vx = -vx
            vy = -vy
        if obj1 != None and obj1 != graphics.ball and obj1 != graphics.paddle:
            #  as the ball touch the brick, the brick will be bounce and the ball bounce
            vx = -vx
            vy = -vy
            graphics.window.remove(obj1)
        elif obj2 != None and obj2 != graphics.ball and obj2 != graphics.paddle:
            vx = -vx
            vy = -vy
            graphics.window.remove(obj2)
        elif obj3 != None and obj3 != graphics.ball and obj3 != graphics.paddle:
            vx = -vx
            vy = -vy
            graphics.window.remove(obj3)
        elif obj4 != None and obj4 != graphics.ball and obj4 != graphics.paddle:
            vx = -vx
            vy = -vy
            graphics.window.remove(obj4)
        if graphics.ball.y+graphics.ball.height >= graphics.window.height:
            #as the ball touch the floor ,lives-1 and graphics.game_start turn to False.
            # When click the mouse the next chance starting.graphics.game_start=True
            lives -= 1
            graphics.game_start=False
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.reset_ball() #no lives ,the ball back to the original position
                break
        if graphics.ball.x <= 0 or graphics.ball.x +graphics.ball.width >= graphics.window.width:
            vx = -vx
        if graphics.ball.y <= 0 :
            vy = -vy


            # for i in range(2):
            #     for j in range(2):
            #         new_ball_x = graphics.ball.x + i * graphics.ball_radius * 2
            #         new_ball_y = graphics.ball.y + j * graphics.ball_radius * 2
            #         obj = graphics.window.get_object_at(new_ball_x, new_ball_y)
            #         if obj == graphics.paddle:
            #             vx = -vx
            #             vy = -vy
            #         if obj != None and obj != graphics.ball and obj != graphics.paddle:
            #             vx = -vx
            #             vy = -vy
            #             graphics.window.remove(obj)







if __name__ == '__main__':
    main()
