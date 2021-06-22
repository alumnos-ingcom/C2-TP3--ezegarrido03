################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 4. Comparación de números
 
def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else:
        return 1
    
def prueba():
    numero = input("Ingrese el primer numero")
    otro_numero = input("Ingrese otro numero")
    print(f"Comparacion de numeros\n")
    resultado = compara(numero, otro_numero)
    print(f'Respuesta: {resultado}')
    
if __name__ == "__main__":
    prueba()
