from turtle import Turtle

joao = Turtle()
joao.speed("fastest")

for i in range(360):
    for j in range(30):
        angulo = 360 / (30)
        joao.forward(25)
        joao.left(angulo)
    joao.right(i + 1)
