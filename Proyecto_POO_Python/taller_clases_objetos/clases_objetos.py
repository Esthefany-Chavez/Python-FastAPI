"""
Taller: Clases y Objetos en Python.

Este programa muestra cómo crear una clase, definir sus atributos
y utilizar métodos para realizar acciones sobre los objetos creados.

En este ejemplo se utiliza la clase Vehiculo para representar
automóviles con información como la marca, el modelo, el año
y el precio.
"""


class Vehiculo:

    # Constructor de la clase.
    # Se ejecuta automáticamente cada vez que se crea
    # un nuevo objeto de tipo Vehiculo.
    def __init__(self, marca, modelo, año, precio):

        # Guarda la marca del vehículo.
        self.marca = marca

        # Guarda el modelo.
        self.modelo = modelo

        # Guarda el año de fabricación.
        self.año = año

        # Guarda el precio del vehículo.
        self.precio = precio

    # Método que muestra toda la información del vehículo.
    def mostrar_info(self):

        print(f"{self.marca} {self.modelo} ({self.año}) - ${self.precio}")

    # Método que aplica un descuento al precio del vehículo.
    # El porcentaje es enviado cuando se llama al método.
    def aplicar_descuento(self, porcentaje):

        # Calcula cuánto dinero se descontará.
        descuento = self.precio * (porcentaje / 100)

        # Resta el descuento al precio original.
        self.precio -= descuento

        # Muestra el nuevo precio.
        print(f"Nuevo precio con descuento: ${self.precio}")


# Si este archivo se ejecuta directamente,
# se crean dos vehículos para probar el funcionamiento
# de la clase y sus métodos.
if __name__ == "__main__":

    # Se crean dos objetos de la clase Vehiculo.
    vehiculo1 = Vehiculo("Toyota", "Corolla", 2022, 80000000)
    vehiculo2 = Vehiculo("Mazda", "CX-5", 2023, 120000000)

    print("--- Información inicial ---")

    # Se muestra la información de ambos vehículos.
    vehiculo1.mostrar_info()
    vehiculo2.mostrar_info()

    print("\n--- Aplicando descuento al Corolla ---")

    # Se aplica un descuento del 10 % al primer vehículo.
    vehiculo1.aplicar_descuento(10)

    # Se vuelve a mostrar la información para comprobar
    # que el precio cambió después del descuento.
    vehiculo1.mostrar_info()