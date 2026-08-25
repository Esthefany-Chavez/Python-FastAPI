from fastapi import FastAPI, Request

from app.routes.user_routes import router as user_router


app = FastAPI(
    title="device_systems API",
    description=(
        "API REST para la gestión de usuarios del sistema device_systems. "
        "Incluye operaciones CRUD, validación de datos, manejo de errores "
        "y Dependency Injection."
    ),
    version="2.0.0",
    contact={
        "name": "Esthefany Valentina Chávez Parra",
    },
    openapi_tags=[
        {
            "name": "Users",
            "description": "Operaciones CRUD para la gestión de usuarios."
        }
    ]
)


app.include_router(user_router)


@app.middleware("http")
async def add_custom_headers(request: Request, call_next):

    response = await call_next(request)

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "2.0"

    return response


@app.get(
    "/",
    summary="Verificar estado de la API",
    description="Comprueba que la API device_systems se encuentre funcionando.",
    response_description="Mensaje de confirmación"
)
def root():
    return {
        "message": "device_systems API funcionando"
    }