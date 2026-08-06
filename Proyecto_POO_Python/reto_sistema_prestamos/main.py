"""
Script principal del Sistema de Préstamos de Equipos.

Este archivo se encarga de ejecutar el programa y mostrar
el funcionamiento completo del sistema.

Aquí se registran equipos y usuarios, se realiza un préstamo,
se intenta prestar nuevamente un equipo que ya está ocupado
y finalmente se devuelve para comprobar que vuelve a quedar
disponible.
"""

# Se importa la clase SistemaPrestamos.
# Esta clase contiene toda la lógica del sistema.
from sistema_prestamos import SistemaPrestamos


# Se crea un objeto de la clase SistemaPrestamos.
# Este objeto será el encargado de administrar
# los equipos, usuarios y préstamos.
sistema = SistemaPrestamos()



# Registro de equipos
print("--- Registro de equipos ---")

# Se registran dos equipos diferentes.
# Cada equipo queda almacenado dentro del sistema.
sistema.registrar_equipo("E001", "Portátil Dell", "Computador")
sistema.registrar_equipo("E002", "Videobeam Epson", "Proyector")



# Registro de usuarios

print("\n--- Registro de usuarios ---")

# Se registran las personas que podrán solicitar
# préstamos de equipos.
sistema.registrar_usuario("123", "Camila Torres", "camila@correo.com")
sistema.registrar_usuario("456", "Jorge Ríos", "jorge@correo.com")



# Consulta de equipos

print("\n--- Equipos registrados ---")

# Se muestran todos los equipos registrados
# y su estado actual (Disponible o Prestado).
sistema.consultar_equipos()



# Registrar un préstamo

print("\n--- Registrar préstamo ---")

# El usuario con documento 123 solicita
# el equipo identificado con el código E001.
sistema.registrar_prestamo("E001", "123")



# Consultar préstamos activos

print("\n--- Préstamos activos ---")

# Se muestran únicamente los préstamos
# que todavía no han sido devueltos.
sistema.consultar_prestamos_activos()



# Intentar prestar nuevamente el mismo equipo

print("\n--- Intento de préstamo duplicado ---")

# Como el equipo ya fue prestado,
# el sistema debe impedir realizar otro préstamo.
sistema.registrar_prestamo("E001", "456")



# Devolución del equipo

print("\n--- Devolución del equipo ---")

# Se devuelve el préstamo cuyo identificador es 1.
# El equipo vuelve a quedar disponible.
sistema.devolver_equipo(1)



# Estado final del sistema

print("\n--- Estado final de los equipos ---")

# Se muestran nuevamente los equipos para comprobar
# que el equipo devuelto ya aparece disponible.
sistema.consultar_equipos()