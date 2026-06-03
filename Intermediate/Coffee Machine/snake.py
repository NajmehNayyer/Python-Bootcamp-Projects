from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
HARDEST_LEVEL = 4
RIGHT = 0; UP = 90; LEFT = 180; DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.speed = MOVE_DISTANCE
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS: self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            ex_seg = self.segments[seg_num-1]
            self.segments[seg_num].goto(ex_seg.xcor(), ex_seg.ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT: self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT: self.head.setheading(LEFT)

    def ask_for_level(self, my_screen):
        game_level = int(my_screen.textinput(title="Game Level",
                                      prompt=f"What level from 1 to {HARDEST_LEVEL} would you like? [Easy to Hard]"))
        if 1 < game_level <= HARDEST_LEVEL:
            self.speed = game_level*5 + MOVE_DISTANCE
