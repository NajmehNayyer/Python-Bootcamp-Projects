from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

WIDTH = 600; HEIGHT = 600
UPPER_WALL = HEIGHT/2; LOWER_WALL = HEIGHT/2
RIGHT_WALL = WIDTH/2
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Move the turtle up
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars
    car_manager.create_car()
    car_manager.move_car()

    # Car crash
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Reaching the finish line
    if player.reach_the_finish_line() is True:
        scoreboard.increase_score()
        player.play_again()
        car_manager.increase_level_difficulty()

screen.exitonclick()
