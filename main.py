from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []

screen.listen()
screen.onkey(player.move, "Up")

loop = 0
game_is_on = True
while game_is_on:
    loop += 1
    time.sleep(0.1)
    screen.update()

    # Create a car every 6 times loop
    if loop % 6 == 0:
        car = CarManager()
        cars.append(car)

        # Detect collision between player and a car
        if player.distance(car) < 20:
            game_is_on = False

        # Detect when player has reach the finish line
        if player.is_stage_win():
            player.next_stage()
            car.increase_car_speed()
            print(car.car_speed) # I have to fix the problem with increase speed

    # move the cars
    for car in cars:
        car.move()

screen.exitonclick()
