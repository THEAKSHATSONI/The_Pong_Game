from turtle import Screen
from paddle import Paddle
from boll import Boll
import time
from scoreboard import Scoreborad



screen = Screen()
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

screen.listen()

r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

l_paddle = Paddle((-350, 0))
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

boll = Boll()

scoreboard = Scoreborad()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(boll.move_speed)
    boll.move()

    # Detect Coillison with wall
    if boll.ycor() > 280 or boll.ycor() < -280:
        boll.bounce_y()

    # Detect colloision with paddle
    if boll.distance(r_paddle) < 50 and boll.xcor() >320 or boll.distance(l_paddle) < 50 and boll.xcor() <-320:
        boll.bounce_x()

    # detect a r_paddle misses
    if boll.xcor() > 330 :
        boll.reset_position()
        scoreboard.l_point()

    # detect a l_paddle misses
    if boll.xcor() < -330 :
        boll.reset_position()
        scoreboard.r_point()










screen.exitonclick()
