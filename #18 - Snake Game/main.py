from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(800, 800)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

s = Snake()
f = Food()
sb = Scoreboard()

sc.listen()
sc.onkeypress(s.w, "w")
sc.onkeypress(s.a, "a")
sc.onkeypress(s.s, "s")
sc.onkeypress(s.d, "d")

game_over = False
while not game_over:
    sc.update()
    time.sleep(0.1)
    s.move()

    if s.segments[0].distance(f) < 15:
        s.grow()
        sb.increment()
        f.spawn()

    if s.segments[0].xcor() > 380 or s.segments[0].xcor() < -380 or \
            s.segments[0].ycor() > 380 or s.segments[0].ycor() < -380:
        game_over = True
        sb.game_over()

    for segment in s.segments[1:]:
        if s.segments[0].distance(segment) < 10:
            game_over = True
            sb.game_over()

sc.exitonclick()
