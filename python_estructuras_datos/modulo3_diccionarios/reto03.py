# RETO MÓDULO 3 - DICCIONARIOS
# Análisis de ventas por región

# Definir ventas_por_region
ventas_por_region = {
    "Norte": {"Q1": 12000, "Q2": 15000, "Q3": 14000, "Q4": 16000},
    "Sur": {"Q1": 10000, "Q2": 11000, "Q3": 13000, "Q4": 12000},
    "Centro": {"Q1": 18000, "Q2": 17000, "Q3": 19000, "Q4": 20000},
    "Occidente": {"Q1": 9000, "Q2": 9500, "Q3": 10500, "Q4": 11000}
}

# Calcular ventas totales por región
totales_region = {}

for region, ventas in ventas_por_region.items():
    totales_region[region] = sum(ventas.values())

# Encontrar la región con mayores ventas
mejor_region = max(totales_region, key=lambda region: totales_region[region])

# Inicializar totales por trimestre
totales_por_trimestre = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0
}

# Acumular ventas por trimestre
for ventas in ventas_por_region.values():
    for trimestre, valor in ventas.items():
        totales_por_trimestre[trimestre] += valor

# Calcular gran total
gran_total = sum(totales_region.values())

# Generar porcentajes por región
porcentajes = {
    region: (total / gran_total) * 100
    for region, total in totales_region.items()
}

# Imprimir reporte ordenado
print("===== REPORTE DE VENTAS =====\n")

print("Ventas totales por región:")
for region, total in sorted(
    totales_region.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(f"{region}: ${total:,} ({porcentajes[region]:.2f}%)")

print("\nRegión con mayores ventas:")
print(f"{mejor_region} con ${totales_region[mejor_region]:,}")

print("\nVentas por trimestre:")
for trimestre, total in totales_por_trimestre.items():
    print(f"{trimestre}: ${total:,}")

print(f"\nGran total anual: ${gran_total:,}")