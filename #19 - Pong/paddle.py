from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, st):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(st)
        self.shapesize(5, 1)

    def up(self):
        y = self.ycor() + 15
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 15
        self.goto(self.xcor(), y)