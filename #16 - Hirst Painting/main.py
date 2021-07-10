import colorgram
import turtle
from turtle import Turtle, Screen
import random

# colors = colorgram.extract("hirst.jpg", 20)
#
# lt = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     col = (r, g, b)
#     lt.append(col)
# print(lt)


def go_to_start():
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.left(180)


turtle.colormode(255)
lt = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]
t = Turtle()
t.shape("classic")
t.speed(0)

t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)

for i in range(10):
    for j in range(10):
        col = random.choice(lt)
        t.dot(20, col)
        t.forward(50)
    go_to_start()

sc = Screen()
sc.exitonclick()

