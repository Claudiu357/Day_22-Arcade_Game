from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.angle = 45
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("blue")
        self.setheading(self.angle)
        self.speed("fastest")

    def move(self):
        self.forward(10)

    def change_direction(self):
        self.angle -= 90
        self.setheading(self.angle)
