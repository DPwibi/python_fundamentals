import turtle
import random


colors = ["red","blue", "green", "purple",'orange' ]

all_turtles = []
x_pos = -300
y_pos = -200
for color in colors:
    t = turtle.Turtle('turtle')
    t.color(color)
    all_turtles.append(t)
    y_pos = y_pos + 50
    t.goto(x_pos,y_pos)



while True:
    for t in all_turtles:
        t.forward(random.randint(1,10))    
