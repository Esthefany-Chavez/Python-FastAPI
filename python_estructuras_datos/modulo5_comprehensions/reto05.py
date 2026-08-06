# RETO MÓDULO 5 - COMPREHENSIONS
# Analizador de ventas con las 3 comprehensions

# Definir ventas con 6 productos (producto, unidades, precio, categoria)

ventas = [
    ("Laptop", 5, 250, "Tecnología"),
    ("Mouse", 30, 25, "Tecnología"),
    ("Teclado", 20, 60, "Tecnología"),
    ("Silla", 10, 120, "Muebles"),
    ("Escritorio", 8, 200, "Muebles"),
    ("Cuaderno", 50, 8, "Papelería")
]

# List comprehension: valor total

valor_total = [
    unidades * precio
    for producto, unidades, precio, categoria in ventas
]

print("Valor total por producto:")
print(valor_total)

# List comprehension con filtro

productos_destacados = [
    producto
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
]

print("\nProductos destacados:")
print(productos_destacados)

# Dict comprehension

producto_info = {
    producto: {
        "valor": unidades * precio,
        "unidades": unidades
    }
    for producto, unidades, precio, categoria in ventas
}

print("\nInformación de productos:")
print(producto_info)

# Dict comprehension con filtro

ranking_premium = dict(
    sorted(
        {
            producto: unidades * precio
            for producto, unidades, precio, categoria in ventas
            if precio > 50
        }.items(),
        key=lambda item: item[1],
        reverse=True
    )
)

print("\nRanking Premium:")
print(ranking_premium)

# Set comprehensions

categorias_unicas = {
    categoria
    for producto, unidades, precio, categoria in ventas
}

productos_baratos = {
    producto
    for producto, unidades, precio, categoria in ventas
    if precio <= 50
}

print("\nCategorías únicas:")
print(categorias_unicas)

print("\nProductos baratos:")
print(productos_baratos)

# Combinar las tres comprehensions

resumen_formateado = {
    producto: f"{unidades} unidades - Valor: ${unidades * precio}"
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
}

gran_total = sum(
    unidades * precio
    for producto, unidades, precio, categoria in ventas
)

print("\nResumen formateado:")
for producto, descripcion in resumen_formateado.items():
    print(f"{producto}: {descripcion}")

print(f"\nGran total de ventas: ${gran_total}")