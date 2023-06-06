from turtle import *


colors = ["blue", "black", "white"]  # top to bottom
flag_width = 500
flag_height = 200

setup(600, 400)
speed(3)
penup()
forward(250)
left(90)
forward(150)
left(90)
pendown()
for clr in colors:
    color('black')
    begin_fill()
    fillcolor(clr)
    for i in range(2):
        forward(flag_width)
        left(90)
        forward(flag_height/len(colors))
        left(90)
    end_fill()

    penup()
    left(90)
    forward(flag_height / len(colors))
    right(90)
    pendown()

exitonclick()