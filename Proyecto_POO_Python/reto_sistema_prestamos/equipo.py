"""
Clase Equipo.

Representa cada uno de los equipos que pueden prestarse dentro
del sistema.

El estado de disponibilidad se encuentra encapsulado para evitar
que cualquier parte del programa pueda modificarlo directamente.
De esta manera, un equipo solo puede cambiar entre disponible
y prestado utilizando los métodos definidos en esta clase.
"""


class Equipo:

    # Constructor de la clase.
    # Se ejecuta automáticamente al crear un nuevo equipo.
    # Guarda el código, el nombre y el tipo del equipo.
    def __init__(self, codigo, nombre, tipo):

        # Código único que identifica el equipo.
        self.codigo = codigo

        # Nombre del equipo.
        self.nombre = nombre

        # Tipo de equipo (computador, cámara, proyector, etc.).
        self.tipo = tipo

        # Atributo privado.
        # Indica si el equipo está disponible para préstamo.
        # Al crear un equipo, inicialmente estará disponible.
        self.__disponible = True

    # Permite consultar si el equipo está disponible.
    # Al usar @property podemos leer el valor como si fuera
    # un atributo, pero sin modificarlo directamente.
    @property
    def disponible(self):
        return self.__disponible

    # Cambia el estado del equipo a prestado.
    # Se utiliza cuando se registra un préstamo.
    def marcar_prestado(self):
        self.__disponible = False

    # Cambia el estado del equipo a disponible.
    # Se utiliza cuando el equipo es devuelto.
    def marcar_disponible(self):
        self.__disponible = True

    # Devuelve una representación en texto del equipo.
    # Este método se ejecuta automáticamente cuando usamos print().
    def __str__(self):

        estado = "Disponible" if self.__disponible else "Prestado"

        return f"[{self.codigo}] {self.nombre} ({self.tipo}) - {estado}"