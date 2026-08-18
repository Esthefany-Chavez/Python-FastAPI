from .validaciones import validar_nombre, validar_edad


class GestorUsuarios:

    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, edad):
        nombre = validar_nombre(nombre)
        edad = validar_edad(edad)

        usuario = {
            "nombre": nombre,
            "edad": edad
        }

        self.usuarios.append(usuario)

        return usuario

    def listar_usuarios(self):
        return self.usuarios

    def buscar_usuario(self, nombre):
        nombre = nombre.strip().lower()

        for usuario in self.usuarios:
            if usuario["nombre"].lower() == nombre:
                return usuario

        return None