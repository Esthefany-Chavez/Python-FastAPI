from app.usuarios.validaciones import (
    validar_nombre,
    validar_edad,
    validar_correo,
    validar_rol
)


class GestorUsuarios:
    """Administra las operaciones relacionadas con los usuarios."""

    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, edad, correo, rol):
        """Valida y registra un nuevo usuario."""

        nombre = validar_nombre(nombre)
        edad = validar_edad(edad)
        correo = validar_correo(correo)
        rol = validar_rol(rol)

        if any(usuario["correo"] == correo for usuario in self.usuarios):
            raise ValueError("Ya existe un usuario registrado con ese correo.")

        nuevo_usuario = {
            "nombre": nombre,
            "edad": edad,
            "correo": correo,
            "rol": rol
        }

        self.usuarios.append(nuevo_usuario)

    def listar_usuarios(self):
        """Devuelve la lista completa de usuarios."""
        return self.usuarios

    def buscar_usuario(self, nombre):
        """Busca usuarios cuyo nombre coincida parcialmente."""
        if not nombre:
            raise ValueError("Debes escribir un nombre para realizar la búsqueda.")

        nombre_buscado = nombre.lower()

        return [
            usuario
            for usuario in self.usuarios
            if nombre_buscado in usuario["nombre"].lower()
        ]