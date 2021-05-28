from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.speed('fastest')
        self.penup()
        self.shapesize(0.75, 0.75)

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.goto(x, y)

    def randomize_location(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)



