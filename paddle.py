from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.distance = 20
        self.penup()
        self.goto(starting_position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)

    def move(self):
        new_y = self.ycor() + self.distance
        self.sety(new_y)

    def change_direction(self):
        self.distance = self.distance * -1

    def hit_wall(self):
        if self.ycor() > 250 or self.ycor() < -250:
            return True
