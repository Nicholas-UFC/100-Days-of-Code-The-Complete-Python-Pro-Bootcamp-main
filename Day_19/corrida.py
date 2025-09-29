from turtle import Turtle, Screen
import random
import time

tela = Screen()

tela.setup(width=500, height=400)
aposta = tela.textinput(title="Faça suas apostas", prompt="Qual a cor da tartaruga que vai vencer a corrida? Digite uma cor primaria em ingles e sem errar!: ")

# Criando as tartarugas
joao = Turtle(shape="turtle")
pedro = Turtle(shape="turtle")
maria = Turtle(shape="turtle")

# Posicionando as tartarugas
joao.color("red")
pedro.color("yellow")
maria.color("blue")
joao.penup()
pedro.penup()
maria.penup()
joao.goto(-200, -100)
pedro.goto(-200, 0)
maria.goto(-200, 100)

# Função para a corrida
def corrida(aposta):
    distancia_joao = 0
    distancia_pedro = 0
    distancia_maria = 0
    jogo = True

    while jogo:
        distancia_1 = random.randint(0, 10)
        distancia_2 = random.randint(0, 10)
        distancia_3 = random.randint(0, 10)
        joao.forward(distancia_1)
        pedro.forward(distancia_2)
        maria.forward(distancia_3)
        distancia_joao += distancia_1
        distancia_pedro += distancia_2
        distancia_maria += distancia_3
        time.sleep(0.01)

        if distancia_joao >= 400:
            vencedor = "red"
            print(f"O vencedor é {vencedor}")
            if vencedor == aposta:
                print("Você venceu a aposta!")
            else:
                print("Você perdeu a aposta!")
            
            jogo = False

        elif distancia_pedro >= 400:
            vencedor = "yellow"
            print(f"O vencedor é {vencedor}")
            if vencedor == aposta:
                print("Você venceu a aposta!")
            else:
                print("Você perdeu a aposta!")

            jogo = False

        elif distancia_maria >= 400:
            vencedor = "blue"
            print(f"O vencedor é {vencedor}")
            if vencedor == aposta:
                print("Você venceu a aposta!")
            else:
                print("Você perdeu a aposta!")
            vencedor = "blue"
        
            jogo = False

corrida(aposta)
tela.exitonclick()