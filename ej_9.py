################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 9 Numeros primos

def es_primo(numero):
    divisores = 1
    for i in range(1, numero):
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        return True
    else:
        return False
    
def prueba():
    numero = int( input("ingrese un numero para saber si es primo"))
    print(es_primo(numero))
    
if __name__ == "__main__":
    prueba()
