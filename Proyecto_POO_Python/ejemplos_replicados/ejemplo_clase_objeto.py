"""
Ejemplo replicado: Clase y Objeto en Python.
Demuestra la creación de una clase básica, sus atributos y métodos,
y la instanciación de varios objetos a partir de ella.
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


if __name__ == "__main__":
    persona1 = Persona("Ana", 28)
    persona2 = Persona("Luis", 35)

    persona1.saludar()
    persona2.saludar()
