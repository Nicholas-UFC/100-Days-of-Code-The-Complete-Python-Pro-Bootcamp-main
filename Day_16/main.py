from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maquina_de_cafe = CoffeeMaker()
caixa = MoneyMachine()

ligado = True

while ligado:
    print("Bem vindo a maquina de café!!!")
    print("\n1 - Gostaria de comprar um café?")
    print("\n2 - Ver o status da maquina")
    print("\n3 - Desligar")

    escolhido = int(input("\nDigite 1,2 ou 3: "))

    if escolhido == 3:
        ligado = False

    elif escolhido == 2:
        print("A maquina atualmente tem: ")
        maquina_de_cafe.report()
        print("\n")
        caixa.report()
        voltar = input("Tecle qualquer botão para voltar!!!")

    else:
        items = menu.get_items()
        pedido = input(f"Digite o que gostaria de pedir: {items}\n")
        tipo_de_cafe = menu.find_drink(pedido)

        if not maquina_de_cafe.is_resource_sufficient(tipo_de_cafe):
            print(
                "Infelizmente não temos ingredientes o suficiente para fazer seu café"
            )
        else:
            if caixa.make_payment(tipo_de_cafe.cost):
                maquina_de_cafe.make_coffee(tipo_de_cafe)
            voltar = input("Tecle qualquer botão para voltar!!!")
