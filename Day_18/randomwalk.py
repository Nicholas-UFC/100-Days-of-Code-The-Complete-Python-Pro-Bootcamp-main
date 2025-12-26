import random
from turtle import Screen, Turtle

tela = Screen()
tela.colormode(255)
joao = Turtle()
direcoes = [0, 90, 180, 270]
joao.speed("fastest")
joao.pensize(15)

for i in range(1000):
    direcao_aleatoria = random.choice(direcoes)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    cor_aleatoria = (r, g, b)

    joao.left(direcao_aleatoria)
    joao.forward(50)
    joao.color(cor_aleatoria)

tela.exitonclick()
