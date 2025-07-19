#É possivel fazer operações matematicas no python.
a = 10
b = 5

#Para fazer soma basta usar o sinal de +.
c = a + b
print(c)

#Para fazer subtração basta usar o sinal de -.
c = a - b
print(c)

#Para fazer multiplicação basta usar o sinal de *.
c = a * b
print(c)

#Para fazer divisão basta usar o sinal de /.
c = a/b
print(c)
#Divisão gera um valor do tipo float.
print(type(c))

#Para fazer potenciação basta usar o sinal de**.
c = a**a
print(c)

#A ordem de execução de calculo do python é: PEMDAS(Parentheses, Exponents, Multiplication, Division, Addition, Subtraction).
print(3 * 3 + 3 / 3 - 3)

#Para fazer com que o resultado de uma divisão retorne um valor do tipo int deve ser usado // em vez de só /.
c = a//b
print(c)
print(type(c))

#para simplificar o codigo pode ser usado +=.
score = 0
score = 0+1
print(score)

score += 1
print(score)

score -=1
print(score)
