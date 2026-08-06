"""
Clase SistemaPrestamos: gestiona las colecciones de equipos, usuarios
y préstamos, y expone los métodos para registrar, consultar,
modificar y devolver préstamos.
"""

from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo


class SistemaPrestamos:
    def __init__(self):
        self.equipos = {}      # {codigo: Equipo}
        self.usuarios = {}     # {documento: Usuario}
        self.prestamos = []    # lista de Prestamo
        self.__contador_id = 1

    # --- Registro de entidades ---
    def registrar_equipo(self, codigo, nombre, tipo):
        self.equipos[codigo] = Equipo(codigo, nombre, tipo)
        print(f"Equipo registrado: {nombre}")

    def registrar_usuario(self, documento, nombre, correo):
        self.usuarios[documento] = Usuario(documento, nombre, correo)
        print(f"Usuario registrado: {nombre}")

    # --- Gestión de préstamos ---
    def registrar_prestamo(self, codigo_equipo, documento_usuario):
        equipo = self.equipos.get(codigo_equipo)
        usuario = self.usuarios.get(documento_usuario)

        if not equipo:
            print("Equipo no encontrado.")
            return
        if not usuario:
            print("Usuario no encontrado.")
            return
        if not equipo.disponible:
            print("El equipo no está disponible.")
            return

        prestamo = Prestamo(self.__contador_id, equipo, usuario)
        equipo.marcar_prestado()
        self.prestamos.append(prestamo)
        self.__contador_id += 1
        print(f"Préstamo registrado: {prestamo}")

    def devolver_equipo(self, id_prestamo):
        for prestamo in self.prestamos:
            if prestamo.id_prestamo == id_prestamo and prestamo.estado == "Activo":
                prestamo.cerrar_prestamo()
                prestamo.equipo.marcar_disponible()
                print(f"Equipo devuelto: {prestamo.equipo.nombre}")
                return
        print("Préstamo no encontrado o ya devuelto.")

    # --- Consultas ---
    def consultar_equipos(self):
        for equipo in self.equipos.values():
            print(equipo)

    def consultar_prestamos_activos(self):
        activos = [p for p in self.prestamos if p.estado == "Activo"]
        if not activos:
            print("No hay préstamos activos.")
        for p in activos:
            print(p)
