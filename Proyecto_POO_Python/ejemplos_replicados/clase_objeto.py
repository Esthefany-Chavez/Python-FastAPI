"""
Ejemplo replicado: Clase y Objeto en Python.

Este programa muestra cómo crear una clase sencilla,
definir sus atributos y crear objetos a partir de ella.
"""


class Persona:
    """
    La clase Persona es un molde.

    A partir de este molde se pueden crear diferentes personas,
    donde cada una tendrá sus propios datos.
    """

    # __init__ es el constructor de la clase.
    # Se ejecuta automáticamente cada vez que se crea un objeto.
    # Su función es guardar los datos iniciales del objeto.
    def __init__(self, nombre, ciudad):

        # self hace referencia al objeto que se está creando.
        # Gracias a self, cada objeto guarda sus propios datos
        # y no los comparte con los demás.

        # nombre y ciudad son los datos que recibe el constructor.
        # Se almacenan dentro del objeto.
        self.nombre = nombre
        self.ciudad = ciudad

    # Un método es una función que pertenece a una clase.
    # Este método muestra la información almacenada en el objeto.
    def presentarse(self):

        # self permite acceder a los atributos del objeto
        # para mostrar sus valores.
        print(f"Hola, soy {self.nombre} y vivo en {self.ciudad}.")


# __name__ es una variable que es creada automáticamente por Python.
#
# Si este archivo se ejecuta directamente, __name__ vale "__main__"
# y el código de abajo se ejecutará.
#
# Si la clase Persona se importa desde otro archivo,
# este bloque no se ejecutará.
#
# Esta estructura se utiliza para separar la definición de la clase
# del código de prueba.
if __name__ == "__main__":

    # Se crean dos objetos diferentes usando la misma clase.
    # Aunque provienen del mismo molde, cada uno almacena
    # información diferente.
    persona1 = Persona("Esthefany", "Medellín")
    persona2 = Persona("Santiago", "Bogotá")

    # Cada objeto ejecuta el mismo método,
    # pero muestra la información que tiene guardada.
    persona1.presentarse()
    persona2.presentarse()