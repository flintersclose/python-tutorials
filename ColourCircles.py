# Draws circles in a loop

import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red", "green", "blue" , "yellow" , "black" , "orange"]
for x in range(2000):
    t.pencolor(colors[x%6])
    t.circle(2*x)
    t.left(91)









