"""
Creá un archivo Ejercicio11.py con una función que reciba dos números y retorne cuál es el mayor. Luego llamá la función con diferentes números y mostrá el resultado con f-strings.
"""
# Ejercicio 11: Función para encontrar el mayor de dos números

def mayor(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return "Los números son iguales"
# Llamando a la función con diferentes números
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el primer número: "))
mayor_numero = mayor(numero1, numero2)

print(f"El número mayor es: {mayor_numero}")

