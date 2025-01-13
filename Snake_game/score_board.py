from turtle import Turtle,Screen
ALIGMENT = "center"
FONT = ("Arial",15,"normal")
screen = Screen()

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.shape()
        with open("data.txt") as file:
            content = file.readlines()
            self.high_score = int(content[0])
            self.player_name_original = content[1]        
        self.player_name = screen.textinput(title="Player", prompt="What is your name?")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-10,240)
        self.score_num = 0
        self.write(f"Your Score:{self.score_num}\n Previous high score {self.high_score} acquired by{self.player_name_original}",move=False,align=ALIGMENT,font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Your Score:{self.score_num}\n Previous high score {self.high_score} acquired by{self.player_name_original}",move=False,align=ALIGMENT,font=FONT)
    
    def increse_score(self):
        self.score_num +=1
        self.update_score()

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
                file.write(f"\n {self.player_name}")
        self.score_num = 0
        self.update_score()


  
    