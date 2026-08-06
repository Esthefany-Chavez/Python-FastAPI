# 🐍 Fundamentos de Python: Estructuras de Control y Funciones

Repositorio correspondiente a la actividad **Fundamentos de Python: Estructuras de Control y Funciones**, desarrollada como parte del programa **Tecnología en Análisis y Desarrollo de Software (ADSO)** del **SENA**.

---

# 📖 Descripción

Este proyecto reúne la solución de tres retos enfocados en el uso de las principales estructuras de control y funciones del lenguaje Python.

Cada reto fue desarrollado aplicando buenas prácticas de programación, incluyendo comentarios explicativos y una organización clara de los archivos para facilitar su comprensión.

---

# 📂 Estructura del proyecto

La guía proponía inicialmente la siguiente organización:

```text
fundamentos_python_control_fun/
│
├── README.md
│
└── src/
    ├── condicionales/
    │   └── reto01.py
    │
    ├── iterativas/
    │   └── reto02.py
    │
    └── funciones/
        └── reto03.py
```

Sin embargo, después de analizar el propósito de cada ejercicio, decidí reorganizar los archivos para que cada reto quedara ubicado en la carpeta correspondiente al concepto principal que desarrolla.

La estructura final quedó así:

```text
fundamentos_python_control_fun/
│
├── src/
│    ├── condicionales/
│    │   └── reto02.py
│    │
│    ├── funciones/
│    │   └── reto01.py
│    │
│    └── iterativas/
│        └── reto03.py
│
└── README.md
```

Esta organización permite identificar con mayor facilidad el tema principal trabajado en cada ejercicio.

---

# 📚 Retos desarrollados

## 🟢 Reto 1 - Calculadora de Métricas del Desarrollador

**Ubicación**

```text
src/funciones/reto01.py
```

### Funcionalidades

El programa solicita:

- Nombre del desarrollador.
- Cantidad de proyectos asignados.
- Horas dedicadas a cada proyecto.

Posteriormente genera un reporte que incluye:

- Total de horas trabajadas.
- Promedio de horas por proyecto.
- Porcentaje de tiempo dedicado a cada proyecto.

---

## 🟡 Reto 2 - Sistema Simplificado de Calificación e Inventario

**Ubicación**

```text
src/condicionales/reto02.py
```

### Funcionalidades

El programa trabaja con una lista de productos y permite:

- Mostrar el estado de cada producto.
- Identificar productos agotados.
- Detectar productos con stock crítico.
- Calcular el porcentaje general de disponibilidad del inventario.

---

## 🔵 Reto 3 - Motor de Análisis de Frecuencia de Texto

**Ubicación**

```text
src/iterativas/reto03.py
```

### Funcionalidades

El programa solicita al usuario un texto y posteriormente:

- Convierte todo el contenido a minúsculas.
- Elimina signos básicos de puntuación.
- Cuenta la frecuencia de cada palabra.
- Identifica la palabra más repetida y el número de veces que aparece.

---

# 🚀 Requisitos

- Python 3.x
- Visual Studio Code (o cualquier editor compatible)
- Git
- GitHub

---

# ▶️ Cómo ejecutar los programas

Desde la carpeta principal del proyecto, utiliza alguno de los siguientes comandos.

### Reto 1

```bash
py src/funciones/reto01.py
```

### Reto 2

```bash
py src/condicionales/reto02.py
```

### Reto 3

```bash
py src/iterativas/reto03.py
```

> También se puede reemplazar `py` por `python` según la configuración de su sistema.

---

# 🛠️ Tecnologías utilizadas

| Herramienta | Uso |
|-------------|-----|
| 🐍 Python 3 | Desarrollo de los retos |
| Git | Control de versiones |
| GitHub | Repositorio remoto |
| Visual Studio Code | Editor de código |

---

# 🎯 Objetivo del proyecto

Aplicar estructuras condicionales, ciclos y funciones mediante la resolución de problemas prácticos que permitan fortalecer la lógica de programación y el desarrollo de algoritmos en Python.

---

# 👩‍💻 Autor

**Esthefany Valentina Chávez Parra**

**SENA – Tecnología en Análisis y Desarrollo de Software (ADSO)**