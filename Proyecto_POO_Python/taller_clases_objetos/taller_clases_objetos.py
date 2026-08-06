"""
Taller: Clases y Objetos en Python.
Ejercicio propio: gestión básica de vehículos, con atributos,
métodos y creación de múltiples objetos.
"""


class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_info(self):
        print(f"{self.marca} {self.modelo} ({self.año}) - ${self.precio}")

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Nuevo precio con descuento: ${self.precio}")


if __name__ == "__main__":
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2022, 80000000)
    vehiculo2 = Vehiculo("Mazda", "CX-5", 2023, 120000000)

    print("--- Información inicial ---")
    vehiculo1.mostrar_info()
    vehiculo2.mostrar_info()

    print("\n--- Aplicando descuento al Corolla ---")
    vehiculo1.aplicar_descuento(10)
    vehiculo1.mostrar_info()
