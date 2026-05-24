"""
Creá una función que reciba un número y retorne si es par o impar.
Luego pedí un número al usuario, llamá la función y mostrá el resultado con f-strings.
"""

def determinarParidad(a): 
    if a%2==0:
        return "Es par"
    else: 
        return "Es impar"

numero = int(input("Ingrese un numero: "))

resultado = determinarParidad(numero)

print(f"El numero es : {resultado}")

