from funcoes import fazer_cafe, pedir_moedas
from menu import MENU, recursos

ligado = True

print("")
while ligado:
    print("Bem vindo a maquina de café!!!")
    print("\n1 - Gostaria de comprar um café espresso?")
    print("\n2 - Gostaria de comprar um café latte?")
    print("\n3 - Gostaria de comprar um café caputino?")
    print("\n4 - Ver o status da maquina")
    print("\n5 - Desligar")

    escolhido = int(input("\nDigite 1,2,3,4 ou 5: "))

    if escolhido == 5:
        ligado = False

    elif escolhido == 4:
        print("A maquina atualmente tem: ")
        print(f"\nAgua: {recursos["agua"]}")
        print(f"\nLeite: {recursos["leite"]}")
        print(f"\nCafé: {recursos["cafe"]}")
        print("\n")
        voltar = input("Tecle qualquer botão para voltar!!!")

    else:
        dinheiro = pedir_moedas()
        fazer_cafe(dinheiro, MENU, recursos, escolhido)
