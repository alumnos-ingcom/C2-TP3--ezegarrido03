################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 2. suma lenta

from tp4_ej1 import ingreso_entero

def suma_lenta(numeroUno, numeroDos):
    
    limite = numeroDos
    if numeroDos < 0:
        limite *= -1
        
    for i in range(limite):
        if numeroDos < 0:
            resultado = numeroUno - i-1
            print(f'{numeroUno-i} + (-1) = {resultado}')
        else:
            resultado = numeroUno + i-1
            print(f'{numeroUno+i} + 1 = {resultado}')
        return resultado
    
def prueba():
    print("ingrese 2 numeros para ser sumados")
    numeroUno = ingreso_entero("ingrese un numero")
    numeroDos = ingreso_entero("ingrese otro numero")
    Resultado = suma_lenta(numeroUno, numeroDos)
    
    
if __name__ == "__main__":
    prueba()
