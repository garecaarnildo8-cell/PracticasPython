"""
Creá un diccionario con los datos de un estudiante: nombre, edad, carrera y promedio. Luego mostrá toda la información con f-strings.
"""
estudiante={
    "nombre": "Juan",
    "edad": "25",
    "carrera": "administracion",
    "Promedio": "85.33"
}

print(f"El nombre del estudiante es {estudiante['nombre']}")
print(f"Su edad es {estudiante['edad']}")
print(f"Carrera que estudia {estudiante['carrera']}")
print(f"Su promedio es {estudiante['Promedio']}")
