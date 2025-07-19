#É possivel mudar o tipo de variavel de uma variavel.

#Abaixo vemos um valor inteiro ser transformado e armazenado em a como uma string.
a = str(123)
print(a)

#Abaixo vemos um valor float ser transformado e armazenado em b como um inteiro, os valores depois da virgula do float são jogados fora.
b = int(3.1415)
print(b)

#Abaixo vemos um valor inteiro ser transformado e armazenado em c como um float.
c = float(123)
print(c)

#Para checar o tipo de variavel basta usar a função type().
print(type(c))

print(str(70) + str(100))
print(70 + float("3.1415"))