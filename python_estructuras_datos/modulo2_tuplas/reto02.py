# RETO MÓDULO 2 - TUPLAS
# Sistema de Películas

# Definir catalogo como tupla de subtuplas
catalogo = (
    ("Interestelar", "Christopher Nolan", 2014, 9.5),
    ("Titanic", "James Cameron", 1997, 9.0),
    ("El Padrino", "Francis Ford Coppola", 1972, 9.8),
    ("Avatar", "James Cameron", 2009, 8.8)
)

# Recorrer catalogo desempaquetando los cuatro campos
print("===== CATÁLOGO DE PELÍCULAS =====")
for titulo, director, anio, puntuacion in catalogo:
    print(f"Título: {titulo}")
    print(f"Director: {director}")
    print(f"Año: {anio}")
    print(f"Puntuación: {puntuacion}")
    print("-" * 35)

# Usar operador * para separar la primera película del resto
primera_pelicula, *resto_peliculas = catalogo

print("\nPrimera película:")
print(primera_pelicula)

print("\nResto de películas:")
for pelicula in resto_peliculas:
    print(pelicula)


# Buscar películas por director
def buscar_por_director(director):
    coincidencias = tuple(
        pelicula for pelicula in catalogo if pelicula[1] == director
    )
    return coincidencias


# Obtener estadísticas de puntuaciones
def obtener_estadisticas(peliculas):
    puntuaciones = [pelicula[3] for pelicula in peliculas]

    minimo = min(puntuaciones)
    maximo = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)

    return minimo, maximo, promedio


# Buscar por director
resultado = buscar_por_director("James Cameron")

print("\nPelículas de James Cameron:")
for pelicula in resultado:
    print(pelicula)

# Desempaquetar estadísticas
minima, maxima, promedio = obtener_estadisticas(catalogo)

print("\n===== ESTADÍSTICAS =====")
print(f"Puntuación mínima: {minima}")
print(f"Puntuación máxima: {maxima}")
print(f"Promedio: {promedio:.2f}")