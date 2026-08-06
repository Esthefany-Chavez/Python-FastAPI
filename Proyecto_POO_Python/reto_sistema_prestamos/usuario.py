"""
Clase Usuario.

Representa la información básica de una persona
autorizada para solicitar préstamos de equipos.
"""


class Usuario:

    # Constructor de la clase.
    # Guarda la información principal del usuario.
    def __init__(self, documento, nombre, correo):

        # Número de documento del usuario.
        self.documento = documento

        # Nombre completo.
        self.nombre = nombre

        # Correo electrónico.
        self.correo = correo

    # Devuelve una representación en texto del usuario.
    def __str__(self):
        return f"{self.nombre} (Documento: {self.documento})"