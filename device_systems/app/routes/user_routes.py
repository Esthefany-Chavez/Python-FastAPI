from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies.user_dependencies import get_user_or_404
from app.schemas.user_schema import UserCreate, UserPatch, UserResponse, UserUpdate
from app.services.user_service import (
    create_user,
    delete_user,
    email_exists,
    get_all_users,
    get_user_by_email,
    patch_user,
    update_user,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get(
    "/",
    response_model=list[UserResponse],
    summary="Listar usuarios",
    description="Obtiene todos los usuarios registrados y permite filtrarlos por rol, estado y orden.",
    response_description="Lista de usuarios registrados",
)
def get_users(
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None),
    sort_by: str | None = Query(default="created_at"),
    db: Session = Depends(get_db),
):
    return get_all_users(db, role=role, is_active=is_active, sort_by=sort_by)


@router.get(
    "/email/{email}",
    response_model=UserResponse,
    summary="Buscar usuario por email",
    description="Busca un usuario por su correo electrónico.",
    response_description="Información del usuario encontrado",
)
def get_user_by_email_route(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Consultar usuario por ID",
    description="Obtiene la información de un usuario con base en su identificador.",
    response_description="Información del usuario solicitado",
)
def get_user(user=Depends(get_user_or_404)):
    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201,
    summary="Crear usuario",
    description="Registra un nuevo usuario en la base de datos.",
    response_description="Usuario creado correctamente",
)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    if email_exists(db, user.email):
        raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")
    return create_user(db, user)


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=200,
    summary="Actualizar usuario completamente",
    description="Reemplaza completamente la información de un usuario existente.",
    response_description="Usuario actualizado correctamente",
)
def update_complete_user(
    user_data: UserUpdate,
    user=Depends(get_user_or_404),
    db: Session = Depends(get_db),
):
    if email_exists(db, user_data.email, exclude_user_id=user.id):
        raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")
    return update_user(db, user.id, user_data)


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    status_code=200,
    summary="Actualizar usuario parcialmente",
    description="Modifica únicamente los campos enviados por el cliente.",
    response_description="Usuario actualizado parcialmente",
)
def update_partial_user(
    user_data: UserPatch,
    user=Depends(get_user_or_404),
    db: Session = Depends(get_db),
):
    update_data = user_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="Debe enviar al menos un campo para actualizar")

    if "email" in update_data and email_exists(db, update_data["email"], exclude_user_id=user.id):
        raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")

    return patch_user(db, user.id, update_data)


@router.delete(
    "/{user_id}",
    status_code=204,
    summary="Eliminar usuario",
    description="Elimina un usuario existente del sistema.",
    response_description="Usuario eliminado correctamente",
)
def remove_user(user=Depends(get_user_or_404), db: Session = Depends(get_db)):
    deleted = delete_user(db, user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return None