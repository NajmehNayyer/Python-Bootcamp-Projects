from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_chance = 1
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a car and puts it in a random position."""
        random_chance = random.randint(1, 6)
        if random_chance == self.car_chance:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_car(self):
        """Moves the car at the speed of that level."""
        for car in self.cars: car.backward(self.car_speed)

    def increase_level_difficulty(self):
        """Increases the level difficulty by increasing the speed of the car."""
        self.car_speed += MOVE_INCREMENT

    def increase_cars(self):
        """Increases the number of cars."""
        levs_to_increase = range(1, 100+1, 5)
        with open("data.txt") as data: current_level = int(data.read())
        if current_level in levs_to_increase: self.car_chance += 1
