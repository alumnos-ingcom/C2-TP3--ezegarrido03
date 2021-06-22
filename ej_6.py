################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 6. Máximo / Mínimo

def maximo(lista):
    maxx = -99
      
    for item in lista:
        if item > maxx:
            maxx = item
    return maxx


def minimo(lista):
    minimo = 99
    
    for item in lista:
        if item < minimo:
            minimo = item
    return minimo
   
def prueba():
    print('Digite una lista de numeros enteros')
    cantidad_numeros = int( input("¿Cuantos numeros tendra su lista?"))
    
    if cantidad_numeros <= 0:
        raise IngresoIncorrecto("No puede ser menor o igual a 0") 
    
    lista = []
    for i in range(cantidad_numeros):
        n = int( input(f'Ingrese el numero {i+1}/{cantidad_numeros}'))
        lista.append(n)
    
    min_lista = minimo(lista)
    print(f'El minimo de la la lista es: {min_lista}')
    max_lista = maximo(lista)
    print(f'El maximo de la la lista es: {max_lista}')
   
if __name__ == "__main__":
    prueba()
