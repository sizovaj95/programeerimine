from turtle import *


bg_color_name = input("Please type background color (e.g. blue, brown, gold etc): ")
line_color_name = input("Please type line color (e.g. blue, brown, gold etc): ")
line_width = int(input("Please type line width: "))

setup(800, 600)
bgcolor(bg_color_name)
title("Second program")
color(line_color_name)
pensize(line_width)
forward(300)
left(120)
forward(300)

exitonclick()
