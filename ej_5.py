################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 5. Números positivos y negativos

def signo(numero):
    if numero > 0:
        return '+'
    elif numero < 0:
        return '-'
    else:
        return '='

def prueba():
    print('Numeros positivos y negativos')
    numero = int( input('Ingrese un numero'))
    
    if signo(numero) == '+':
        print('Es positivo')
    elif signo(numero) == '-':
        print('Es negativo')
    else:
        print('Es igual a cero')

if __name__ == "__main__":
    prueba()
