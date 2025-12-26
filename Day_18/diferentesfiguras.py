from turtle import Turtle

joao = Turtle()

for i in range(2, 100):
    for j in range(i):
        angulo = 360 / (i)
        joao.forward(25)
        joao.left(angulo)
