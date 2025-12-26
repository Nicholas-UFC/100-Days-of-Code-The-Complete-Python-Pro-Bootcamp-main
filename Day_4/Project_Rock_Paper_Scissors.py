# Projeto que permite criar um jogo onde você e a maquina jogam pedra, papel e tesoura.
import random

Player_1 = int(
    input("Qual você escolhe: 0 para Pedra, 1 para Tesoura e 2 para Papel: ")
)

Player_2 = random.randint(0, 2)

if Player_1 == 0:
    if Player_2 == 0:
        print("Ambos escolheram pedra e deu EMPATE!")
    elif Player_2 == 1:
        print("Você escolheu pedra, a maquina escolheu tesoura, você GANHOU!")
    else:
        print("Você escolheu Pedra e a maquina escolheu papel, você PERDEU!")

elif Player_1 == 1:
    if Player_2 == 0:
        print("Você escolheu tesoura e a maquina escolheu pedra, você PERDEU!")
    elif Player_2 == 1:
        print("Ambos escolheram tesoura e deu EMPATE!")
    else:
        print("Você escolheu tesoura, a maquina escolheu papel, você GANHOU!")

else:
    if Player_2 == 0:
        print("Você escolheu papel e a maquina escolheu pedra, você GANHOU!")
    elif Player_2 == 1:
        print("Você escolheu papel e a maquina escolheu tesoura, você PERDEU!")
    else:
        print("Ambos escolheram papel e deu EMPATE!")
