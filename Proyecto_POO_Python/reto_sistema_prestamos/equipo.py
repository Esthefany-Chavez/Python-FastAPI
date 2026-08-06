"""
Clase Equipo: representa un equipo disponible para préstamo.
El atributo 'disponible' está encapsulado porque es sensible:
solo debe cambiar a través de las operaciones controladas del sistema.
"""


class Equipo:
    def __init__(self, codigo, nombre, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.__disponible = True  # atributo sensible encapsulado

    @property
    def disponible(self):
        return self.__disponible

    def marcar_prestado(self):
        self.__disponible = False

    def marcar_disponible(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"[{self.codigo}] {self.nombre} ({self.tipo}) - {estado}"
