#Formato condional pode ser feito no python usando if e else.
#Pergunto a altura da pessoa e armazeno.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
Bill = 0

#Faço comparação simples usando if, escrevo if depois a condição. Caso seja verdade, vai ser executado o que está dentro do If, caso seja mentira, vai ser executado o que está dentro do else.
#5 exemplos de comparação que existe são:
# >, significa maior que
# <, significa menor que
# >=, significa maior que ou igual
# <=, significa menor que ou igual
# ==, significa igual  

#É possivel colocar um if dentro de um if, podendo assim adicionar mais de uma condição.
#Elif seria uma segunda condição depois da condição, se A não for verdade, B não for verdade, então execute C, nessa ordem.
if height > 120:
    print("You can ride the rollercoaster!")

    age = int(input("What is your age? "))
    if age < 12:
        Bill = 5
        print("Please pay R$5,00.")
    elif age >= 45 and age <= 55:
        print("Everythin is going to be ok. Have a free ride on us!")
    elif age <= 18:
        Bill = 7
        print("Please pay R$7,00.")
    else:
        Bill = 12
        print("Please pay R$12,00.")

    Wants_photo = str(input("Do you want a photo taken? Y or N: "))
    if Wants_photo == "Y":
        Bill = Bill + 3
    
    print(f"Your final bill is {Bill}")
else:
    print("Sorry, you have to grow taller before you can  ride.")