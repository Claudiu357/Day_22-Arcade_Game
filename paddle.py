from turtle import Turtle


class Paddle:
    def __init__(self, starting_position):
        self.segments = []
        for position in starting_position:
            new_seg = Turtle(shape="square")
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)

    def move_up(self):
        for seg in self.segments:
            new_y = seg.ycor() + 20
            seg.sety(new_y)

    def move_down(self):
        for seg in self.segments:
            new_y = seg.ycor() - 20
            seg.sety(new_y)