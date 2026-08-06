# RETO MÓDULO 1 - LISTAS
# Gestión de Inventario

# Definir inventario con tres productos [nombre, cantidad, precio]
inventario = [
    ["Laptop", 10, 2500000],
    ["Mouse", 30, 50000],
    ["Teclado", 20, 120000]
]


# Actualizar el precio de un producto
def actualizar_precio(producto, nuevo_precio):
    for item in inventario:
        if item[0] == producto:
            item[2] = nuevo_precio
            print(f"Precio de {producto} actualizado a ${nuevo_precio}")
            return
    print("Producto no encontrado.")


# Registrar una venta
def registrar_venta(producto, cantidad):
    for item in inventario:
        if item[0] == producto:
            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta realizada: {cantidad} unidades de {producto}")
            else:
                print(f"No hay suficiente stock de {producto}")
            return
    print("Producto no encontrado.")


# Añadir un producto o actualizar el stock si ya existe
def anadir_producto(producto, cantidad, precio):
    for item in inventario:
        if item[0] == producto:
            item[1] += cantidad
            item[2] = precio
            print(f"Stock actualizado para {producto}")
            return

    inventario.append([producto, cantidad, precio])
    print(f"Producto {producto} agregado al inventario.")


# Mostrar inventario
def mostrar_inventario():
    print("\n===== INVENTARIO =====")
    for producto in inventario:
        print(
            f"Producto: {producto[0]} | "
            f"Cantidad: {producto[1]} | "
            f"Precio: ${producto[2]:,}"
        )


# Pruebas 

# Actualizar precio del segundo producto
actualizar_precio("Mouse", 55000)

# Registrar venta del primer producto
registrar_venta("Laptop", 3)

# Añadir un producto nuevo
anadir_producto("Monitor", 8, 780000)

# Mostrar inventario final
mostrar_inventario()