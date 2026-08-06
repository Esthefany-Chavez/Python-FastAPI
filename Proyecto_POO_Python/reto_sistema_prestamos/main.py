"""
Script principal: demuestra el flujo completo del Sistema de
Préstamos de Equipos (registro, consulta, préstamo, intento
de préstamo duplicado y devolución).
"""

from sistema_prestamos import SistemaPrestamos

sistema = SistemaPrestamos()

# Registro de equipos
print("--- Registro de equipos ---")
sistema.registrar_equipo("E001", "Portátil Dell", "Computador")
sistema.registrar_equipo("E002", "Videobeam Epson", "Proyector")

# Registro de usuarios
print("\n--- Registro de usuarios ---")
sistema.registrar_usuario("123", "Camila Torres", "camila@correo.com")
sistema.registrar_usuario("456", "Jorge Ríos", "jorge@correo.com")

# Consultar equipos disponibles
print("\n--- Equipos ---")
sistema.consultar_equipos()

# Registrar un préstamo
print("\n--- Registrar préstamo ---")
sistema.registrar_prestamo("E001", "123")

# Consultar préstamos activos
print("\n--- Préstamos activos ---")
sistema.consultar_prestamos_activos()

# Intentar prestar el mismo equipo (debe fallar)
print("\n--- Intento de préstamo duplicado ---")
sistema.registrar_prestamo("E001", "456")

# Devolver el equipo
print("\n--- Devolución ---")
sistema.devolver_equipo(1)

print("\n--- Estado final de equipos ---")
sistema.consultar_equipos()
