"""
Implementa un programa en Python que permita registrar y mantener un
seguimiento de los puntajes de un juego. El programa debe permitir a los
jugadores ingresar sus nombres y puntajes, almacenarlos en un
diccionario y proporcionar funcionalidades para mostrar el puntaje más
alto, el promedio de puntajes y la cantidad total de jugadores.

"""




# Base de datos con puntajes
registros={}
continuar = True



# Seguimiento de los puntajes --> Actualizados

while continuar:
    # Pedir al usuario su nombre
    nombre = input("Ingrese nombre del jugador ( o 'salir' para terminar):")
    if nombre.lower() == 'salir':
        continuar = False
    else:
     puntaje = int(input("Ingrese el puntaje del jugador:"))
     registros[nombre] = puntaje


# Obtener puntaje mas alto

jugador_mas_alto = max(registros, key=registros.get)
puntaje_mas_alto = registros[jugador_mas_alto]

print("Puntaje mas algo: ")
print("Jugador:", jugador_mas_alto)
print("Puntaje:", puntaje_mas_alto)

# Obtener el promedio de puntajes
total_puntajes = sum(registros.values())
cantidad_jugadores = len(registros)

promedio = total_puntajes / cantidad_jugadores
print("Promedio de puntajes:", promedio)

# Cantidad total de jugadores
print("La cantidad de jugadores es:", cantidad_jugadores)