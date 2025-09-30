from clase_celda import Celda

class Pila:
    __cant:int
    __tope:Celda

    def __init__(self):
        self.__tope = None
        self.__cant = 0


    def vacia(self)->bool:
        return (self.__cant == 0)
    
    def insertar(self,x):
        nodo = Celda(x)
        if self.__tope == None:
            nodo.setSiguiente(self.__tope)
            self.__tope = nodo
            self.__cant += 1
    
    def suprimir(self):
        if not self.vacia():
            aux = self.__tope
            dato = self.__tope.getDatos()
            del aux
            self.__cant -= 1
        else:
            print('Pila vacia')
        return dato
    
    def mostrar(self):
        aux = self.__tope
        while aux != None:
            print(aux.getDatos())
            aux = aux.getSiguiente()