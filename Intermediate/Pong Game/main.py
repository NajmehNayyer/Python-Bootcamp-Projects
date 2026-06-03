from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from score import Score
import time

RIGHT_COR = (373, 0)
LEFT_COR = (-380, 0)
WIDTH = 800; HEIGHT = 600; WALL_DIF = 15
RIGHT_WALL = WIDTH/2-WALL_DIF
LEFT_WALL = -RIGHT_WALL
UPPER_WALL = HEIGHT/2-WALL_DIF
LOWER_WALL = -UPPER_WALL

# Create the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("#D1E5EB")
screen.title("Pong Game")
screen.tracer(0)

# Central line
center_line = Turtle()
center_line.color("black")
center_line.penup()
center_line.goto(0, UPPER_WALL)
center_line.setheading(270)
center_line.pensize(2)
center_line.pendown()
center_line.goto(0, LOWER_WALL)
center_line.hideturtle()

# Create the objects
right_paddle = Paddle(RIGHT_COR, "#A52F58")
left_paddle = Paddle(LEFT_COR, "#274886")
ball = Ball()
score = Score()

# Create moving keys for the paddles
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# Start the game
game_on = True
while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall and bounce
    if UPPER_WALL < ball.ycor() or LOWER_WALL > ball.ycor(): ball.bounce("y")

    # Detect collision with a paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350: ball.bounce("x")
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -350: ball.bounce("x")

    # Detect when a paddle misses
    if RIGHT_WALL < ball.xcor():
        score.increase_score("left")
        ball.shoot_again()
    elif LEFT_WALL > ball.xcor():
        score.increase_score("right")
        ball.shoot_again()

    # End the game when someone reaches 12
    if score.left_score == 12 or score.right_score == 12:
        game_on = False
        ball.clear()

screen.exitonclick()
