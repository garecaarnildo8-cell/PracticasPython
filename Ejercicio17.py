try:
    manzanas = int(input("Cuantas manzanas tienes? "))
except:
    print("Error, debe ingresar un numero..")
    exit()
if manzanas<=0: 
    print("Error")
    exit()

try:
    come = int(input("Cuantas comes al dia: "))
except:
    print("Error,debe ingresar un numero")
    exit()
if come<=0: 
    print("Error")
    exit()
duran=manzanas//come
print("Las manzanas de duran", duran," dias")
