from turtle import Turtle


class Dotted(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)
        self.pencolor("white")
        while self.ycor() != -300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 200)
        self.write(self.score2, align="center", font=("Arial", 40, "normal"))

