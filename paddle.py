from turtle import Turtle
import time

class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.goto(coordinate)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        time.sleep(0.0000000001)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
