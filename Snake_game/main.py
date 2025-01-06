
from turtle import Screen, Turtle
import time
import turtle

from snake import Snake
from food import Food
from score_board import Score_Board

#make a screen
screen = Screen()
screen.setup(width=600,height=600)   
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score_Board()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

        
game_on = True

while game_on:
    #refresh the screen 
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increse_score()
        snake.extend()
        #grow
        

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    #Collision with its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


       




screen.exitonclick()