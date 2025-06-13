import turtle,random

def draw(x:int,mj:int):
    turtle.setup(1000,1000)
    turtle.title('胡世界奇趣乐园')

    turtle.penup()
    turtle.goto(x,mj)


    turtle.fillcolor('pink')

    turtle.speed(6)


    turtle.begin_fill()
    turtle.pendown()
    turtle.color('pink')
    turtle.pensize(5)
    turtle.left(40)

    turtle.circle(-80,180)
    turtle.forward(132)

    turtle.penup()
    turtle.goto(x,mj)

    turtle.right(40)
    turtle.pendown()
    turtle.right(40)
    turtle.circle(80,180)
    turtle.forward(137)

    turtle.end_fill()
    turtle.penup()





draw(-350,350)
turtle.home()
draw(350,350)
turtle.home()
draw(200,-30)
draw(-350,-200)
turtle.home()

draw(-100,100)
turtle.home()
draw(0,-250)
turtle.home()
draw(100,250)
turtle.home()
draw(-50,450)
turtle.home()





turtle.done()

