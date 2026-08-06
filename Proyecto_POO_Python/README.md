# Fundamentos de Python: Clases, Objetos y Encapsulación

Proyecto desarrollado para la actividad de SENA (ADSO) sobre Programación Orientada
a Objetos en Python, aplicando los conceptos de clase, objeto y encapsulación
a través de ejemplos replicados, dos talleres independientes y un reto integrador.

## Estructura del repositorio

```
proyecto-poo-python/
├── ejemplos_replicados/
│   ├── ejemplo_clase_objeto.py       # Clase Persona: clase y objeto básicos
│   └── ejemplo_encapsulacion.py      # Clase CuentaBancaria: encapsulación básica
├── taller_clases_objetos/
│   └── taller_clases_objetos.py      # Clase Vehiculo: clases, atributos y objetos
├── taller_encapsulacion/
│   └── taller_encapsulacion.py       # Clase Empleado: atributo privado + @property
├── reto_sistema_prestamos/
│   ├── equipo.py                     # Clase Equipo
│   ├── usuario.py                    # Clase Usuario
│   ├── prestamo.py                   # Clase Prestamo
│   ├── sistema_prestamos.py          # Gestión de colecciones y operaciones
│   └── main.py                       # Ejecución del flujo completo
└── README.md
```

## Diseño de clases y encapsulación

- **Ejemplos replicados:** muestran la base de POO en Python: definición de una
  clase (`Persona`), instanciación de objetos y, en `CuentaBancaria`, el uso de
  un atributo privado (`__saldo`) que solo puede modificarse mediante métodos
  controlados (`depositar`, `retirar`).
- **Taller de Clases y Objetos:** la clase `Vehiculo` practica atributos,
  métodos de instancia y la creación de varios objetos independientes.
- **Taller de Encapsulación:** la clase `Empleado` encapsula el salario con
  doble guion bajo (`__salario`) y expone su acceso controlado mediante
  `@property` y un `setter` que valida que el valor no sea negativo.
- **Reto — Sistema de Préstamos de Equipos:**
  - `Equipo`: encapsula `disponible`, ya que ese estado no debe cambiar
    libremente desde fuera de la clase, solo a través de `marcar_prestado()`
    y `marcar_disponible()`.
  - `Usuario`: datos básicos de la persona que solicita el préstamo.
  - `Prestamo`: relaciona un `Equipo` con un `Usuario` y encapsula el
    `estado` (Activo/Devuelto), modificable solo mediante `cerrar_prestamo()`.
  - `SistemaPrestamos`: organiza todo en colecciones (`dict` para equipos y
    usuarios, `list` para préstamos) y expone los métodos para registrar,
    consultar, modificar y devolver préstamos, validando reglas de negocio
    como que un equipo no disponible no pueda volver a prestarse.

## Instrucciones de ejecución

Cada script se ejecuta de forma independiente con Python 3, sin dependencias
externas:

```bash
python3 ejemplos_replicados/ejemplo_clase_objeto.py
python3 ejemplos_replicados/ejemplo_encapsulacion.py
python3 taller_clases_objetos/taller_clases_objetos.py
python3 taller_encapsulacion/taller_encapsulacion.py
cd reto_sistema_prestamos
python3 main.py
```

## Ejemplo de salida en consola (reto integrador)

```
--- Registro de equipos ---
Equipo registrado: Portátil Dell
Equipo registrado: Videobeam Epson

--- Registro de usuarios ---
Usuario registrado: Camila Torres
Usuario registrado: Jorge Ríos

--- Equipos ---
[E001] Portátil Dell (Computador) - Disponible
[E002] Videobeam Epson (Proyector) - Disponible

--- Registrar préstamo ---
Préstamo registrado: Préstamo #1 | Equipo: Portátil Dell | Usuario: Camila Torres | Estado: Activo

--- Préstamos activos ---
Préstamo #1 | Equipo: Portátil Dell | Usuario: Camila Torres | Estado: Activo

--- Intento de préstamo duplicado ---
El equipo no está disponible.

--- Devolución ---
Equipo devuelto: Portátil Dell

--- Estado final de equipos ---
[E001] Portátil Dell (Computador) - Disponible
[E002] Videobeam Epson (Proyector) - Disponible
```

*(Reemplaza este bloque por capturas de pantalla reales de tu consola antes de
entregar, tal como lo pide la rúbrica.)*

## Reflexión personal

Durante este proyecto entendí de forma más práctica qué significa encapsular
un atributo y por qué no es solo "ponerle dos guiones bajos al nombre": la
idea es proteger los datos que pueden dejar el sistema en un estado
inconsistente si se modifican sin control, como la disponibilidad de un
equipo o el estado de un préstamo. Trabajar con varias clases relacionadas
entre sí (Equipo, Usuario, Préstamo) también me ayudó a ver cómo se organiza
un sistema pequeño usando diccionarios y listas en vez de solo variables
sueltas. El mayor reto fue decidir en qué clase debía vivir cada
responsabilidad, por ejemplo, si la validación de disponibilidad debía estar
en `Equipo` o en `SistemaPrestamos`; terminé dejando el estado en `Equipo` y
la lógica de negocio (validar antes de prestar) en `SistemaPrestamos`, lo que
me dejó más claro el principio de responsabilidad de cada clase.
