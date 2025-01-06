#Game coponents
#Create components
    #ball
    #player1
    #player2
    #net
    #score
#make them move
#ball moves
#ball interacts with players
#score keep

from turtle import Screen,Turtle
import time
from ball import Ball
from paddle import Paddle
from score_board import Score_board

#make a screen
screen = Screen()
screen.setup(width=800,height=600)   
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
score = Score_board()
ball = Ball()

screen.listen()
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down,"Down")
screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down,"s")




game_on = True
while game_on:
    #refresh the screen 
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
    
    #DETECT COLLISION WITH WALL
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.collision_up() 

    #DETECT COLLISION WITH R_PADDLE
    if ball.distance(paddle_r) < 50 and  ball.xcor() > 320:
        ball.collision_paddle()
   

    if ball.distance(paddle_l) < 50 and  ball.xcor() < -320:
        ball.collision_paddle()
       
    
    #IF ball out of field refresh
    #keep score
    if ball.xcor() >= 400:
        ball.refresh()
        #add point to the left paddle
        score.increse_score_left()

    if ball.xcor() <= -400:
        ball.refresh()
        #add point o the right paddle
        score.increse_score_right()

    if score.score_num_left == 10 or score.score_num_right == 10:
        score.game_over()
      
    
       
      
    
       

screen.exitonclick()

