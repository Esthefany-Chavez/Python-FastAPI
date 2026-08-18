from app.config.settings import APP_NAME, APP_VERSION, ADMIN_USER
from app.usuarios.gestor import GestorUsuarios


def mostrar_encabezado():
    """Muestra la información principal de la aplicación."""
    print("\n" + "=" * 50)
    print(f"   {APP_NAME} - Versión {APP_VERSION}")
    print("=" * 50)
    print(f"Administrador: {ADMIN_USER}")
    print("=" * 50)


def mostrar_menu():
    """Muestra las opciones disponibles."""
    print("\n¿Qué deseas hacer?")
    print("1. Registrar usuario")
    print("2. Mostrar usuarios")
    print("3. Buscar usuario")
    print("4. Salir")


def registrar_usuario(gestor):
    """Solicita los datos y registra un nuevo usuario."""
    print("\n--- REGISTRO DE USUARIO ---")

    nombre = input("Nombre completo: ").strip()
    edad = input("Edad: ").strip()
    correo = input("Correo electrónico: ").strip()
    rol = input("Rol (administrador, aprendiz, instructor): ").strip()

    try:
        gestor.registrar_usuario(nombre, edad, correo, rol)
        print("\n✓ Usuario registrado correctamente.")

    except ValueError as error:
        print(f"\n⚠ No se pudo registrar el usuario: {error}")


def mostrar_usuarios(gestor):
    """Muestra todos los usuarios registrados."""
    print("\n--- USUARIOS REGISTRADOS ---")

    usuarios = gestor.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for numero, usuario in enumerate(usuarios, start=1):
        print(
            f"{numero}. {usuario['nombre']} | "
            f"Edad: {usuario['edad']} | "
            f"Correo: {usuario['correo']} | "
            f"Rol: {usuario['rol']}"
        )


def buscar_usuario(gestor):
    """Busca usuarios utilizando parte del nombre."""
    print("\n--- BUSCAR USUARIO ---")

    nombre = input("Escribe el nombre que deseas buscar: ").strip()

    try:
        resultados = gestor.buscar_usuario(nombre)

        if not resultados:
            print("\nNo se encontraron usuarios con ese nombre.")
            return

        print(f"\nSe encontraron {len(resultados)} usuario(s):")

        for usuario in resultados:
            print(
                f"- {usuario['nombre']} | "
                f"Edad: {usuario['edad']} | "
                f"Correo: {usuario['correo']} | "
                f"Rol: {usuario['rol']}"
            )

    except ValueError as error:
        print(f"\n⚠ {error}")


def ejecutar():
    """Ejecuta el menú principal de la aplicación."""
    gestor = GestorUsuarios()

    mostrar_encabezado()

    while True:
        mostrar_menu()

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            registrar_usuario(gestor)

        elif opcion == "2":
            mostrar_usuarios(gestor)

        elif opcion == "3":
            buscar_usuario(gestor)

        elif opcion == "4":
            print("\nGracias por utilizar el sistema.")
            print("Programa finalizado correctamente.")
            break

        else:
            print("\n⚠ Opción no válida. Selecciona una opción del 1 al 4.")


if __name__ == "__main__":
    ejecutar()