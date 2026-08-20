from fastapi import FastAPI  # type: ignore[import-not-found]
from pydantic import BaseModel  # type: ignore[import-not-found]
from fastapi import HTTPException, status  # type: ignore[import-not-found]

app = FastAPI()

# @app.get("/")
# def read_root():
#    return {"Mensaje": "Hola, Mundo"}



class Estudiantes(BaseModel):
    nombre: str
    edad: int
    curso: str

@app.post("/estudiantes/")
def crear_estudiante(estudiante: Estudiantes):
    return estudiante

@app.get("/estudiantes/{id}")
def obtener_estudiante(id: int):
    if id not in base_datos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Estudiante no encontrado"
            )
    return base_datos[id]