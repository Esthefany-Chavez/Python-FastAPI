import re


ROLES_PERMITIDOS = {
    "administrador",
    "aprendiz",
    "instructor"
}


def validar_nombre(nombre):
    """Valida que el nombre sea correcto."""
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")

    if len(nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")

    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+", nombre):
        raise ValueError("El nombre solo puede contener letras y espacios.")

    return nombre


def validar_edad(edad):
    """Valida que la edad sea numérica y se encuentre en un rango válido."""
    try:
        edad = int(edad)
    except ValueError:
        raise ValueError("La edad debe ser un número entero.")

    if edad < 18 or edad > 100:
        raise ValueError("La edad debe estar entre 18 y 100 años.")

    return edad


def validar_correo(correo):
    """Valida el formato básico de un correo electrónico."""
    if not correo:
        raise ValueError("El correo electrónico no puede estar vacío.")

    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.fullmatch(patron, correo):
        raise ValueError("El correo electrónico no tiene un formato válido.")

    return correo.lower()


def validar_rol(rol):
    """Valida que el rol pertenezca a los roles disponibles."""
    rol = rol.lower().strip()

    if rol not in ROLES_PERMITIDOS:
        roles = ", ".join(sorted(ROLES_PERMITIDOS))
        raise ValueError(
            f"Rol no válido. Los roles disponibles son: {roles}."
        )

    return rol