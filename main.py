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

    # create a new car on every 6th loop
    if num_of_loops == 6:
        car_manager.generate_car()
        num_of_loops = 0

    # move cars
    car_manager.move_cars()

    # detect if car collides with player
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    # detect if player gets to other side of road
    if player.at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

scoreboard.game_over()

screen.exitonclick()
