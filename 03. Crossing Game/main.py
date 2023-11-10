import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, 'w')

car_manager_list = []
car_speed = STARTING_MOVE_DISTANCE

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Create a new car object
    if counter % 6 == 0:
        new_car = CarManager()
        new_car.move_speed = car_speed
        car_manager_list.append(new_car)

    # Move every car object created to the left
    for car in car_manager_list:
        car.move()
        # Detect collision with car
        if turtle.distance(car) < 30:
            turtle.reset_position()
            scoreboard.reset_score()
            car_speed = STARTING_MOVE_DISTANCE

    # Remove car object from list when they reach x cor
    for car in car_manager_list:
        if car.xcor() < -320:
            car_manager_list.remove(car)
            car.hideturtle()

    if turtle.ycor() > 250:
        turtle.reset_position()
        scoreboard.score_point()
        car_speed += 2

    screen.update()
    counter += 1
