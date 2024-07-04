from paddle import Paddle
from turtle import Screen

player1_pos = ((-380, 0), (-380, 20), (-380, -20), (-380, -40))
player2_pos = ((380, 0), (380, 20), (380, -20), (380, -40))
game_is_on = True

screen = Screen()
player1 = Paddle(player1_pos)
player2 = Paddle(player2_pos)

screen.setup(width=800, height=600)
screen.tracer(0)
screen.update()
screen.listen()
while game_is_on:
    screen.onkey(key="w", fun=player1.move_up)
    screen.onkey(key="s", fun=player1.move_down)
    player2.move_along_yaxis()
    screen.update()



screen.exitonclick()