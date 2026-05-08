primer =int(input("Ingrese el numero #1: "))

menor=primer
mayor =primer
suma = primer

for i in range(2,6): 
    segundo = int(input(f"Ingrese el numero #{i}: "))
    suma = suma+segundo
    if segundo<=menor:
        menor=segundo 
    
    if segundo>mayor: 
        mayor=segundo

promedio = suma/5

print("El numero menor es: ",menor)
print("El numero mayor es: ",mayor)
print("El promedio es: ",promedio)


        