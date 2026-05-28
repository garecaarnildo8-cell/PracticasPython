"""
Ahora un ejercicio más para reforzar try/except. Ejercicio18.py:
Hacé una calculadora simple que:

1.Pida dos números al usuario
2.Pregunte qué operación quiere hacer (+, -, *, /)
3.Muestre el resultado
4.Use try/except para manejar:
    -Si el usuario ingresa texto en lugar de números
    -Si el usuario divide entre cero
"""

try: 
    numero=int(input("Ingrese un numero: "))
except: 
    print("Debe ingresar un numero")
    exit()

if numero<=0: 
    print("Ingrese un numero mayor a 0")
    exit()
try: 
    numero2=int(input("Ingrese otro numero: "))
except: 
    print("Debe ingresar un numero")
    exit()


print("------MENU------")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")

opcion=int(input("Opcion: "))

sumar=numero+numero2
if opcion==1: 
    print(f"La suma es {numero+numero2}")

if opcion==2:
    print(f"La resta es {numero-numero2}")

if opcion==3: 
    print(f"La multiplicacion es {numero*numero2}")

if opcion==4: 
    if numero2<=0: 
        print("Error, ingrese un numero positivo")
        exit()
    print(f"La division es {numero/numero2}")