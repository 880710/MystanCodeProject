"""
File: draw_line
Name:Amber
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
SIZE =10
first_point = 0
sec_point = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle)

def circle(mouse):
    global first_point
    global sec_point
    if first_point == 0: #0 = the odd point
        first_point = GOval(SIZE,SIZE,x = mouse.x-SIZE/2,y = mouse.y-SIZE/2)
        #record the first point and make a circle
        window.add(first_point)
    else:
        sec_point = GLine(first_point.x,first_point.y,mouse.x,mouse.y)
        #using the second point(mouse) to make a line with first point as the starting point
        window.remove(first_point)  #removing the first point circle
        window.add(sec_point)
        first_point = 0  #restart making a new line,so first_point = 0


if __name__ == "__main__":
    main()
