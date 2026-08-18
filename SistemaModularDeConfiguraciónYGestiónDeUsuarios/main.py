from app.config.settings import APP_NAME, APP_VERSION, ADMIN_USER
from app.usuarios.gestor import GestorUsuarios


def mostrar_menu():
    print("\n" + "=" * 40)
    print(f"      {APP_NAME}")
    print(f"      Versión: {APP_VERSION}")
    print("=" * 40)
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")
    print("=" * 40)


def registrar_usuario(gestor):
    print("\n--- Registrar usuario ---")

    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")

    try:
        usuario = gestor.registrar_usuario(nombre, edad)

        print("\nUsuario registrado correctamente.")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")

    except ValueError as error:
        print(f"\nError: {error}")


def listar_usuarios(gestor):
    print("\n--- Lista de usuarios ---")

    usuarios = gestor.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for numero, usuario in enumerate(usuarios, start=1):
        print(
            f"{numero}. "
            f"Nombre: {usuario['nombre']} | "
            f"Edad: {usuario['edad']}"
        )


def buscar_usuario(gestor):
    print("\n--- Buscar usuario ---")

    nombre = input("Ingrese el nombre que desea buscar: ")

    usuario = gestor.buscar_usuario(nombre)

    if usuario:
        print("\nUsuario encontrado.")
        print(f"Nombre: {usuario['nombre']}")
        print(f"Edad: {usuario['edad']}")
    else:
        print("\nUsuario no encontrado.")


def main():
    gestor = GestorUsuarios()

    print(f"\nBienvenido a {APP_NAME}")
    print(f"Usuario administrador: {ADMIN_USER}")

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(gestor)

        elif opcion == "2":
            listar_usuarios(gestor)

        elif opcion == "3":
            buscar_usuario(gestor)

        elif opcion == "4":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()