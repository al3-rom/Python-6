"""
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias
de tus productos. Cada producto tiene un nombre y una cantidad
vendida. Implementa un programa en Python que utilice un diccionario
para almacenar la información de las ventas. El programa debe permitir
registrar las ventas de productos, actualizar la cantidad vendida de un
producto existente y calcular el total de ventas diarias.
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada
producto)

"""
# Diccionario de ventas
ventas = {}

# Registrar las ventas
ventas["Producto1"] = 10
ventas["Producto2"] = 5
ventas["Producto3"] = 3

# Actualizar cantidad vendida de un producto existente
ventas["Producto2"] += 2

# Total de ventas diarias
total_ventas = sum(ventas.values())

# Imprimir el registro de ventas y el total de ventas diarias

print("Registro de ventas:")
for producto, cantidad in ventas.items():
    print(producto + ":" + str(cantidad))
    
print("Total de ventas diarias:", total_ventas)






