#Python tem a biblioteca Random, onde existe ferramentas que serve para devolver valores pseudos aleatorios.
#Não tem como o computador executar valores realmente aleatorios.
#Usando a função import, podemos chamar uma biblioteca para que suas ferramentas estejam disponiveis para ser executadas.
import random
import My_module

#A função random.randint me devolve um valor aleatorio entre os intervalos A e B definidos pela função random.randint(A, B).
random_integer = random.randint(1, 10)
print(random_integer)

#Mesmo não criando um valor pi, criei em My_module, posso chamar esse valor pi apenas usando a função My_module.py.
print(My_module.pi)

#Enquanto a função random.randint retorna um valor int, a função random.random retorna um valor aleatorio float entre 0 e 1.
random_float = random.random()
print(random_float)

#Caso eu queira que gere um valor aleatorio entre 0 e 10, basta multiplicar por 10.
random_float = random.random() * 10
print(random_float)