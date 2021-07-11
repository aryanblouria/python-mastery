from turtle import Turtle, Screen
import random

sc = Screen()
sc.setup(800, 600)
race_on = False
bet = sc.textinput("Make your bet!", "Which turtle will win the race? Enter a colour: ")
colours = ["red", "blue", "green", "orange", "pink", "yellow"]
y_pos = [-100, -50, 0, 50, 100, 150]
random.shuffle(colours)

turtles = []
for i in range(6):
    t = Turtle("turtle")
    t.penup()
    t.color(colours[i])
    t.goto(-375, y_pos[i])
    turtles.append(t)

if bet:
    race_on = True

while race_on:
    for i in range(6):
        rand_dist = random.randint(0, 10)
        turtles[i].forward(rand_dist)
        if turtles[i].xcor() >= 375:
            winner = turtles[i].pencolor()
            if winner == bet:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")
            race_on = False

sc.exitonclick()