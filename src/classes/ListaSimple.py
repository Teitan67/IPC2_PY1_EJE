class Nodo():
    
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
    
    # Método para agregar elementos en el frente de la linked list
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)  


