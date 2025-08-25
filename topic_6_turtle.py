import turtle

class My_turtle:
    def __init__(self,color,pox,poy):
        self.tt = turtle.Turtle()
        self.tt.shape('turtle')
        self.tt.penup()
        self.tt.shapesize(5,5)
        self.tt.color(color)
        self.tt.goto(pox,poy)
    

t1 = My_turtle('red',-300,0)
t2 = My_turtle('blue',-300,100)
t3 = My_turtle('green',-300,-100)#




turtle.done()