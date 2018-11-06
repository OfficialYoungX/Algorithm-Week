# coding:utf-8
import turtle as t
t.color((0,0,0))
# t.speed(1)
# t.goto(0, -200)
# t.begin_fill()
t.Turtle().screen.delay(0)
def drawDot(x, y):
    raduis = 50
    t.up()
    t.setpos(x,y)
    t.pu()
    t.dot(raduis, 'pink')
    t.up()


def drawText(x, y, str):
    t.up()
    t.setpos(x,y)
    t.pu()
    t.write(str, font = ("Arail", 18))
    t.up()
    
def drawNode(x, y, str):
    drawDot(x, y)
    drawText(x, y, str);

drawNode(100,100,'LOVE')
drawNode(-100,100,'I')

t.hideturtle()

t.done()



