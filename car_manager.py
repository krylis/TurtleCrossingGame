from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(position)

    def move(self, move_distance):
        self.back(move_distance)


class CarManager:

    def __init__(self):
        self.cars = []
        self.generate_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Car(position=(300, random.randint(-250, 250)))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.car_speed)
            if car.xcor() < -340:
                self.remove_car(car)

    def remove_car(self, car):
        self.cars.remove(car)
        car.clear()

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

