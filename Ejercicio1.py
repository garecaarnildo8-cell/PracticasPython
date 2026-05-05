manzanas = int(input("Cuantas manzanas tienes? "))
if manzanas<=0: 
    print("Error")
    exit()
come = int(input("Cuantas comes al dia: "))
if come<=0: 
    print("Error")
    exit()
duran=manzanas//come
print("Las manzanas de duran", duran," dias")
