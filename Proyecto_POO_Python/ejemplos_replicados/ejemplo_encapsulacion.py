"""
Ejemplo replicado: Encapsulación en Python.
Demuestra el uso de un atributo privado (__saldo) que solo puede
modificarse a través de métodos controlados de la clase.
"""


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("El monto debe ser mayor a cero.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def consultar_saldo(self):
        return self.__saldo


if __name__ == "__main__":
    cuenta = CuentaBancaria("Carlos", 1000)
    cuenta.depositar(500)
    cuenta.retirar(300)
    print(f"Saldo final: {cuenta.consultar_saldo()}")
