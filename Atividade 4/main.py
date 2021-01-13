from random import randint

class Sorteio:

    def gerarNumeros(self):
        numeros = []
        for cont in range(0, 6):
            numeros.append(randint(0, 60))
        return numeros
    
    def remove_repetidos(self, lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l


sorteio = Sorteio()
print(sorteio.remove_repetidos(sorteio.gerarNumeros()))
