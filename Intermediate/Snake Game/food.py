from turtle import Turtle
import random

MAX_CORR = 270

def rand_cor(): return random.randint(-MAX_CORR, MAX_CORR)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(rand_cor(), rand_cor())

    def change_loc(self):
        self.goto(rand_cor(), rand_cor())
