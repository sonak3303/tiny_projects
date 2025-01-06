from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.score_num = 1
    

    def add_score(self):
        self.clear()
        self.write(f" Level: {self.score_num}",move=False,align=ALIGMENT,font=FONT)
      
    def update_score(self):
        self.score_num += 1
        self.add_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",move=False,align=ALIGMENT,font=FONT)