
Precio = int(input("Cual es el precio del producto que desea llevar: "))

Cantidad = int(input("Cual es la cantidad que desea llevar: "))
Total=Precio*Cantidad
Pregunta = input(("Desea agregar otro producto: "))

while(Pregunta.upper()!="NO" ): 
    Precio = int(input("Cual es el precio del producto que desea llevar: "))
    
    Cantidad = int(input("Cual es la cantidad que desea llevar: "))
    Total=Total+(Precio*Cantidad)
    Pregunta = input(("Desea agregar otro producto: "))

print("Su precio total es: ",Total)


