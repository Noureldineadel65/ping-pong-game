from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
paddle_right = Paddle((350, 240))
paddle_left = Paddle((-350, 0))
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.listen()
game_on = True
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
SPEED = 0.1
while game_on:
    time.sleep(SPEED)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        SPEED -= 0.01
    if ball.xcor() > 380:
        scoreboard.increase_left()
        ball.reset()
    if ball.xcor() < -380:
        scoreboard.increase_right()
        ball.reset()

screen.exitonclick()