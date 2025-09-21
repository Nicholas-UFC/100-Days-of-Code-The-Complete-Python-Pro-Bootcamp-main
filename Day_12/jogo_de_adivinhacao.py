import random

def jogo_de_adivinhar():
    numero = random.randint(1, 100)
    print(numero)
    dificuldade = input("Vamos jogar um jogo de adivinhar um numero entre 1 e 100, quer da forma facil ou dificil: ")
    dificuldade = dificuldade.lower()

    if dificuldade == "facil":
        print("Você tem 10 tentativas!")
        tentativas = 10
    else:
        tentativas = 5

    while tentativas > 0:
        chute = int(input("Diga um numero: "))
        if chute == numero:
            print(f"O numero que eu estava pensando era {numero}, você acertou, parabens!!!")
            break
        elif tentativas > 0:
            if chute < numero:
                print("Muito Baixo!")
            else:
                print("Muito Alto!")
            print("Você errou, tente de novo!")
            tentativas -=1
        elif tentativas < 1:
            print("Você perdeu!!!")

jogo_de_adivinhar()