
"""
Creá un diccionario que represente un producto de una tienda con: nombre, precio y cantidad en stock.
Luego hacé un programa que:

1-Muestre la información del producto
2-Pregunte cuántas unidades quiere comprar el usuario
3-Verifique si hay suficiente stock
4-Si hay stock, muestre el total a pagar
5-Si no hay stock suficiente, muestre un mensaje de error
"""
Tienda={
    "nombre": "Laptop",
    "precio": 3000,
    "cantidad": 20
}

def informacion():
    print(f"Nombre del producto {Tienda['nombre']}")
    print(f"Precio del producto {Tienda['precio']} bs")
    print(f"Stock del producto {Tienda['cantidad']}")

def pregunta(Total):
    if Total<=Tienda["cantidad"]:
         print(f"El total a pagar es: {Total*Tienda['precio']} bs")
    else:
        print("Error, no hay suficiente stock")    
     
informacion()
opcion=int(input("Cuantas unidades va a comprar: "))

pregunta(opcion)

