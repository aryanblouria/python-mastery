from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 375)
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.clear()
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 16, "normal"))
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "normal"))
