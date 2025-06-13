import time
import turtle


turtle.setup(1000,1000)
turtle.speed(15)

#go位置
turtle.penup()
turtle.goto(-180,120)

#画笔设置
turtle.colormode(255)
turtle.color((255,155,192))
turtle.pendown()
turtle.pensize(5)
#猪鼻孔/left
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(-8)
turtle.end_fill()
turtle.penup()

#猪鼻孔/right
turtle.goto(-150,120)
turtle.pendown()
turtle.begin_fill()
turtle.circle(-8)
turtle.end_fill()





#猪鼻子
turtle.penup()
turtle.goto(-130,125)
turtle.pendown()
turtle.right(70)
for i in range(2):
    turtle.circle(-35, 90)
    turtle.circle(-35, 90)


#大体颜色噢填充
turtle.colormode(255)
turtle.fillcolor((255,192,203))

turtle.begin_fill()


#大体
turtle.penup()
turtle.goto(-143,140)

turtle.left(60)
turtle.pendown()
turtle.forward(150)

for i in range(3):
    turtle.right(2)
    turtle.forward(40)

for mj in range(5):
    turtle.right(2)
    turtle.forward(10)

#大体外框
turtle.circle(-120,250)

turtle.left(63)
turtle.forward(186)

turtle.right(115)
turtle.forward(37)

turtle.left(40)
turtle.forward(20)
turtle.left(4)
turtle.forward(3)
turtle.left(30)
turtle.forward(20)

turtle.end_fill()

#眼眶/1
turtle.fillcolor(   (  255,255,255   )  )
turtle.begin_fill()

turtle.penup()

turtle.goto(60,55)

turtle.pendown()

turtle.circle(30)

turtle.end_fill()

#眼眶/2
turtle.fillcolor(   (  255,255,255   )  )
turtle.begin_fill()


turtle.penup()

turtle.goto(140,40)

turtle.pendown()
turtle.right(150)
turtle.circle(-30)

turtle.end_fill()

#emje/2


turtle.penup()
turtle.goto(110,5)

#emje填充--black
turtle.fillcolor('black')

turtle.begin_fill()
turtle.pendown()
turtle.circle(15)
turtle.end_fill()


#emje/1
turtle.penup()
turtle.goto(15,40)

turtle.fillcolor('black')


turtle.begin_fill()
turtle.pendown()
turtle.circle(15)
turtle.end_fill()


#ear/eft
turtle.penup()
turtle.goto(148,77)
turtle.left(110)

turtle.fillcolor(255,192,203)
turtle.begin_fill()

turtle.pendown()

for lp1 in range(10):
    turtle.right(4)
    turtle.forward(7)

for lo1 in range(9):
    turtle.right(18)
    turtle.forward(5)

for lo1 in range(13):
    turtle.right(0.11)
    turtle.forward(4)
turtle.end_fill()

#ear/right
turtle.penup()
turtle.goto(194,42)
turtle.right(180)

turtle.pendown()
turtle.fillcolor(255,192,203)
turtle.begin_fill()


for lp2 in range(10):
    turtle.right(4)
    turtle.forward(7)

for lo2 in range(9):
    turtle.right(18)
    turtle.forward(5)

for lo2 in range(13):
    turtle.right(0.11)
    turtle.forward(3.5)

turtle.end_fill()





#面部细节
turtle.penup()
turtle.goto(140,-40)
turtle.pendown()


turtle.fillcolor((255,155,191))
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()


#嘴巴
turtle.penup()
turtle.goto(30,-82)

turtle.pencolor('red')

turtle.pendown()
turtle.left(90)

for mj in range(18):
    turtle.left(4.44)
    turtle.forward(5)



#身体
turtle.penup()
turtle.goto(184.5,-138)

turtle.right(65)
turtle.forward(5)

turtle.fillcolor((255,100,100))
turtle.begin_fill()
turtle.pendown()

for t in range(20):
    turtle.right(2)
    turtle.forward(10)


turtle.right(85.6)
turtle.forward(220)


turtle.right(85.6)

for r in range(18):
    turtle.right(1.32)
    turtle.forward(10.5)





turtle.end_fill()

#手臂
turtle.pencolor((255,155,192))
turtle.penup()

turtle.goto(24,-200)
turtle.right(245)

turtle.pendown()
for lm in range(30):
    turtle.left(0.5)
    turtle.forward(2)


#手指/left

turtle.right(90)
for mjmj in range(10):
    turtle.left(0.8)
    turtle.forward(2.3)

turtle.penup()
turtle.backward(25)
turtle.left(90)

turtle.pendown()
turtle.forward(25)

turtle.penup()
turtle.backward(25)

turtle.left(90)
turtle.pendown()
turtle.forward(25)




#脚/left
turtle.penup()

turtle.goto(90,-334)
turtle.right(29)

turtle.pencolor((249,204,204))
turtle.pensize(15)

turtle.pendown()

turtle.forward(50)

turtle.pencolor((0,0,0))
turtle.pensize(24)
turtle.right(85)

turtle.forward(25)



#脚/right

turtle.penup()

turtle.goto(160,-334)
turtle.left(85)


turtle.pencolor((249,204,204))
turtle.pensize(15)


turtle.pendown()

turtle.forward(50)

turtle.pencolor((0,0,0))
turtle.pensize(24)
turtle.right(85)

turtle.forward(25)





#手指/right

turtle.penup()

turtle.goto(220,-200)
turtle.right(180)

turtle.pensize(5)
turtle.pencolor((255,155,192))

turtle.pendown()
for mjmj in range(15):
    turtle.right(0.8)
    turtle.forward(3.8)

turtle.left(85)

for tmj in range(10):
    turtle.right(5)
    turtle.forward(2.5)

turtle.penup()
for po in range(10):
    turtle.left(5)
    turtle.backward(2.5)

turtle.pendown()
turtle.right(85)
turtle.forward(25)

turtle.penup()

turtle.backward(25)

turtle.right(85)
turtle.pendown()

for tmj in range(10):
    turtle.left(5)
    turtle.forward(2.5)

#尾巴
turtle.penup()

turtle.goto(235,-300)

turtle.left(34)

turtle.pendown()

for lpo in range(8):
    turtle.left(2)
    turtle.forward(5)

for mjui in range(13):
    turtle.left(28)
    turtle.forward(6)

for rr in range(10):
    turtle.left(1)
    turtle.forward(5)








turtle.done()