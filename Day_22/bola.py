from turtle import Turtle
import random


class Bola(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def movendo(self):
        novo_x = self.xcor() + self.move_x
        novo_y = self.ycor() + self.move_y
        self.goto(novo_x, novo_y)

    def colicao_y(self):
        self.move_y *= -1

    def colicao_x(self):
        self.move_x *= -1
        self.move_speed *= 0.5

    def reset_posicao(self):
        self.move_speed = 0.1
        self.goto(0,0)