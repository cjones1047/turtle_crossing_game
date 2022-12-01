from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        random_y = random.randint(-1000, 1000)
        new_car.goto(310, random_y)
        self.all_cars.append(new_car)

    def drive_all_cars(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)
