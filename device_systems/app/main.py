from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Request
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.connection import create_tables, get_db
from app.routes.device_routes import router as device_router
from app.routes.loan_routes import router as loan_router
from app.routes.user_routes import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="device_systems API",
    description=(
        "API REST para la gestión de usuarios, dispositivos y préstamos del sistema device_systems. "
        "Incluye operaciones CRUD, filtros, validación de datos, joins de información y manejo de errores."
    ),
    version="2.0.0",
    lifespan=lifespan,
    contact={
        "name": "Esthefany Valentina Chávez Parra",
    },
    openapi_tags=[
        {"name": "Users", "description": "Gestión de usuarios del sistema."},
        {"name": "Devices", "description": "Gestión y consulta de dispositivos disponibles para préstamo."},
        {"name": "Loans", "description": "Gestión de préstamos, devoluciones y consultas combinadas."},
    ],
)


app.include_router(user_router)
app.include_router(device_router)
app.include_router(loan_router)


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
    response_description="Mensaje de confirmación",
)
def root():
    return {"message": "device_systems API funcionando"}


@app.get("/test-db/", summary="Verificar conexión con SQLite")
def test_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"database": "conectada"}