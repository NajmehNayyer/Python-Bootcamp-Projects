from turtle import Turtle
import random

rand_direction = [-10, 10]

class Ball(Turtle):

    def __init__(self):
        """ Initialize the ball object."""
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.x_move = random.choice(rand_direction)
        self.y_move = random.choice(rand_direction)
        self.moving_speed = 0.05

    def move(self):
        """ Ball starts moving at the start of the game.
        Note: This code comes from course solutions."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, axis):
        """ Note: The code for move *= -1 came from course solutions."""
        if axis == "x":
            self.x_move *= -1
            self.y_move *= random.choice(rand_direction)/10
            self.moving_speed *= 0.99
        elif axis == "y":
            self.y_move *= -1

    def shoot_again(self):
        self.goto(0, 0)
        self.bounce("x")
