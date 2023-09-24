"""
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y
una lista de fechas en las que asistió a clases. Implementa un programa
en Python que utilice un diccionario para almacenar la información de las
asistencias. El programa debe permitir registrar la asistencia de los
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de
estudiantes y las fechas en las que asistieron.
(Pista: puedes comenzar con un diccionario vacío y construir un
diccionario de listas)

"""

# Diccionario de asistencia

asistencia = dict()

# Registramos la asistencia

asistencia["Estudiante1"] = ["22-09-2023", "23-09-2023", "24-09-2023"]
asistencia["Estudiante2"] = ["23-10-2023", "24-10-2023", "25-10-2023"]
asistencia["Estudiante3"] = ["22-08-2023", "23-08-2023", "24-08-2023"]


# Agregamos nuevas fechas de las asistencias

asistencia["Estudiante1"].append("25-09-2023")

# Mostramos la lista de estudiantes y las fechas en las que asistieron.

for estudiante, fechas in asistencia.items():
    print("El estudiante:", estudiante)
    print("Asistia en estas fechas:", "/" .join(fechas))
    print()
