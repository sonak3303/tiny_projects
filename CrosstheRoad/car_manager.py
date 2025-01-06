from turtle import Turtle, ycor
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#cars
class CarManager(Turtle):
   
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def create_cars(self):
        random_chance = random.randint(0,6)
        if random_chance == 1 :
            random_y = random.randint(-280,280)
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(290,random_y)
            self.all_cars.append(new_car)
        

    def cars_move(self):
        for n in self.all_cars:
            movement = n.xcor() - self.speed
            n.goto(movement,n.ycor())

    def cars_speed_up(self):
        self.speed += MOVE_INCREMENT