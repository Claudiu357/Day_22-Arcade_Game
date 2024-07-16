from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 60, "normal"))

    def score_right(self):
        self.p1_score += 1
        self.update_scoreboard()

    def score_left(self):
        self.p2_score += 1
        self.update_scoreboard()

    def draw_line(self):
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        for _ in range(20):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
