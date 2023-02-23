from .ListaSimple import Lista_simple

class Muestra:

    dimensionX:int
    dimensionY:int
    listaOrganismos:Lista_simple
    listaCeldasVivas:Lista_simple

    def __init__(self,codigo,descripcion,dimensionX,dimensionY) -> None:
        self.codigo=codigo
        self.descripcion=descripcion
        self.dimensionX=dimensionX
        self.dimensionY=dimensionY
        self.listaOrganismos = Lista_simple()
        self.listaCeldasVivas = Lista_simple()