from turtle import Turtle
ALIGMENT = "center"
FONT = ("Arial",15,"normal")


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10,270)
        self.score_num = 0
      
        self.write(f"Score: {self.score_num}",move=False,align=ALIGMENT,font=FONT)

    def update_score(self):
                self.write(f"Score: {self.score_num}",move=False,align=ALIGMENT,font=FONT)
    
    def increse_score(self):
        self.score_num +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",move=False,align=ALIGMENT,font=FONT)


    def reset(self):
        if self.score_num > self.high_score:
             self.high_score = self.score_num

        self.score_num = 0
        self.update_score()


  
    