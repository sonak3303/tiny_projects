from turtle import Turtle
from ball import Ball
from paddle import Paddle
ALIGMENT = "center"
FONT = ("Arial",20,"normal")

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10,270)
        self.score_num_left = 0
        self.score_num_right = 0
        self.write(f"Score: {self.score_num_left} : {self.score_num_right}",move=False,align=ALIGMENT,font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_num_left} : {self.score_num_right}",move=False,align=ALIGMENT,font=FONT)
    
    def increse_score_right(self):
        self.score_num_right +=1
        self.update_score()

    def increse_score_left(self):
        self.score_num_left +=1
        self.update_score()

    def game_over(self):
        if self.score_num_left == 10:
            self.write(f"Left player won",move=False,align=ALIGMENT,font=FONT)

        if self.score_num_right == 10:
            self.write(f"Right player won",move=False,align=ALIGMENT,font=FONT)


        self.goto(0,0)
        self.write(f"GAME OVER",move=False,align=ALIGMENT,font=FONT)
        