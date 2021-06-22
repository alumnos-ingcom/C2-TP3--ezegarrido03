################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 7. Restas sucesivas

def division_lenta(dividendo, divisor):
    cociente = 0
    
    if divisor == 0:
        raise IngresoIncorrecto("No se puede dividir por cero") 
    
    elif dividendo == 0:
        cociente = 0
        resto = divisor
   
    elif dividendo > 0 and divisor > 0:        
        while dividendo >= divisor:
            dividendo -= divisor
            cociente +=1
        resto = dividendo
    
    elif (dividendo < 0) and (divisor > 0 ): 
        dividendo *= -1
        while dividendo >= divisor:
            dividendo -= divisor
            cociente -=1
        resto = dividendo
    
    elif (divisor < 0) and (dividendo > 0):  
        divisor *= -1
        while dividendo >= divisor:
            dividendo -= divisor
            cociente -=1
        resto = dividendo
    
    else:                                  
        divisor *= -1
        dividendo *= -1
        while dividendo >= divisor:
            dividendo -= divisor
            cociente +=1
        resto = dividendo
    
    print(f'El cociente de la division es: {cociente}')
    print(f'El resto de la division es: {resto}')
    
def prueba():
    dividendo = int( input('Ingrese el dividendo'))
    divisor = int( input('Ingrese el divisor'))
    division_lenta(dividendo, divisor)
    
if __name__ == "__main__":
    prueba()
