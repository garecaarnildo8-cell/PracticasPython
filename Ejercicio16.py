"""
Creá una lista de diccionarios donde cada diccionario represente un estudiante con nombre y promedio. Luego recorrela con un for y mostrá solo los estudiantes que aprobaron (promedio >= 51).
"""

estudiante=[
    {"nombre": "Juan","Promedio":85},
    {"nombre": "Ana","Promedio":45}
]

def mostrar():
    estudiante
    for i in estudiante:
        
        if i["Promedio"]>=51:
            print(f"El estudiante {i['nombre']} con promedio de {i['Promedio']} aprobo la materia")


mostrar()
