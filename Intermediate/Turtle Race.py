from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# Ask for the bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nRed, Orange, Yellow, Green,\nBlue or Purple?")
user_bet.lower(); user_bet.rstrip(); user_bet.lstrip()
if user_bet != 0: race_stat = True

# Create the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -140; turtles = []
for tury in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[tury])
    new_turtle.penup()
    # Put it in the race line
    y = y+40
    new_turtle.goto(x=-230, y=y)
    # Add it to the turtle list
    turtles.append(new_turtle)

while race_stat:

    # Move each turtle by random speed
    for tury in turtles:

        # Determine the winner turtle
        if tury.xcor() >= 230:
            race_stat = False
            winner = tury.pencolor()
            if tury == user_bet: print(f"You've won!")
            else: print(f"You've lost! The {winner} turtle won!")

        tury.forward(random.randint(0, 10))

screen.exitonclick()
