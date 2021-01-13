class Quadrilatero():
    
    def __init__(self, P1, P2):
        self.P1 = P1
        self.P2 = P2

    def contidoEmQ(self, a):
        if(a.getX( ) <= self.P2.getX( ) and a.getX( ) >= self.P1.getX( ) and a.getY( ) <= self.P1.getY() and a.getX() >= self.P2.getY()):
            return True
        else:
            return False