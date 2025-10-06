import time
from turtle import Turtle


class Marca(Turtle):
    def __init__(self, estado, x, y):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(x, y)
        self.write(f"{estado}")

    def noexiste(self):
        self.clear()
        self.write("Esse estado não existe!")
        time.sleep(2)
        self.clear()
        self.hideturtle()
