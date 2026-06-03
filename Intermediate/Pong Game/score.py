from turtle import Turtle
RED = "#A52F58"
BLUE = "#274886"

FONT = ("Courier", 50, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup(); self.hideturtle()
        self.color(BLUE)
        self.goto(-100, 220)
        self.write(f"{self.left_score}", align="center", font=FONT)
        self.color(RED)
        self.goto(100, 220)
        self.write(f"{self.right_score}", align="center", font=FONT)

    def increase_score(self, side):
        if side == "right": self.right_score += 1
        elif side == "left": self.left_score += 1
        self.clear()
        self.color(BLUE)
        self.goto(-100, 220)
        self.write(f"{self.left_score}", align="center", font=FONT)
        self.color(RED)
        self.goto(100, 220)
        self.write(f"{self.right_score}", align="center", font=FONT)
