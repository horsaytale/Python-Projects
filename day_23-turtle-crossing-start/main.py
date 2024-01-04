import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score=Scoreboard()
user=Player()
car_manager= CarManager()

screen.listen()
screen.onkey(user.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if user.distance(car)<=25:
            game_is_on=False
            score.game_over()

    if user.next_level():
        user.goto((0, -280))
        car_manager.level_up()
        score.increase_level()


screen.exitonclick()