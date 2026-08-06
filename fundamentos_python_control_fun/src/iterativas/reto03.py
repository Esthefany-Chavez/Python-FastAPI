# Reto 3: Motor de Análisis de Frecuencia de Texto
# Tema: Bucles, Cadenas y Diccionarios


# Solicitar al usuario una frase o párrafo
texto = input("Ingrese una frase o un párrafo: ")

# Convertir el texto a minúsculas
texto = texto.lower()

# Eliminar signos de puntuación básicos
for signo in [",", ".", ";", "!"]:
    texto = texto.replace(signo, "")

# Separar el texto en palabras
palabras = texto.split()

# Crear el diccionario de frecuencias
frecuencias = {}

for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

# Buscar la palabra con mayor frecuencia
palabra_frecuente = ""
mayor_frecuencia = 0

for palabra, cantidad in frecuencias.items():
    if cantidad > mayor_frecuencia:
        mayor_frecuencia = cantidad
        palabra_frecuente = palabra

# Mostrar el diccionario de frecuencias
print("\n===== FRECUENCIA DE PALABRAS =====")

for palabra, cantidad in frecuencias.items():
    print(f"{palabra}: {cantidad}")

# Mostrar la palabra más frecuente
print("\n===== RESULTADO =====")
print(f"La palabra más frecuente es '{palabra_frecuente}' con {mayor_frecuencia} apariciones.")