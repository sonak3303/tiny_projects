STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from token import STAR
from turtle import Turtle


#turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0,new_y)


    def refresh(self):
        self.goto(STARTING_POSITION)
        
    
    