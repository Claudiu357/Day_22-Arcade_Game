from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0

    def reset_ball(self):
        self.goto(0, 0)

    def draw_line(self):
        self.penup()
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(20):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
