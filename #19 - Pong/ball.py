from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_mov = 10
        self.y_mov = 10
        self.velocity = 0.1

    def move(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_mov *= -1
        self.velocity *= 0.9

    def bounce_y(self):
        self.y_mov *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()


