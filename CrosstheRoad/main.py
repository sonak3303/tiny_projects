import time
from turtle import Screen, write

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the Road")
screen.tracer(0)


new_player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(new_player.up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.cars_move()
  
   #collision
    for car in cars.all_cars:
        if car.distance(new_player) < 20:
            game_is_on = False
            score.game_over()


    #the other side
    if new_player.ycor() == 290:
        new_player.refresh()
        cars.cars_speed_up()
        score.update_score()
        

    
        
screen.exitonclick()