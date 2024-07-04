from paddle import Paddle
from turtle import Screen
from ball import Ball
import time


player1_pos = ((-380, 0), (-380, 20), (-380, -20), (-380, -40))
player2_pos = ((380, 0), (380, -20), (380, -40), (380, -60))
game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
player1 = Paddle(player1_pos)
player2 = Paddle(player2_pos)
ball = Ball()

screen.listen()
while game_is_on:
    ball.move()
    screen.onkey(key="w", fun=player1.move_up)
    screen.onkey(key="s", fun=player1.move_down)
    player2.move()
    if player2.hit_wall(player2.segments):
        player2.change_direction()
    if ball.ycor() > 280 or ball.ycor() < -280 or ball.xcor() > 380 or ball.xcor() <= -380:
        ball.change_direction()
    for segment in player1.segments:
        if ball.distance(segment) < 20:
            ball.change_direction()
    for segment in player2.segments:
        if ball.distance(segment) < 20:
            ball.change_direction()
    screen.update()
    time.sleep(0.04)



screen.exitonclick()