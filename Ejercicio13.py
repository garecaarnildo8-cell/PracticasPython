# Ejercicio 13
"""
Creá una función que reciba una lista de números y retorne la suma de todos. Luego pedí números al usuario con un while hasta que ingrese 0, guardalos en una lista y llamá la función.
"""

def suma(numeros):
    resultado=0
    for n in numeros:
        resultado=resultado+n
    return resultado

numeros=[]
numero=int(input("Ingrese un numero: "))
numeros.append(numero)
while numero!=0:
    
    numero=int(input("Ingrese un numero: "))
    if(numero==0):
        break
        
    numeros.append(numero)

print(f"La suma es: {suma(numeros)}")

