from turtle import Turtle

FONT = ("Arial", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.xcor(), 270)
        with open("data.txt") as data:
            self.highest_score = int(data.read())

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Your Score: {self.score}, Highest Score: {self.highest_score}", align="center", font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.highest_score + 1))

    def game_over(self):
        self.clear()
        self.color("white")
        self.goto(0, 0)
        self.write(f"Game Over! You scored {self.score} points.", align="center", font=FONT)
