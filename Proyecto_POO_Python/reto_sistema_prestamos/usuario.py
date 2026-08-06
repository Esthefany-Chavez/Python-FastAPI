"""
Clase Usuario: representa a la persona que solicita un préstamo.
"""


class Usuario:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} (Doc: {self.documento})"
