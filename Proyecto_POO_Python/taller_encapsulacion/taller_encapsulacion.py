"""
Taller: Encapsulación en Python.
Ejercicio propio: gestión de empleados, usando un atributo privado
para el salario y controlando su acceso mediante @property.
"""


class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario  # atributo privado

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario >= 0:
            self.__salario = nuevo_salario
        else:
            print("El salario no puede ser negativo.")

    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Salario: ${self.__salario}")


if __name__ == "__main__":
    empleado1 = Empleado("María", 2500000)
    empleado1.mostrar_info()

    print("\n--- Aumentando salario mediante el setter ---")
    empleado1.salario = 3000000
    empleado1.mostrar_info()

    print("\n--- Intentando asignar un salario negativo ---")
    empleado1.salario = -500
    empleado1.mostrar_info()
