def add(*num):
    somatoria = 0
    for i in num:
        somatoria += i
    return somatoria


soma = add(1, 2, 0, 3, 4, 5, 12, 7, 8)
print(soma)


class Carro:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


meu_carro = Carro(make="Toyota", model="Corolla")
print(meu_carro.model)
