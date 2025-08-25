import turtle
class ping_pong_object():
    def __init__(self,shape,width,height,heading,positionx,positiony):
        self.t = turtle.Turtle(shape)
        self.t.penup()
        self.t.shapesize(height,width)
        self.t.setheading(heading)
        self.t.goto(positionx,positiony)
        self.t.penup()
    def move_rod_up(self):
        self.t.forward(10)
    def move_rod_down(self):
        self.t.forward(-10)
    def keep_moving(self,speed_x,speed_y):
        current_x_pos  = self.t.xcor()
        current_y_pos  = self.t.ycor()
        current_x_pos += speed_x
        current_y_pos += speed_y
        self.t.goto(current_x_pos,current_y_pos)