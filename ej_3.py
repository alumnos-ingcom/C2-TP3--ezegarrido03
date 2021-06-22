################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 3. Conversión de temperaturas

def convertir_a_fahrenheit(centigrados):
    try:
        centigrados = float(centigrados)
    except ValueError as err:
        raise IngresoIncorrecto("No es un numero") from err
    
    fahrenheit = ((centigrados * 9/5) + 32)
    return fahrenheit
    
    
def convertir_a_centigrados(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
    except ValueError as err:
        raise IngresoIncorrecto("No es un numero") from err
    
    centigrados = ((fahrenheit *5/9) - 32)
    centigrados = round(centigrados,2)
    return centigrados
    
def prueba():         

    print(f'Conversion de temperaturas\n')
    
    centigrados = input('Ingrese los grados Centigrados a convertir en Fahrenheit: ')
    fahr = convertir_a_fahrenheit(centigrados)
    print(f'Son {fahr} grados Fahrenheits')
    
    fahrenheit = input('Ingrese los grados Fahrenheit a convertir en Centigrados: ')
    centi = convertir_a_centigrados(fahrenheit)
    print(f'Son {centi} grados Centigrados')    
            
if __name__ == "__main__":
    prueba()
