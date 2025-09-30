class Celda:
    __dato:object
    __siguiente:object

    def __init__(self,x):
        self.__dato = x
        self.__siguiente = None
    
    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente
    
    def getSiguiente(self):
        return self.__siguiente
    
    def getDatos(self):
        return self.__dato