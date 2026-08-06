"""
Clase Prestamo: relaciona un Equipo con un Usuario y controla
el estado del préstamo (Activo / Devuelto) de forma encapsulada,
ya que es un dato sensible que no debe modificarse libremente
desde fuera de la clase.
"""

from datetime import date


class Prestamo:
    def __init__(self, id_prestamo, equipo, usuario, fecha_prestamo=None):
        self.id_prestamo = id_prestamo
        self.equipo = equipo
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo or date.today()
        self.fecha_devolucion = None
        self.__estado = "Activo"  # atributo sensible encapsulado

    @property
    def estado(self):
        return self.__estado

    def cerrar_prestamo(self):
        self.__estado = "Devuelto"
        self.fecha_devolucion = date.today()

    def __str__(self):
        return (f"Préstamo #{self.id_prestamo} | Equipo: {self.equipo.nombre} | "
                f"Usuario: {self.usuario.nombre} | Estado: {self.__estado}")
