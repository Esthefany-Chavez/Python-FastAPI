# Reto 2: Sistema Simplificado de Calificación e Inventario
# Tema: Condicionales y Listas


# Lista predefinida con el stock de los equipos
stock = [12, 0, 5, 23, 2, 0, 8]

# Listas para almacenar la información solicitada
productos_agotados = []
total_criticos = []

# Contador de productos disponibles
productos_disponibles = 0

print("===== ESTADO DEL INVENTARIO =====")

# Recorrer la lista de stock
for indice, cantidad in enumerate(stock):

    # Clasificar cada producto según su cantidad
    if cantidad == 0:
        estado = "Agotado - Reorden Inmediata"
        productos_agotados.append(indice)

    elif 1 <= cantidad <= 5:
        estado = "Crítico - Reposición Sugerida"
        total_criticos.append(cantidad)
        productos_disponibles += 1

    else:
        estado = "Adecuado"
        productos_disponibles += 1

    # Mostrar el resultado de cada producto
    print(f"Producto {indice}: Stock = {cantidad} --> {estado}")

# Calcular el porcentaje de disponibilidad
porcentaje_disponibilidad = (productos_disponibles / len(stock)) * 100

# Mostrar resultados finales
print("\n===== RESUMEN =====")
print(f"Productos agotados (índices): {productos_agotados}")
print(f"Stock de productos críticos: {total_criticos}")
print(f"Disponibilidad del inventario: {porcentaje_disponibilidad:.2f}%")