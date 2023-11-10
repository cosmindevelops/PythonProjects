from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        random_y = random.randint(-200, 200)
        self.goto(250, random_y)
        self.move_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.move_speed)



