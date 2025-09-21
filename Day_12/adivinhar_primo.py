def is_prime(num):
    saida = True
    for i in range(100):
        if i != num and i != 1 and i != 0:
            div = num % i
            if div == 0:
                saida = False
                break

    return saida


num = 4

print(is_prime(num))
