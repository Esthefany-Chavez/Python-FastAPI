# RETO MÓDULO 4 - CONJUNTOS
# Tiendas y recomendaciones de películas

# Definir las tiendas como conjuntos
tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor"}
tienda_norte = {"Mouse", "Teclado", "Impresora", "Parlantes"}
tienda_sur = {"Laptop", "Monitor", "Cámara", "Impresora"}

# Catálogo completo
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)

# Productos comunes a las tres tiendas
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

# Productos exclusivos de cada tienda
exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivos_norte = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivos_sur = tienda_sur.difference(tienda_centro.union(tienda_norte))

# Verificar si existen tiendas sin productos en común
print("¿Centro y Norte no tienen productos en común?",
      tienda_centro.isdisjoint(tienda_norte))

print("¿Centro y Sur no tienen productos en común?",
      tienda_centro.isdisjoint(tienda_sur))

print("¿Norte y Sur no tienen productos en común?",
      tienda_norte.isdisjoint(tienda_sur))

# Recomendaciones de películas

usuario1 = {"Acción", "Drama", "Ciencia Ficción", "Comedia"}
usuario2 = {"Drama", "Terror", "Acción", "Suspenso"}
usuario3 = {"Comedia", "Animación", "Drama"}

# Géneros comunes entre usuario1 y usuario2
comunes = usuario1 & usuario2

# Todos los géneros favoritos
universo = usuario1 | usuario2 | usuario3

# Géneros exclusivos del usuario1
exclusivos_usuario1 = usuario1 - usuario2

# Diferencias simétricas entre usuario2 y usuario3
diferencias = usuario2 ^ usuario3

# Verificar si los gustos del usuario3 son subconjunto del universo
es_subconjunto = usuario3 <= universo

# Resumen final

print("\n===== RESUMEN TIENDAS =====")
print("Catálogo completo:", catalogo_completo)
print("Productos comunes:", productos_comunes)

print("\nExclusivos Centro:", exclusivos_centro)
print("Exclusivos Norte:", exclusivos_norte)
print("Exclusivos Sur:", exclusivos_sur)

print("\n===== RECOMENDACIONES =====")
print("Géneros comunes Usuario1 y Usuario2:", comunes)
print("Todos los géneros:", universo)
print("Exclusivos Usuario1:", exclusivos_usuario1)
print("Diferencias Usuario2 y Usuario3:", diferencias)
print("¿Usuario3 es subconjunto del universo?:", es_subconjunto)