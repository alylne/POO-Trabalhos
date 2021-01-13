from Ponto import Ponto
from Quadrilatero import Quadrilatero

if __name__ == '__main__':
    p1 = Ponto(2, 4)
    p2 = Ponto(4, 2)
    quadri = Quadrilatero(p1, p2)
    print(quadri.contidoEmQ(p1))
    print(quadri.contidoEmQ(p2))