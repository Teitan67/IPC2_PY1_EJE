from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from .Muestra import Muestra
from .Organismo import Organismo
from .CeldaViva import CeldaViva

class Menu:

    muestraAnalizada:Muestra

    def __init__(self) -> None:
        self.opciones=[
            'Abrir muestra',
            'Graficar muestra',
            '----',
            '----',
            '----',
            'Acerca de',
            'Salir'
        ]

    def mostrar(self,error:bool) -> None:
        system("cls")
        
        print('         __________________________           ')
        print('        |        Proyecto 1        |          ')
        print('        |        Muestras          |          ')
        print('        |--------------------------|          \n')

        i = 0

        
        for opcion in self.opciones:
            i = i + 1
            print("\t",i," - "+opcion)
        
        if(error):
            print('\n            OPCION INCORRECTA!!               ')

        opcion = input('\nEscribe tu opcion: ')
        self.ejecutarOpcion(opcion)
        
    
    def pausa(self):
        espera = input('Presiona cualquier tecla para continuar...\n')     
        self.mostrar(False)

    def ejecutarOpcion(self,opcion:str) -> None:
        if(opcion=='1'):
            filename = askopenfilename()
            objetoXml = minidom.parse(filename)
            self.procesarInformacion(objetoXml)
            self.pausa()
        elif(opcion=='2'):
            self.graficarMuestra()
            self.pausa()
        elif(opcion=='6'):
            espera = input('\n\tUSAC - SS2\n\tPractica 1\n\tDesarrollado por Oscar Leon 201709144 (Teitan67)...')
            self.pausa()  
        elif(opcion=='7'):
            pass   
        else:
            self.mostrar()

    def procesarInformacion(self,objetoXML):
 
        coleccionX  = objetoXML.getElementsByTagName('columnas')
        coleccionY  = objetoXML.getElementsByTagName('filas')
        muestra     = objetoXML.getElementsByTagName('muestra')

        codigoMuestra       = muestra[0].childNodes[1].firstChild.data 
        descripcionMuestra  = muestra[0].childNodes[3].firstChild.data 

        dimensionX = coleccionX[0].childNodes[0].data
        dimensionY = coleccionY[0].childNodes[0].data

        nuevaMuestra  =  Muestra(codigoMuestra,descripcionMuestra,dimensionX,dimensionY)

        organismosXML = objetoXML.getElementsByTagName('organismo')

        letra = 65
        for organismo in organismosXML:

            codigo = organismo.childNodes[1].firstChild.data
            nombre = organismo.childNodes[3].firstChild.data
            nuevoOrganismo = Organismo(codigo,nombre,letra)
            nuevaMuestra.listaOrganismos.agregar_al_inicio(nuevoOrganismo)
            letra = letra + 1

        celdasVivasXML = objetoXML.getElementsByTagName('celdaViva')

        for celdaViva in celdasVivasXML:

            fila            = celdaViva.childNodes[1].firstChild.data
            columna         = celdaViva.childNodes[3].firstChild.data
            codigoOrganismo = celdaViva.childNodes[5].firstChild.data

            nuevaCeldaViva  = CeldaViva(codigoOrganismo,columna,fila)

            nuevaMuestra.listaCeldasVivas.agregar_al_inicio(nuevaCeldaViva)

        self.muestraAnalizada = nuevaMuestra

    def graficarMuestra(self):
        
        x   = self.muestraAnalizada.dimensionX
        y   = self.muestraAnalizada.dimensionY

        codigoGraphiz = """
            digraph structs {
                node [shape=record];
                MATRIZ [
                    label="
                    

        """
        cuentaX = -1
        cuentaY = -1
        while (cuentaX < int(x)):
            if(cuentaY == -1):
                codigoGraphiz=codigoGraphiz+'{x,y'
            else:
                codigoGraphiz=codigoGraphiz+'{'+str(cuentaX)
            
            cuentaY = 0
            
            while (cuentaY < int(y)):
                
                if(cuentaX == -1):
                    codigoGraphiz=codigoGraphiz+'|'+str(cuentaY)
                else:
                    listaCeldasVivas  = self.muestraAnalizada.listaCeldasVivas
                    nodoActual = listaCeldasVivas.cabeza

                    codigoOrganismo = ""
                    while nodoActual != None:
                       
                        celdaViva:CeldaViva = nodoActual.dato
                        coordenadaX = celdaViva.x
                        coordenadaY = celdaViva.y
                        
                        if (int(cuentaX)==int(coordenadaX) and int(cuentaY) == int(coordenadaY)):
                            
                            inicio = self.muestraAnalizada.listaOrganismos.cabeza
                            while(inicio!=None):
                                organismo:Organismo = inicio.dato
                                
                                if(celdaViva.organismo==organismo.codigo):
                                    codigoOrganismo='|'+chr(organismo.letra)
                                    break
                                inicio=inicio.siguiente
                            break
                        else:
                            codigoOrganismo='|'
                        nodoActual = nodoActual.siguiente

                    codigoGraphiz = codigoGraphiz + codigoOrganismo
                cuentaY = cuentaY + 1
                
            cuentaX = cuentaX + 1
            
            if(cuentaX == int(x)):
                codigoGraphiz=codigoGraphiz+'}'
            else:
                codigoGraphiz=codigoGraphiz+'}|'

        codigoGraphiz =codigoGraphiz+ """
                        "];
        """
        inicio = self.muestraAnalizada.listaOrganismos.cabeza
        codigoGraphiz =codigoGraphiz+"\""
        while(inicio!=None):
            organismo:Organismo = inicio.dato
            codigoGraphiz =codigoGraphiz +chr(organismo.letra)+"-"+organismo.codigo+"\n"
            inicio=inicio.siguiente
        codigoGraphiz =codigoGraphiz+ """
                        \"}     
        """
        archivo = open("./img/muestra.txt","w")
        archivo.write(codigoGraphiz)
        print("Creando imagen...")
        system("\"D:\\USAC\\2023 Semestre 1\\IPC 2 AUXILIATURA\\Ejemplos Practicos\\[IPC2]Proyecto1_201709144\\src\\img\\generarImagen.bat\"")
        