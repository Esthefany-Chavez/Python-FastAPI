"""
Taller: Encapsulación en Python.

Este programa muestra cómo proteger un atributo de una clase
utilizando encapsulación.

En este ejemplo se utiliza la clase Empleado, donde el salario
es un dato privado que solo puede consultarse y modificarse
mediante métodos controlados.
"""


class Empleado:

    # Constructor de la clase.
    # Se ejecuta automáticamente cuando se crea un nuevo empleado.
    def __init__(self, nombre, salario):

        # Guarda el nombre del empleado.
        self.nombre = nombre

        # __salario es un atributo privado.
        # Solo puede modificarse mediante el setter.
        self.__salario = salario

    # @property permite consultar el salario
    # como si fuera un atributo normal, sin acceder
    # directamente al atributo privado.
    @property
    def salario(self):
        return self.__salario

    # El setter controla la modificación del salario.
    # Antes de cambiar el valor realiza una validación.
    @salario.setter
    def salario(self, nuevo_salario):

        # Solo se permiten salarios iguales o mayores a cero.
        if nuevo_salario >= 0:

            # Se actualiza el salario.
            self.__salario = nuevo_salario

        else:
            print("El salario no puede ser negativo.")

    # Método que muestra la información del empleado.
    def mostrar_info(self):

        print(f"Empleado: {self.nombre} | Salario: ${self.__salario}")


# Si este archivo se ejecuta directamente,
# se crea un empleado para probar el funcionamiento
# de la encapsulación.
if __name__ == "__main__":

    # Se crea un objeto de la clase Empleado.
    empleado1 = Empleado("María", 2500000)

    # Se muestra la información inicial.
    empleado1.mostrar_info()

    print("\n--- Aumentando salario mediante el setter ---")

    # El salario se modifica utilizando el setter.
    empleado1.salario = 3000000

    # Se muestra nuevamente la información.
    empleado1.mostrar_info()

    print("\n--- Intentando asignar un salario negativo ---")

    # Se intenta asignar un salario inválido.
    # El setter evita que se realice el cambio.
    empleado1.salario = -500

    # El salario continúa siendo el anterior.
    empleado1.mostrar_info()