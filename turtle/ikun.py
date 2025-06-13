import turtle
from time import sleep


turtle.setup(800,800)

turtle.title('同心圆')

color = ['green','mjellow','blue','brown']

b = 0
c = 0
p = -1
for i in range(1,5):

    turtle.pensize(3)

    turtle.pendown()
    c += 20
    p += 1
    turtle.pencolor(color[p])
    turtle.circle(c)
    turtle.penup()
    b -= 18
    turtle.goto(0,b)





turtle.done()