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
screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
