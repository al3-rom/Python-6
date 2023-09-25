""" 
Supongamos que tienes los resultados de una elección con los nombres
de los candidatos y la cantidad de votos obtenidos por cada uno.
Implementa un programa en Python que permita registrar los votos,
mostrar la lista completa de candidatos y sus votos, encontrar al
candidato ganador (con más votos) y calcular el porcentaje de votos que
obtuvo cada candidato.

"""

resultados = {}
continuar = True

while continuar:
    print("1. Registrar voto ")
    print("2. Mostrar lista de candidatos y votos ")
    print("3. Encontrar candidato ganador ")
    print("4. Calcular porcentaje de votos ")
    print("5. Salir ")
    opcion = input("Seleccione una opcion: ")

    # Registrar voto
    if opcion == "1":
        # pedidmos nombre de candidato
        candidato = input("Ingrese nombre del candidato: ")
        # añadimos voto
        if candidato in resultados:
            resultados[candidato] += 1
            # si no esta en la base de datos añadimos par clave-valor
        else:
            resultados[candidato] = 1
        print("Voto registrado satisfactoriamente")

    # Mostrar lista de candidatos y votos
    elif opcion == "2":
        print("Lista de candidatos y votos: ")
        # recorremos pares clave-valor
        for candidato, votos in resultados.items():
            # imprimimos candidatos-votos
            print(f"Candidato: {candidato}, Votos: {votos}")
    # Encontrar candidato ganador
    elif opcion == "3":
        # Comprobamos si se ha votado ya
        # si no
        if len(resultados) == 0:
            print("No hay candidatos registrados.")
            # si hay votaciones
        else:
         # extraemos la clave asociada al numero de votos mas alto
         ganador = max(resultados, key = resultados.get) 
         print(f"El candidato ganador es: {ganador}")

    # Calculamos el procentaje de votos
    elif opcion == "4":
        total_votos = sum(resultados.values())
        print("Porcentaje de votos por candidato")   
        for candidato, votos in resultados.items():
            porcentaje = (votos/total_votos) * 100
            print(f"Candidato: {candidato}, Porcentaje de votos {porcentaje: .2f}%") # .2f-muestra solo dos decimales

            
    elif opcion == "5":
        print("Cerrando programa")
        continuar = False
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")