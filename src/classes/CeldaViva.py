class CeldaViva:

    x:int
    y:int
    
    def __init__(self,organismo,x,y) -> None:
        self.x=x
        self.y=y
        self.organismo=organismo

    def obtenerPosicion(self,dimensionXdeMatriz)->int:
        return self.x+self.y * dimensionXdeMatriz;