"""
Eres un gerente de proyectos y necesitas un programa para administrar
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre,
una descripción y un responsable asignado. Implementa un programa en
Python que utilice un diccionario para almacenar la información de las
tareas. El programa debe permitir agregar nuevas tareas, asignar
responsables a las tareas existentes, actualizar las descripciones de las
tareas y mostrar la lista completa de tareas y responsables.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de diccionarios) 

"""
# Diccionario de tareas.
tareas = {}

#  Registrar las tareas
tareas["Tarea1"] = {"nombre": "Fifa", "descripcion": "Nuevo futbol", "responsable": "Alex"}
tareas["Tarea2"] = {"nombre": "KFC", "descripcion": "El mejor pollo", "responsable": "Alejandro"}
tareas["Tarea3"] = {"nombre": "BMW", "descripcion": "El coche nuevo", "responsable": "Alvaro"}

# Agregamos nuevas tareas.

tareas["Tarea4"] = {"nombre": "Samsung", "descripcion": "Telefono nuevo", "responsable": "Roger"}

# Asignar responsables.

tareas["Tarea1"]["responsable"] = "Angel"

# Actualizar las descripciones de las tareas.

tareas["Tarea3"]["descripcion"] = "El coche viejo"

# Mostrar la lista completa de tareas y responsables.


for tarea, info in tareas.items():
    nombre_tarea = info["nombre"]
    info_descripcion = info["descripcion"]
    nombre_responsable = info["responsable"]

    print(f"El nombre de la {tarea} es: {nombre_tarea}")
    print(f"La descripcion: {info_descripcion}")
    print(f"El nombre del responsable: {nombre_responsable}")
    print()

