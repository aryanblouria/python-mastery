from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0)
        self.spawn()

    def spawn(self):
        rand_x = random.randint(-350, 350)
        rand_y = random.randint(-350, 350)
        self.goto(rand_x, rand_y)

