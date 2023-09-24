# Crea un diccionario vacío llamado “mi_diccionario”.

mi_diccionario = {}

# Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor
# sea tu nombre.

mi_diccionario["nombre"] = "Alejandro"

# Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario". 

print(mi_diccionario["nombre"])

# Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False"
# en caso contrario.

mi_diccionario.get("edad")

# Manera mas facil:
print("edad" in mi_diccionario)

#if "edad" in mi_diccionario:
#    print("True")
#else:
#    print("False")


# Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor:
# "nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia
# favorita.

estudiante = {
    "nombre": "alex",
    "edad": 16,
    "materia": "mates"
}

# Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad
# actual de tu amigo

estudiante["edad"] = 20

print(estudiante)

# Elimina el par clave-valor con la clave "materia" del diccionario “estudiante"

del(estudiante["materia"])

# Imprime todas las claves en el diccionario “estudiante". 

for clave in estudiante.keys():
    print(clave)

#  Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor
# "1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor
# “5555555555”.

agenda = {
    "Juan": "1234567890",
    "Joana": "9876543210",
    "Jimena": "5555555555",
}

# Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor
# “9998887777". 

agenda["Julio"] = "9998887777"

# Imprime el número de entradas (pares clave-valor) en el diccionario “agenda". 

print(len(agenda))

# Crea una lista llamada "claves" que contenga todas las claves del diccionario
# “agenda"


# Mas facil

claves = list(agenda.keys())

#claves = []

# for clave in agenda.values():
#    claves.append(clave)

print(claves)

# Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y
# "False" en caso contrario.

print("Juan" in agenda)

#if "Juan" in agenda:
    #print("True")
#else:
    #print("False")

# Elimina la entrada con la clave “Jimena”. 

del(agenda["Jimena"])

# Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e
# imprime cada par clave-valor en el formato "Nombre: Número”. 

for nombre, numero in agenda.items():
    print(f"{nombre}:{numero}")

# Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el
# diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”.

# valor = agenda.get("Juan")

# O mas facil

valor = agenda.get("Juan", "Clave no encontrada")
print(valor)
#if valor is not None:
#    print(valor)
#else:
#    print("Clave no encontrada")

# Borra todas las entradas del diccionario “agenda”
print(agenda)
agenda.clear()
print(agenda)

