import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=turtle.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.drive_all_cars()

    # Detect collision between turtle and car
    if car_manager.collision(turtle):
        scoreboard.game_over()
        game_is_on = False

    # Detect passed level
    if turtle.ycor() > turtle.finish_line_y:
        turtle.set_starting_position()
        scoreboard.level_up()
        car_manager.move_increment += 5

screen.exitonclick()
