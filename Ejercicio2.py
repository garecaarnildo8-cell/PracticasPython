sueldo = int(input("Cual es sueldo: "))

if sueldo <=0: 
    print("Error el sueldo debe ser mayor a 0.......")
    exit()
gasto = int(input("Cuanto gasta por semana: "))
if gasto<=0 :
    print("Error el gasto no puede ser negativo.....")
    exit()
if gasto>=sueldo: 
    print ("El gasto no puede ser mayor que el sueldo")
    exit()
duracion = sueldo//gasto

print("Los dias que durara su saldo es de: ",duracion)