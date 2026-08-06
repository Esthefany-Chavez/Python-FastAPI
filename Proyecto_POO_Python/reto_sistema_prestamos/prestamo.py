"""
Clase Prestamo.

Representa el préstamo de un equipo a un usuario.

Esta clase relaciona un objeto de la clase Equipo con un objeto
de la clase Usuario y almacena toda la información del préstamo,
como la fecha en que se realizó, la fecha de devolución y su estado.

El estado del préstamo se encuentra encapsulado para evitar que
pueda modificarse directamente desde fuera de la clase.
"""

# Se importa la clase date del módulo datetime.
# Se utiliza para obtener automáticamente la fecha actual.
from datetime import date


class Prestamo:

    # Constructor de la clase.
    # Se ejecuta automáticamente al crear un nuevo préstamo.
    def __init__(self, id_prestamo, equipo, usuario, fecha_prestamo=None):

        # Identificador único del préstamo.
        self.id_prestamo = id_prestamo

        # Objeto de la clase Equipo que será prestado.
        self.equipo = equipo

        # Objeto de la clase Usuario que solicita el préstamo.
        self.usuario = usuario

        # Si no se envía una fecha, automáticamente
        # se registra la fecha del día actual.
        self.fecha_prestamo = fecha_prestamo or date.today()

        # Al crear el préstamo todavía no existe una fecha
        # de devolución, por eso inicialmente vale None.
        self.fecha_devolucion = None

        # __estado es un atributo privado.
        # Solo la clase puede cambiar su valor.
        # Todo préstamo inicia con estado "Activo".
        self.__estado = "Activo"

    # Permite consultar el estado del préstamo.
    # Gracias a @property podemos leer el estado,
    # pero no modificarlo directamente.
    @property
    def estado(self):
        return self.__estado

    # Método encargado de finalizar el préstamo.
    # Cambia el estado a "Devuelto" y registra
    # automáticamente la fecha de devolución.
    def cerrar_prestamo(self):

        self.__estado = "Devuelto"

        self.fecha_devolucion = date.today()

    # Devuelve una representación en texto del préstamo.
    # Este método se ejecuta automáticamente cuando usamos print().
    def __str__(self):

        return (
            f"Préstamo #{self.id_prestamo} | "
            f"Equipo: {self.equipo.nombre} | "
            f"Usuario: {self.usuario.nombre} | "
            f"Estado: {self.__estado}"
        )