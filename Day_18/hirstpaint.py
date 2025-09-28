from  colorgram import extract
from turtle import Turtle, Screen
from random import choice

cores = extract(r"C:\Python\100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-main\Day_18\images.jpg", 30)

rgb_cores = []
for cor in cores:
    cor_1 = cor.rgb.r
    cor_2 = cor.rgb.g
    cor_3 = cor.rgb.b
    rgb_cores.append((cor_1, cor_2, cor_3))

tela = Screen()
joao = Turtle()
joao.speed("fastest")
joao.penup()
tela.colormode(255)


joao.setheading(225)
joao.forward(250)
joao.setheading(0)

for j in range(10):
    for i in range(10):
        joao.dot(20, choice(rgb_cores))
        joao.forward(50)
    joao.left(90)
    joao.forward(50)
    joao.left(90)
    for i in range(10):
        joao.dot(20, choice(rgb_cores))
        joao.forward(50)
    joao.right(90)
    joao.forward(50)
    joao.right(90)

tela.exitonclick()