"""
Ejemplo replicado: Encapsulación en Python.

Este programa muestra cómo proteger un atributo de una clase
utilizando encapsulación. En este caso, el saldo de una
billetera digital solo puede modificarse mediante los métodos
definidos por la clase.
"""


class BilleteraDigital:
    """
    La clase BilleteraDigital representa una billetera virtual.

    Cada objeto almacena el nombre del propietario y el saldo
    disponible para realizar recargas y pagos.
    """

    # Constructor de la clase.
    # Se ejecuta automáticamente cuando se crea una billetera.
    # Permite guardar el nombre del propietario y un saldo inicial.
    def __init__(self, propietario, saldo_inicial=0):

        # Nombre del propietario de la billetera.
        self.propietario = propietario

        # __saldo es un atributo privado.
        # Los dos guiones bajos (__) indican que este atributo
        # no debe modificarse directamente desde fuera de la clase.
        # Para cambiar su valor es necesario utilizar los métodos
        # definidos por la propia clase.
        self.__saldo = saldo_inicial

    # Método para recargar dinero en la billetera.
    def recargar(self, valor):

        # Solo se permite recargar valores mayores que cero.
        if valor > 0:

            # Se suma el valor recargado al saldo actual.
            self.__saldo += valor

            print(f"Recarga realizada con éxito. Saldo disponible: ${self.__saldo}")

        else:
            print("El valor de la recarga debe ser mayor que cero.")

    # Método para realizar un pago desde la billetera.
    def pagar(self, valor):

        # Se verifica que el valor sea válido
        # y que exista suficiente saldo para realizar el pago.
        if 0 < valor <= self.__saldo:

            # Se descuenta el valor del pago del saldo disponible.
            self.__saldo -= valor

            print(f"Pago realizado con éxito. Saldo disponible: ${self.__saldo}")

        else:
            print("Saldo insuficiente o valor inválido.")

    # Método para consultar el saldo.
    # Devuelve el saldo disponible sin permitir modificarlo.
    def consultar_saldo(self):
        return self.__saldo


# Si este archivo se ejecuta directamente,
# se crea una billetera para probar el funcionamiento
# de los métodos de la clase.
if __name__ == "__main__":

    # Se crea un objeto de la clase BilleteraDigital.
    billetera = BilleteraDigital("Esthefany", 80000)

    # Se realizan algunas operaciones sobre la billetera.
    billetera.recargar(20000)
    billetera.pagar(35000)

    # Se consulta el saldo final disponible.
    print(f"Saldo final: ${billetera.consultar_saldo()}")