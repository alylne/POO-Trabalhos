class Ponto:

    def __init__(self, x ,y):
        self._x = x
        self._y = y

    def getX(self):
            return self._x
    def getY(self):
            return self._y
    def setX(self, x):
            return self._x
    def setY(self, y):
            return self._x
            
    def qualQuadrante(self, x, y):
            if(x > 0 and y > 0 ):
                return 1
            if(x < 0 and y > 0 ):
                return 2
            if(y < 0 and y < 0 ):
                return 3
            if(y < 0 and y > 0 ):
                return 4
            if(y == 0 and x == 0 ):
                return 0