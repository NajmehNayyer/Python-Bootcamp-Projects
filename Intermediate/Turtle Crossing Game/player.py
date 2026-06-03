from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("DeepPink4")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Moves the turtle up by the level distance."""
        self.forward(MOVE_DISTANCE)

    def play_again(self):
        """Puts the turtle at the beginning of the game."""
        self.goto(STARTING_POSITION)

    def reach_the_finish_line(self):
        """Determines if the turtle has reached the finish line."""
        if self.ycor() >= FINISH_LINE_Y: return True
        else: return False
