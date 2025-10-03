from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        dado = random.randint(1,6)
        if dado == 1:
            novo_carro = Turtle("square")
            novo_carro.shapesize(stretch_wid=1, stretch_len=2)
            novo_carro.penup()
            novo_carro.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            novo_carro.goto(300, random_y)
            self.all_cars.append(novo_carro)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT