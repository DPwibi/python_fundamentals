import turtle
import random

t1 = turtle.Turtle('turtle')
t2 = turtle.Turtle('turtle')
t1.penup()
t2.penup()
t1.color('red')
t2.color('blue')
t1.goto(-300,-100)
t2.goto(-300,100)

running = True
while running == True:
    t1.forward(random.randint(1,10))
    t2.forward(random.randint(1,10))

    if t1.xcor() >300:
        print('red won')
        turtle.write('t1 won',font=('Arial',14,'normal'))
        running = False
    if t2.xcor() >300:
        print('blue won')
        turtle.write('t2 won',font=('Arial',14,'normal'))
        running = False


#[]
# () parathesis or small bracket
# {} curly



turtle.done()