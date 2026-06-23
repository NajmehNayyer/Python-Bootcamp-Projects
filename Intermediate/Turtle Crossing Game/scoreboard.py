from turtle import Turtle

FONT = ("Ariel", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup(); self.hideturtle()
        self.draw_finish_line()
        self.goto(x=-250, y=300-30)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        """Increase the score."""
        self.level += 1
        with open("level.txt", "w") as data:
            data.write(str(self.level))
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Writes the game over message."""
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=FONT)
        with open("level.txt", "w") as data: data.write(str(1))

    def draw_finish_line(self):
        self.goto(x=200,y=280)
        self.color("red")
        while self.xcor() >= -200:
            self.pendown()
            self.forward(10)
            self.penup()
        self.penup()
        self.color("black")
