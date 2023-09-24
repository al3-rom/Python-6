# Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario
# representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos
# valores. Recorre la lista e imprime el nombre y edad de cada estudiante.

estudiantes = [
    {"nombre": "alejandro", "edad": 19},
    {"nombre": "alvaro", "edad": 21}
    ]
for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    edad = estudiante["edad"]
    print("Nombre:", nombre.title(), "Edad:", edad)
print("/////")

# Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las
# mismas claves "nombre" y "edad". Imprime la lista actualizada.

estudiantes.append({"nombre": "alex", "edad": 23})
print(estudiantes)
print("/////")
# .Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada

del(estudiantes[1])
print(estudiantes)
print("/////")

# Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor.
# Imprime la lista actualizada. 

estudiantes[0]["edad"] = 20
print(estudiantes)
print("/////")