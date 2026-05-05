numero_secreto=7
numero = int(input("Diga un numero y adivine el numero secreto: "))
while numero !=numero_secreto: 
    
    if numero<numero_secreto:
        print("El numero es menor al numero secreto.")
    
    if numero>numero_secreto: 
        print("El numero es mayor al numero secreto.")
        
    numero = int(input("Diga un numero y adivine el numero secreto: "))

if numero==numero_secreto :
        print("Ganaste....")