# Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada
# representa un producto y tiene a su vez las claves "nombre" y "precio" con sus
# respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada
# producto.

productos = {
    "Mango":{
        "nombre": "mango", "precio": 28
    },
    "Banana":{
        "nombre": "banana", "precio": 14
    },
}

for nombre,precio in productos.items():
    full_nombre = precio.get("nombre")
    full_precio = precio.get("precio")

    print(f"El nombre del producto es: {full_nombre.title()} y el precio: {full_precio}")

# Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y
# valor. Imprime el diccionario actualizado.

productos["Manzana"] = {"nombre": "manzana", "precio": 11}
print(productos)

# Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada
# representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus
# respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de
# los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de
# jugadores

equipos = {
    "Equipo1":{
        "nombre": "Fox1", "jugadores": ["Ivan", "Alex","Alvaro"]
    },

    "Equipo2":{
        "nombre": "Fox2", "jugadores": ["Sasha", "Roger","Danco"]
    },

    "Equipo3":{
        "nombre": "Fox3", "jugadores": ["Nikita", "Limber","Julio"]
    }
}

for equipo, nombre in equipos.items():
    titulo_equipo = nombre.get("nombre")
    titulo_jugadores = nombre.get("jugadores")

    print(f"El nobmre del equipo es: {titulo_equipo} y los jugadores son {titulo_jugadores}")

# Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor.
# La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario
# actualizado.

equipos["Equipo4"] = {"nombre": "Fox4", "jugadores": ["Juan", "Angel","Candela"]}

print(equipos)

# Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario
# "equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado.

equipos["Equipo1"]["jugadores"][0] = "Lera"

equipos["Equipo2"]["jugadores"].append("Tania")

print(equipos)