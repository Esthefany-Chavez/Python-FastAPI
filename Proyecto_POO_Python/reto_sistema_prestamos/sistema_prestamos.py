"""
Clase SistemaPrestamos.

Esta clase administra el funcionamiento del sistema de préstamos.

Aquí se almacenan todos los equipos registrados, los usuarios
y los préstamos realizados. Además, contiene los métodos para
registrar información, consultar datos y devolver equipos.

Se puede decir que esta es la clase principal del proyecto,
porque coordina el trabajo de las demás clases.
"""

# Se importan las clases necesarias para construir el sistema.
from equipo import Equipo
from usuario import Usuario
from prestamo import Prestamo


class SistemaPrestamos:

    # Constructor de la clase.
    # Se ejecuta automáticamente cuando se crea el sistema.
    def __init__(self):

        # Diccionario donde se almacenan los equipos.
        # La clave será el código del equipo.
        # El valor será un objeto de la clase Equipo.
        self.equipos = {}

        # Diccionario donde se almacenan los usuarios.
        # La clave será el documento.
        # El valor será un objeto Usuario.
        self.usuarios = {}

        # Lista donde se guardarán todos los préstamos
        # realizados en el sistema.
        self.prestamos = []

        # Contador privado utilizado para asignar un
        # identificador diferente a cada préstamo.
        self.__contador_id = 1


    # Registro de equipos

    def registrar_equipo(self, codigo, nombre, tipo):

        # Se crea un nuevo objeto Equipo y se guarda
        # dentro del diccionario utilizando su código.
        self.equipos[codigo] = Equipo(codigo, nombre, tipo)

        print(f"Equipo registrado: {nombre}")


    # Registro de usuarios

    def registrar_usuario(self, documento, nombre, correo):

        # Se crea un nuevo objeto Usuario y se guarda
        # utilizando el documento como identificador.
        self.usuarios[documento] = Usuario(documento, nombre, correo)

        print(f"Usuario registrado: {nombre}")


    # Registrar un préstamo

    def registrar_prestamo(self, codigo_equipo, documento_usuario):

        # Busca el equipo utilizando su código.
        # Si no existe, devuelve None.
        equipo = self.equipos.get(codigo_equipo)

        # Busca el usuario mediante su documento.
        usuario = self.usuarios.get(documento_usuario)

        # Verifica que el equipo exista.
        if not equipo:
            print("Equipo no encontrado.")
            return

        # Verifica que el usuario exista.
        if not usuario:
            print("Usuario no encontrado.")
            return

        # Verifica que el equipo todavía esté disponible.
        if not equipo.disponible:
            print("El equipo no está disponible.")
            return

        # Si todas las validaciones son correctas,
        # se crea el préstamo.
        prestamo = Prestamo(
            self.__contador_id,
            equipo,
            usuario
        )

        # El equipo cambia a estado prestado.
        equipo.marcar_prestado()

        # El préstamo se agrega a la lista.
        self.prestamos.append(prestamo)

        # Se incrementa el contador para que el siguiente
        # préstamo tenga otro identificador.
        self.__contador_id += 1

        print(f"Préstamo registrado: {prestamo}")


    # Devolver un equipo

    def devolver_equipo(self, id_prestamo):

        # Se recorren todos los préstamos registrados.
        for prestamo in self.prestamos:

            # Se verifica que el préstamo exista
            # y todavía esté activo.
            if (
                prestamo.id_prestamo == id_prestamo
                and prestamo.estado == "Activo"
            ):

                # Se cambia el estado del préstamo.
                prestamo.cerrar_prestamo()

                # El equipo vuelve a quedar disponible.
                prestamo.equipo.marcar_disponible()

                print(f"Equipo devuelto: {prestamo.equipo.nombre}")

                return

        # Si no se encontró el préstamo.
        print("Préstamo no encontrado o ya fue devuelto.")


    # Consultar equipos

    def consultar_equipos(self):

        # Recorre todos los equipos registrados
        # e imprime su información.
        for equipo in self.equipos.values():
            print(equipo)


    # Consultar préstamos activos

    def consultar_prestamos_activos(self):

        # Se crea una lista únicamente con los préstamos
        # cuyo estado sea Activo.
        activos = [
            p for p in self.prestamos
            if p.estado == "Activo"
        ]

        # Si la lista está vacía...
        if not activos:
            print("No hay préstamos activos.")
            return

        # Se muestran todos los préstamos activos.
        for prestamo in activos:
            print(prestamo)