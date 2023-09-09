from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

num_of_loops = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    num_of_loops += 1

    if num_of_loops == 6:
        car_manager.generate_car()
        num_of_loops = 0

    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.finished():
        player.restart()
        car_manager.increase_speed()
        scoreboard.increase_level()

scoreboard.game_over()

screen.exitonclick()
