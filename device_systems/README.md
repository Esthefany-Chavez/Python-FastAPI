# device_systems

API REST para la gestión de usuarios, dispositivos tecnológicos y préstamos,
desarrollada con FastAPI, SQLAlchemy, SQLite, Pydantic v2 y Alembic.

Este repositorio corresponde a la actividad **GA1-220501096-01-AA1-EV10 -
FastAPI Avanzado: Migraciones con Alembic, Asociaciones de Modelos y Consultas
con Joins**.

## Objetivo

La aplicación amplía el CRUD de usuarios de la actividad anterior y permite:

- Crear y consultar usuarios.
- Crear, actualizar, filtrar y eliminar dispositivos.
- Asociar dispositivos a usuarios mediante préstamos.
- Validar usuarios, dispositivos y disponibilidad antes de prestar.
- Registrar devoluciones y liberar nuevamente los dispositivos.
- Consultar préstamos con información relacionada mediante `join()`.
- Filtrar por estado, correo, tipo de dispositivo y búsqueda textual.
- Versionar la estructura de la base de datos con Alembic.
- Documentar la API con Swagger UI, ReDoc y OpenAPI.

## Tecnologías

- Python
- FastAPI
- Uvicorn
- SQLAlchemy 2
- Alembic
- SQLite
- Pydantic v2
- Pytest

## Estructura del proyecto

```text
device_systems/
├── app/
│   ├── database/
│   │   └── connection.py
│   ├── dependencies/
│   │   ├── database_dependency.py
│   │   ├── device_dependencies.py
│   │   ├── loan_dependencies.py
│   │   └── user_dependencies.py
│   ├── models/
│   │   ├── user_model.py
│   │   ├── device_model.py
│   │   └── loan_model.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── device_schema.py
│   │   └── loan_schema.py
│   ├── routes/
│   │   ├── user_routes.py
│   │   ├── device_routes.py
│   │   └── loan_routes.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── device_service.py
│   │   └── loan_service.py
│   └── main.py
├── alembic/
│   └── alembic/
│       ├── env.py
│       └── versions/
├── docs/
│   └── capturas/
├── tests/
├── alembic.ini
├── requirements.txt
└── README.md
```

## Instalación y ejecución

Desde la carpeta `device_systems`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

La base de datos debe prepararse con Alembic antes de iniciar la API:

```powershell
alembic upgrade head
uvicorn app.main:app --reload
```

La aplicación queda disponible en:

- API: <http://127.0.0.1:8000>
- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>
- OpenAPI: <http://127.0.0.1:8000/openapi.json>

## Migraciones con Alembic

La configuración principal se encuentra en `alembic.ini`, en la raíz del
proyecto. La metadata se importa desde `app.database.connection.Base` en
`alembic/alembic/env.py`.

Comandos utilizados en la actividad:

```powershell
alembic history
alembic current
alembic upgrade head
alembic check
alembic revision --autogenerate -m "describe the schema change"
```

La cadena actual de migraciones es:

```text
<base>
  └── 11cb831701ca  create users, devices and loans tables
        └── 7ddf8f3c0401  create devices and loans tables
```

La primera revisión crea `users`, `devices` y `loans`; la segunda conserva el
estado generado como `head`. `alembic check` confirma que no existen cambios de
modelo pendientes de migrar.

### Evidencias de Alembic

![Inicialización de Alembic](docs/capturas/evidencia_alembic_init.png)

![Generación automática de una revisión](docs/capturas/evidencia_alembic_revision_autogenerate.png)

![Aplicación de migraciones](docs/capturas/evidencia_alembic_upgrade_head.png)

![Historial de migraciones](docs/capturas/evidencia_alembic_history.png)

![Revisión aplicada](docs/capturas/evidencia_alembic_current.png)

![Verificación Alembic](docs/capturas/evidencia_alembic_check.png)

![Estructura de tablas](docs/capturas/evidencia_estructura_tablas.png)

## Modelos y asociaciones

### User

`User` representa la tabla `users` y conserva el CRUD completo:

- `id`
- `name`
- `email` único
- `role`
- `is_active`
- `created_at`

Un usuario puede tener muchos préstamos:

```python
loans = relationship("Loan", back_populates="user")
```

### Device

`Device` representa los equipos disponibles:

- `id`
- `name`
- `serial_number` único y obligatorio
- `device_type`
- `brand`
- `is_available`
- `created_at`

Un dispositivo puede aparecer en múltiples préstamos históricos:

```python
loans = relationship("Loan", back_populates="device")
```

### Loan

`Loan` relaciona usuarios y dispositivos mediante claves foráneas:

- `id`
- `user_id` hacia `users.id`
- `device_id` hacia `devices.id`
- `loan_date`
- `return_date`
- `status`: `active`, `returned` u `overdue`

Las relaciones inversas son:

```python
user = relationship("User", back_populates="loans")
device = relationship("Device", back_populates="loans")
```

![Creación de usuario, dispositivo y préstamo](docs/capturas/evidencia_creacion_usuario_dispositivo_prestamo.png)

## Endpoints

### Users

| Método | Endpoint | Descripción |
| --- | --- | --- |
| GET | `/users/` | Lista usuarios con filtros por rol y estado. |
| GET | `/users/{user_id}` | Consulta un usuario. |
| GET | `/users/email/{email}` | Busca por correo. |
| GET | `/users/{user_id}/loans` | Consulta préstamos del usuario. |
| POST | `/users/` | Crea un usuario. |
| PUT | `/users/{user_id}` | Actualiza completamente un usuario. |
| PATCH | `/users/{user_id}` | Actualiza parcialmente un usuario. |
| DELETE | `/users/{user_id}` | Elimina un usuario sin préstamos registrados. |

### Devices

| Método | Endpoint | Descripción |
| --- | --- | --- |
| GET | `/devices/` | Lista y filtra por tipo, disponibilidad, marca y búsqueda. |
| GET | `/devices/{device_id}` | Consulta un dispositivo. |
| GET | `/devices/{device_id}/loans` | Consulta su historial de préstamos. |
| POST | `/devices/` | Crea un dispositivo. |
| PUT | `/devices/{device_id}` | Actualiza completamente un dispositivo. |
| PATCH | `/devices/{device_id}` | Actualiza parcialmente un dispositivo. |
| DELETE | `/devices/{device_id}` | Elimina un dispositivo sin préstamos registrados. |

Filtros disponibles:

```text
GET /devices/?device_type=laptop
GET /devices/?is_available=true
GET /devices/?brand=lenovo
GET /devices/?search=thinkpad
```

### Loans

| Método | Endpoint | Descripción |
| --- | --- | --- |
| GET | `/loans/` | Lista préstamos y aplica filtros avanzados. |
| GET | `/loans/details` | Lista préstamos con usuario y dispositivo relacionados. |
| GET | `/loans/{loan_id}` | Consulta un préstamo detallado. |
| GET | `/loans/users/{user_id}` | Consulta préstamos por usuario. |
| GET | `/loans/devices/{device_id}` | Consulta préstamos por dispositivo. |
| POST | `/loans/` | Registra un préstamo. |
| PATCH | `/loans/{loan_id}/return` | Registra la devolución. |

Filtros disponibles:

```text
GET /loans/?status=active
GET /loans/?user_email=aprendiz@sena.edu.co
GET /loans/?device_type=laptop
GET /loans/?search=lenovo
```

## Reglas de negocio y errores

- Un usuario inexistente produce `404 Not Found`.
- Un dispositivo inexistente produce `404 Not Found`.
- Un dispositivo ocupado produce `409 Conflict`.
- Un préstamo inexistente produce `404 Not Found`.
- Devolver un préstamo ya devuelto produce `409 Conflict`.
- Un correo o serial duplicado produce `400 Bad Request`.
- Un préstamo siempre requiere un usuario y un dispositivo existentes.
- Los datos que no cumplen los schemas Pydantic producen `422 Unprocessable Entity`.
- No se permite eliminar un usuario o dispositivo con préstamos registrados.
- Una devolución cambia el préstamo a `returned`, registra `return_date` y
  actualiza `is_available` a `true`.

![Dispositivo no disponible](docs/capturas/evidencia_dispositivo_no_disponible.png)

## Consultas con joins y filtros

`app/services/loan_service.py` utiliza joins explícitos entre `Loan`, `User` y
`Device`. Las consultas aplican filtros opcionales con `and_`, `or_`, `filter`,
`ilike` y condiciones por identificador.

La respuesta de `/loans/details` contiene los datos reales de las tres tablas:

```json
{
  "loan_id": 1,
  "status": "active",
  "user": {
    "id": 1,
    "name": "Ana Perez",
    "email": "ana@sena.edu.co"
  },
  "device": {
    "id": 1,
    "name": "Laptop Lenovo ThinkPad",
    "serial_number": "LEN-EVID-001",
    "device_type": "laptop"
  }
}
```

![Consulta con joins](docs/capturas/evidencia_joins_prestamos_detalle.png)

![Filtros avanzados](docs/capturas/evidencia_filtros_avanzados.png)

![Historial por usuario](docs/capturas/evidencia_historial_usuario.png)

![Historial por dispositivo](docs/capturas/evidencia_historial_dispositivo.png)

## Devolución de un dispositivo

El flujo de devolución es:

1. Se valida que el préstamo exista.
2. Se rechaza la operación si ya tiene estado `returned`.
3. Se asigna la fecha de devolución.
4. Se actualiza el estado a `returned`.
5. Se cambia `Device.is_available` a `true`.

![Devolución y disponibilidad](docs/capturas/evidencia_devolucion_dispositivo.png)

## Swagger, ReDoc y OpenAPI

La API está organizada en los tags:

- `Users`
- `Devices`
- `Loans`

Los endpoints incluyen `summary`, `description`, `response_description`,
modelos de respuesta y ejemplos Pydantic.

![Swagger y OpenAPI](docs/capturas/evidencia_swagger_openapi_actualizado.png)

## Pruebas funcionales

La suite cubre los escenarios mínimos de la guía:

1. Ejecutar migraciones con Alembic.
2. Crear usuario.
3. Crear dispositivo.
4. Crear préstamo.
5. Intentar prestar un dispositivo no disponible.
6. Listar préstamos con información de usuario y dispositivo.
7. Filtrar préstamos por estado.
8. Filtrar préstamos por tipo de dispositivo.
9. Consultar préstamos de un usuario.
10. Devolver un dispositivo.
11. Verificar que el dispositivo vuelva a estar disponible.
12. Consultar el historial de préstamos del dispositivo.

Ejecutar:

```powershell
python -m pytest -q
```

Resultado validado: **10 pruebas aprobadas**.

## Evidencias anteriores conservadas

Las capturas de la actividad anterior se mantienen en `docs/capturas`, entre
ellas:

- `estructura_proyecto_01.png`
- `estructura_service_02.png`
- `creacion_usuario.png`
- `listar_usuarios.png`
- `actualizacion_completa.png`
- `actualizado_parcialmente.png`
- `eliminar_usuario.png`
- `Verificar SwaggerOpenAPI.png`
- `redoc.png`

## Autora

**Esthefany Valentina Chávez Parra**

Tecnología en Análisis y Desarrollo de Software (ADSO) - SENA
