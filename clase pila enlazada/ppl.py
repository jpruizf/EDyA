from clase_pila import Pila

def test():
    p = Pila()
    x = [3]
    x = int(input('Insertar un numero->'))
    i = 0
    while x != 0:
        p.insertar(x)
        x = int(input('Insertar un numero->'))
        i += 1
    valor = p.suprimir()
    print(f'se suprimio el numero {valor}')
    p.mostrar()







if __name__ == '__main__':
    test()