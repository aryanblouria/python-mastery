from turtle import Turtle


class Snake:
    start_pos = [(0, 0), (-20, 0), (-40, 0)]
    segments = []

    def __init__(self):
        for i in range(len(self.start_pos)):
            s = Turtle("square")
            s.color("white")
            s.penup()
            s.goto(self.start_pos[i])
            self.segments.append(s)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto((new_x, new_y))
        self.segments[0].forward(20)

    def w(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def a(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def s(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def d(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def grow(self):
        s = Turtle("square")
        s.color("white")
        s.penup()
        s.goto(self.segments[-1].position())
        self.segments.append(s)


