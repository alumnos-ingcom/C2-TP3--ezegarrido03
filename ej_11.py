################
# Ezequiel Gaston Garrido Rivera - @ezegarrido03
# Comision 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# 10. Palíndromo

def es_palindromo(texto):
    texto = texto.lower()         
    texto = texto.replace(" ", "") 
    cantidad_caracteres = len(texto)
    coincidencias = 0
    for i in range(cantidad_caracteres):
        if texto[i] == texto[-i-1]:
            coincidencias +=1
            if coincidencias == cantidad_caracteres:
                return True
        else:
            return False
    
def prueba():
    texto = input('Ingrese una palabra o frase para saber si es palindromo: ')
    print(es_palindromo(texto))
    
if __name__ == "__main__":
    prueba()
