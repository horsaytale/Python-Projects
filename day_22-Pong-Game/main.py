from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle=Paddle((-370,0))
r_paddle=Paddle((370,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()

    if ball.xcor()>380:
        scoreboard.clear()
        scoreboard.l_score+=1
        scoreboard.update_score()
        ball.home()
        ball.bounce_x()
        
    if ball.xcor()<-380:
        scoreboard.clear()
        scoreboard.r_score+=1
        scoreboard.update_score()
        ball.home()
        ball.bounce_x()

    screen.update()

screen.exitonclick()