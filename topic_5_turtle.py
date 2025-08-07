import turtle 
import funs
t1 = turtle.Turtle('turtle')
t2 = turtle.Turtle('turtle')
t1.color('red')
t2.color('blue')
t1.speed(200)
t2.speed(200)

s1 = 400
s2 = 399
turtle.tracer(0)
while s1 > 0:
    funs.makesquare(t1,s1)
    funs.makesquare(t2,s2)
    s1 = s1 - 2
    s2 = s2 - 2
    turtle.update()





turtle.done()