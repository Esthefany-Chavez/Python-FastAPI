# 🐍 Programación Orientada a Objetos en Python

Repositorio correspondiente a la actividad **Programación Orientada a Objetos (POO)** del programa **Tecnología en Análisis y Desarrollo de Software (ADSO)** del **SENA**.

---

# 📖 Descripción

Este proyecto reúne los ejercicios desarrollados para comprender los fundamentos de la **Programación Orientada a Objetos (POO)** en Python.

A través de ejemplos guiados, talleres y un reto integrador se aplican conceptos como:

- Clases
- Objetos
- Atributos
- Métodos
- Encapsulación
- Relaciones entre clases
- Organización de proyectos orientados a objetos

---

# 📂 Estructura del proyecto

```text
Proyecto_POO_Python/
│
├── ejemplos_replicados/
│   ├── clase_objeto.py
│   └── encapsulacion.py
│
├── reto_sistema_prestamos/
│   ├── equipo.py
│   ├── usuario.py
│   ├── prestamo.py
│   ├── sistema_prestamos.py
│   └── main.py
│
├── taller_clases_objetos/
│   └── clases_objetos.py
│
├── taller_encapsulacion/
│   └── taller_encapsulacion.py
│
└── README.md
```

---

# 📚 Contenido del proyecto

## 🟢 Ejemplos replicados

Se desarrollan ejemplos básicos para comprender la estructura de una clase y el funcionamiento de la encapsulación.

### Archivos

- `clase_objeto.py`
- `encapsulacion.py`

### Conceptos aplicados

- Definición de clases
- Creación de objetos
- Constructores (`__init__`)
- Métodos
- Encapsulación mediante atributos privados (`__atributo`)

---

## 🟡 Taller de Clases y Objetos

Se desarrolla una clase `Vehiculo` con el objetivo de practicar:

- Atributos
- Métodos
- Creación de múltiples objetos
- Independencia entre instancias

**Archivo**

```text
clases_objetos.py
```

---

## 🔵 Taller de Encapsulación

Se implementa la clase `Empleado`, aplicando el principio de encapsulación mediante atributos privados.

### Conceptos trabajados

- Atributos privados
- Métodos Getter y Setter
- Decorador `@property`
- Validación de datos

**Archivo**

```text
taller_encapsulacion.py
```

---

## 🔴 Reto Integrador – Sistema de Préstamos de Equipos

El reto consiste en desarrollar un sistema para administrar préstamos de equipos tecnológicos utilizando Programación Orientada a Objetos.

### Clases implementadas

### 📦 Equipo

Representa cada equipo disponible para préstamo.

Responsabilidades:

- Registrar información del equipo.
- Controlar su disponibilidad.
- Cambiar su estado mediante métodos controlados.

---

### 👤 Usuario

Representa la persona que solicita un préstamo.

Responsabilidades:

- Almacenar la información básica del usuario.
- Identificar al solicitante del préstamo.

---

### 📄 Prestamo

Relaciona un usuario con un equipo.

Responsabilidades:

- Registrar préstamos.
- Controlar el estado del préstamo.
- Gestionar la devolución del equipo.

---

### 🖥️ SistemaPrestamos

Es la clase encargada de administrar todo el sistema.

Funciones principales:

- Registrar equipos.
- Registrar usuarios.
- Crear préstamos.
- Validar disponibilidad.
- Registrar devoluciones.
- Consultar información del sistema.

---

# ▶️ Cómo ejecutar el proyecto

Cada archivo puede ejecutarse de manera independiente.

```bash
py ejemplos_replicados/clase_objeto.py

py ejemplos_replicados/encapsulacion.py

py taller_clases_objetos/clases_objetos.py

py taller_encapsulacion/taller_encapsulacion.py
```

Para ejecutar el reto principal:

```bash
cd reto_sistema_prestamos

py main.py
```

> En algunos sistemas puede utilizarse `python` en lugar de `py`.

---

# 💻 Ejemplo de ejecución

```text
--- Registro de equipos ---
Equipo registrado: Portátil Dell
Equipo registrado: Videobeam Epson

--- Registro de usuarios ---
Usuario registrado: Camila Torres
Usuario registrado: Jorge Ríos

--- Equipos registrados ---
[E001] Portátil Dell (Computador) - Disponible
[E002] Videobeam Epson (Proyector) - Disponible

--- Registrar préstamo ---
Préstamo registrado: Préstamo #1 | Equipo: Portátil Dell | Usuario: Camila Torres | Estado: Activo

--- Préstamos activos ---
Préstamo #1 | Equipo: Portátil Dell | Usuario: Camila Torres | Estado: Activo

--- Intento de préstamo duplicado ---
El equipo no está disponible.

--- Devolución del equipo ---
Equipo devuelto: Portátil Dell

--- Estado final de los equipos ---
[E001] Portátil Dell (Computador) - Disponible
[E002] Videobeam Epson (Proyector) - Disponible
```

---

# 🛠️ Tecnologías utilizadas

| Herramienta | Uso |
|------------|-----|
| 🐍 Python 3 | Desarrollo del proyecto |
| Git | Control de versiones |
| GitHub | Repositorio remoto |
| Visual Studio Code | Editor de código |

---

# 🎯 Objetivo del proyecto

Aplicar los principios fundamentales de la Programación Orientada a Objetos mediante el desarrollo de ejemplos, talleres y un sistema funcional de préstamos de equipos, fortaleciendo el uso de clases, objetos, encapsulación y organización del código.

---

# 💡 Reflexión

Durante el desarrollo de este proyecto comprendí que la encapsulación no consiste únicamente en declarar atributos privados, sino en proteger la información para garantizar que solo pueda modificarse mediante métodos controlados.

Además, trabajar con varias clases relacionadas entre sí me permitió entender mejor cómo dividir responsabilidades dentro de una aplicación y cómo cada clase cumple una función específica para mantener un código más organizado, reutilizable y fácil de mantener.

---

# 👩‍💻 Autor

**Esthefany Valentina Chávez Parra**

**Tecnología en Análisis y Desarrollo de Software (ADSO)**

**SENA**