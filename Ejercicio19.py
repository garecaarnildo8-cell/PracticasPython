"""
Hacé un programa que:

1-Pida el nombre y promedio de un estudiante
2-Guarde esa información en un archivo estudiantes.txt
3-Luego lea el archivo y muestre el contenido
"""
#Clasico 
"""
nombre=input("Ingrese el nombre del estudiante: ")
try:
    promedio=float(input("Cual es su promedio: "))
except: 
    print("Ingrese un promedio valido")

archivo = open("estudiantes.txt","w")
archivo.write(f"Nombre: {nombre}, Promedio {promedio}")
archivo.close()


archivo=open("estudiantes.txt","r")

contenido=archivo.read()
archivo.close()

print(contenido)
"""
#Crear y leer archivo optimizado

nombre=input("Ingrese el nombre del estudiante: ")
try:
    promedio=float(input("Cual es su promedio: "))
except: 
    print("Ingrese un promedio valido")

with open("estudiantes.txt", "w") as archivo: 
    archivo.write(f"Nombbre: {nombre} Promedio: {promedio}")

with open("estudiantes.txt","r") as archivo: 
    contenido=archivo.read()
    print(contenido)
