import turtle

colors = ['red',"blue", "green"]

shape = "turtle"

colour = "red"

turtle.shape(shape)
turtle.color(colour)

steps = 100
angle = 120

for x in range(2):
    for c in colors:
        turtle.color(c)
        turtle.forward(steps)
        turtle.right(angle)



turtle.mainloop()



