"""
 Imagina que eres el gerente de recursos humanos de una empresa y
necesitas gestionar la información de los empleados. Cada empleado
tiene un nombre, salario y departamento al que pertenece. Implementa
un programa en Python que permita agregar nuevos empleados,
actualizar el salario de un empleado existente, mostrar la lista completa
de empleados y calcular el promedio salarial por departamento

"""



empleados = {}
continuar = True

while continuar:
    print("Seleccione una de las siguientes opciones")
    print("1. Agregar empleado")
    print("2. Actualizar salario de empleados")
    print("3. Mostrar lista de empleados")
    print("4. Calcular promedio salarial por departamento")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    # Agregar empleado
    if opcion == "1":
        nombre = input("Ingrese nombre del empleado: ")
        salario = float(input("Ingrese salario del empleado: "))
        departamento = input("Ingrese departamento del empleado: ")

        empleados[nombre] = {
            "salario": salario,
            "departamento": departamento
        }

        print("Empleado agregado exitosamente!")
        print(empleados)

    # Actualizar salario de los empleados
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        if nombre in empleados:
            # pedimos nuevo salario
            nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
            # actualizamos salario del empleado
            empleados[nombre]["salario"] = nuevo_salario
            print("Salario actualizado exitosamente!")
        # Si el empleado no existe en la base de datos lo indicamos
        else:
            print("Empleado no encontrado! :(")
    # Mostrar lista de empleados
    elif opcion == "3":
        print("Lista de empleados: ")
        # recorremos pares clave-valor = nombre-datos
        for nombre, datos_empleado in empleados.items():
            salario = datos_empleado["salario"] # Extraemos valor del salario
            departamento = datos_empleado["departamento"] # Extraemos departamento
            print(f"Nombre: {nombre}, Salario: {salario}, Departamento: {departamento}")

    # Calcular promedio salarial por departamento
    elif opcion == "4":
        departamento = input("Ingerese el departamento")

        # Inicializamos variables
        total_salarios = 0
        contador = 0
        # recorremos datos de los empleados guardados en los valores del dict
        for datos_empleado in empleados.values():
            # si el departamento coincide sumamos el salario
            if datos_empleado["departamento"] == departamento:
                total_salarios += datos_empleado["salario"] 
                contador += 1
        # Si hay empleados en el departamento calculamos el promedio
        if contador > 0:
            promedio_salario = total_salarios/contador
            print(f"Promedio salarial del departamento {departamento}: {promedio_salario}")
        # Si no hay empleados en el departamento lo indicamos
        else:
            print(f"No hay empleados en el departamento {departamento}")
    
    elif opcion == "5":
        print("Cerrando programa")
        continuar = False
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")