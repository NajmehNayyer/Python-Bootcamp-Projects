from turtle import Turtle

UP = 90; DOWN = 270
PADDLE_BORDER = 230

class Paddle(Turtle):

    def __init__(self, coordinates, color):
        """ Initialize the Paddle object and take it to its side."""
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates)

    def up(self):
        """ Move the paddle up by 20px."""
        y_up = self.ycor(); current_x = self.xcor()
        if y_up < PADDLE_BORDER: self.goto(current_x, y_up+20)
        else: self.goto(current_x, y_up)

    def down(self):
        """ Move the paddle down by 20px."""
        y_down = self.ycor(); current_x = self.xcor()
        if y_down > -PADDLE_BORDER: self.goto(current_x, y_down-20)
        else: self.goto(current_x, y_down)
