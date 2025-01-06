from shutil import move
from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x,random_y)

    def collision_up(self):
        self.y_move *= -1

    def collision_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.collision_paddle()


 