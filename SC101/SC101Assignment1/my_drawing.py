"""
File: CHIIKAWA
Name:Amber
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect,GArc,GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title : chiikawa-Usagi
    As facing a challenge, just scream like Usagi,all difficulties will be solved.wu-la.
    """
    window = GWindow(width=650, height=400, title='USAGI')
    background = GRect(800,400)
    background.filled = True
    background.fill_color = 'floralwhite'
    window.add(background)

    right_ear =GOval(30,150,x =325,y= 30)
    right_ear.filled = True
    right_ear.fill_color = 'lemonchiffon'
    right_ear.color ='dimgray'
    window.add(right_ear)

    left_ear =GOval(30,150,x =275,y= 30)
    left_ear.filled = True
    left_ear.fill_color = 'lemonchiffon'
    left_ear.color ='dimgray'
    window.add(left_ear)

    pr_ear =GOval(20,130,x =333,y= 35)
    pr_ear.filled = True
    pr_ear.fill_color = 'lightpink'
    pr_ear.color ='lightpink'
    window.add(pr_ear)

    pl_ear =GOval(20,130,x =277,y= 35)
    pl_ear.filled = True
    pl_ear.fill_color = 'lightpink'
    pl_ear.color ='lightpink'
    window.add(pl_ear)

    face = GOval(225,200,x = 200,y= 125)
    face.filled = True
    face.fill_color = 'lemonchiffon'
    face.color = 'dimgray'
    window.add(face)

    left_eye =GOval(25,25,x =265,y= 200)
    left_eye.filled = True
    left_eye.fill_color = 'black'
    left_eye.color ='black'
    window.add(left_eye)

    right_eye =GOval(25,25,x =333,y= 200)
    right_eye.filled = True
    right_eye.fill_color = 'black'
    right_eye.color ='black'
    window.add(right_eye)

    left_ball_1 =GOval(10,10,x =272,y= 203)
    left_ball_1 .filled = True
    left_ball_1 .fill_color = 'white'
    left_ball_1 .color ='white'
    window.add(left_ball_1 )

    left_ball_2 =GOval(8,3,x =273,y= 217)
    left_ball_2 .filled = True
    left_ball_2 .fill_color = 'white'
    left_ball_2 .color ='white'
    window.add(left_ball_2)

    right_ball_1 =GOval(10,10,x =340,y= 203)
    right_ball_1 .filled = True
    right_ball_1 .fill_color = 'white'
    right_ball_1 .color ='white'
    window.add(right_ball_1 )

    right_ball_2 =GOval(8,3,x =341,y= 217)
    right_ball_2 .filled = True
    right_ball_2 .fill_color = 'white'
    right_ball_2 .color ='white'
    window.add(right_ball_2)

    left_eyebrow = GArc(70,80,70,130,x =250,y=155)
    window.add(left_eyebrow)

    right_eyebrow = GArc(70,80,340,130,x =328,y=155)
    window.add(right_eyebrow)

    left_blush = GOval(35,25,x =235,y= 220)
    left_blush.filled =True
    left_blush.fill_color = 'lightpink'
    left_blush.color = 'lightpink'
    window.add(left_blush)

    right_blush = GOval(35,25,x =352,y= 220)
    right_blush.filled =True
    right_blush.fill_color = 'lightpink'
    right_blush.color = 'lightpink'
    window.add(right_blush)

    blush_1 = GLabel('/ / /',x =240,y=240)
    window.add(blush_1)
    blush_2 = GLabel('/ / /', x=362, y=240)
    window.add(blush_2)

    mouth = GArc(20,30,210,160,x =292,y=230)
    window.add(mouth)
    mouth_1 = GArc(20,30,210,150,x =308,y=232)
    window.add(mouth_1)
    mouth_1 = GArc(20,30,160,150,x =303,y=242)
    window.add(mouth_1)

    hide = GArc(225,200,80,42,x =257,y=123)
    hide.filled = True
    hide.fill_color = 'lemonchiffon'
    hide.color = 'lemonchiffon'
    window.add(hide)

    hide_1 = GArc(225,200,55,42,x =292,y=123)
    hide_1.filled = True
    hide_1.fill_color = 'lemonchiffon'
    hide_1.color = 'lemonchiffon'
    window.add(hide_1)






if __name__ == '__main__':
    main()
