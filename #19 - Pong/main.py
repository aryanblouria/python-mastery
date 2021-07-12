from turtle import Screen
from paddle import Paddle
from ball import Ball
from dotted import Dotted, Scoreboard
import time

sc = Screen()
sc.setup(800, 600)
sc.title("Pong")
sc.bgcolor("black")
sc.tracer(0)

p1 = Paddle((-350, 0))
p2 = Paddle((350, 0))
b = Ball()
dot = Dotted()
sb = Scoreboard()

sc.listen()
sc.onkeypress(p1.up, "w")
sc.onkeypress(p1.down, "s")
sc.onkeypress(p2.up, "Up")
sc.onkeypress(p2.down, "Down")

game_over = False
while not game_over:
    time.sleep(b.velocity)
    sc.update()
    b.move()

    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()

    if (b.xcor() < -320 and b.distance(p1) < 50) or (b.xcor() > 320 and b.distance(p2) < 50):
        b.bounce_x()

    if b.xcor() > 390:
        sb.score1 += 1
        sb.update()
        b.reset_pos()

    if b.xcor() < -390:
        sb.score2 += 1
        sb.update()
        b.reset_pos()

sc.exitonclick()