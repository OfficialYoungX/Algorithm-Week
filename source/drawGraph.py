# coding:utf-8
import turtle as t
t.speed(0)
t.Turtle().screen.delay(0)
t.setup(1000, 800, 10, 10) # 窗体位置和大小
raduis = 50

def drawDot(x, y):
    t.up()
    t.setpos(x, y)
    t.pu()
    t.dot(raduis, '#10316B')
    t.up()


def drawText(x, y, str,color = 'black'):
    t.color(color)
    t.up()
    t.setpos(x, y)
    t.pu()
    t.write(str, font=("Arail", 18))
    t.up()
    t.color("black")


def drawLine(dot_1=(0, 0), dot_2=(100, 100),color='black'):
    t.color(color)
    t.up()
    t.goto(dot_1[0], dot_1[1])
    t.pd()
    t.goto(dot_2[0], dot_2[1])
    t.up()
    t.color("black")


def drawNode(x, y, str):
    drawDot(x, y)
    drawText(x, y, str, '#ffffff')
