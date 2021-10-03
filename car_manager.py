from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.creation_position()
        self.car_speed = STARTING_MOVE_DISTANCE

    def creation_position(self):
        self.goto(x=300, y=random.randint(-250, 250))

    def move(self):
        self.forward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
