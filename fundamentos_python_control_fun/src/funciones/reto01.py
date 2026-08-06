# Reto 1: Calculadora de Métricas del Desarrollador
# Tema: Entrada/Salida, Variables y Conversiones


# Solicita el nombre del desarrollador
nombre = input("Ingrese el nombre del desarrollador: ")

# Solicita la cantidad de proyectos
cantidad_proyectos = int(input("Ingrese la cantidad de proyectos asignados: "))

# Lista para almacenar las horas dedicadas a cada proyecto
horas_proyectos = []

# Recolecta las horas trabajadas en cada proyecto
for i in range(cantidad_proyectos):
    horas = float(input(f"Ingrese las horas del proyecto {i + 1}: "))
    horas_proyectos.append(horas)

# Calcula el total y el promedio de horas
total_horas = sum(horas_proyectos)
promedio = total_horas / cantidad_proyectos

# Muestra el reporte final
print("\n===== REPORTE DE MÉTRICAS =====")
print(f"Desarrollador: {nombre}")
print(f"Total de horas: {total_horas}")
print(f"Promedio de horas por proyecto: {promedio:.2f}")

# Calcula e imprime el porcentaje de cada proyecto
for i, horas in enumerate(horas_proyectos):
    porcentaje = (horas / total_horas) * 100
    print(f"Proyecto {i + 1}: {horas} horas ({porcentaje:.2f}%)")