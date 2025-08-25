# 1. turtle with 5 hight and 1 width
# 2. turtle will be a ball
# 3. turtle with 5 height and 1 width

import turtle
from pingpongfun import ping_pong_object


screen = turtle.Screen()
screen.setup(800,600)

rod_left = ping_pong_object('square',5,1,90,-300,0)
rod_right = ping_pong_object('square',5,1,90,300,0)
ball = ping_pong_object('circle',1,1,0,100,0)


screen.listen()
screen.onkeypress(rod_left.move_rod_up,'w')
screen.onkeypress(rod_left.move_rod_down,'s')

screen.onkeypress(rod_right.move_rod_up,'Up')
screen.onkeypress(rod_right.move_rod_down,'Down')

global_speed_x = 1
global_speed_y = 1
while True:
    ball.keep_moving(global_speed_x,global_speed_y)
    if ball.t.ycor()>290:
        global_speed_y = -1
    if ball.t.ycor() < -290:
        global_speed_y = 1
        
    if abs(ball.t.xcor()-rod_right.t.xcor())<20 and abs(ball.t.ycor()-rod_right.t.ycor())<50:
        global_speed_x = -1
    if abs(ball.t.xcor()-rod_left.t.xcor())<20 and abs(ball.t.ycor()-rod_left.t.ycor())<50:
        global_speed_x = 1
        
# data types, data structure, conditons, loops and functions, finally classes

    


turtle.done()