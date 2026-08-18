def validar_nombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo puede contener letras.")

    return nombre.strip()


def validar_edad(edad):
    try:
        edad = int(edad)
    except ValueError:
        raise ValueError("La edad debe ser un número entero.")

    if edad < 1:
        raise ValueError("La edad debe ser mayor que 0.")

    return edad