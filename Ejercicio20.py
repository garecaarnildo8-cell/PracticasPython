"""
Hacé un programa que:

1-Permita agregar varios estudiantes con nombre y promedio
2-Cada estudiante se guarda en el archivo sin borrar los anteriores (hint: modo "a")
3-Al final muestre todos los estudiantes guardados

"""

nombre=input("Ingrese el nombre del estudiante: ")

try: 
    promedio=float(input("Introduzca su promedio: "))
except: 
    print("Ingrese un numero valido...")

with open("Lista.txt","a") as archivo: 
        archivo.write(f";Nombre: {nombre}, Promedio: {promedio}\n")

opcion=input("¿Desea agregar otro estudiante?: ")
opcion=opcion.upper()
while opcion!="NO": 
    
    with open("Lista.txt","a") as archivo: 
        archivo.write(f";Nombre: {nombre}, Promedio: {promedio}\n")
    
    nombre=input("Ingrese el nombre del estudiante: ")
    try: 
        promedio=float(input("Introduzca su promedio: "))
    except: 
        print("Ingrese un numero valido...")
    
    with open("Lista.txt","a") as archivo: 
        archivo.write(f";Nombre: {nombre}, Promedio: {promedio}\n")
    
    opcion=input("¿Desea agregar otro estudiante?: ")
    opcion=opcion.upper()

with open("Lista.txt","r") as archivo: 
    contenido=archivo.read()
    print(contenido)


