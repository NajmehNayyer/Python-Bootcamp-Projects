from turtle import Screen
from snake import Snake; from food import Food; from scoreboard import Scoreboard
import time

WALL_COR = 290

def game_over():
    game_on = False
    scoreboard.game_over()
    screen.exitonclick()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

ask_for_level = True
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.update()

    # Default movement
    snake.move()

    # Eating the food
    if snake.head.distance(food) < 15:
        scoreboard.reset_scoreboard()
        food.change_loc()
        snake.extend()
        scoreboard.increase_score()

    # Collision with the wall
    if snake.head.xcor() > WALL_COR or snake.head.xcor() < -WALL_COR or snake.head.ycor() > WALL_COR or snake.head.ycor() < -WALL_COR:
        game_over()

    # Collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10: game_over()

screen.exitonclick()
