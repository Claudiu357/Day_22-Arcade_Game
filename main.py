from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time


player1_pos = (-360, 0)
player2_pos = (360, 0)
game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
player1 = Paddle(player1_pos)
player2 = Paddle(player2_pos)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    scoreboard.draw_line()
    ball.move()
    screen.onkey(key="w", fun=player1.move_up)
    screen.onkey(key="s", fun=player1.move_down)
    screen.onkey(key="Up", fun=player2.move_up)
    screen.onkey(key="Down", fun=player2.move_down)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_direction_y()
    if ball.distance(player1) < 50 and ball.xcor() < -340 or ball.distance(player2) < 50 and ball.xcor() > 340:
        ball.change_direction_x()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.score_right()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.score_left()


screen.exitonclick()