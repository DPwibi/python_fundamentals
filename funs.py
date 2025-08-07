def fahrenheit_2_celcius(f):
    c = (f - 32) * 5/9
    return c

def celcius_2_fahrenheit(c):
    f = (c*9/5) +32
    return f


def makesquare(tt,steps):
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)
    tt.forward(steps)
    tt.left(90)




def move_up(local_turtle):
    local_turtle.setheading(90)


def move_left(TT):
    TT.setheading(180)

def move_down(TT):
    TT.setheading(270)

def move_right(TT):
    TT.setheading(0)


