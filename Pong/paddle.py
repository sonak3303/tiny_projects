
from turtle import Turtle
POSITION = [(0,0),(350,0)]
import random

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        # Player_1.speed("fastest")
        self.goto(position)

    def up(self):    
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

