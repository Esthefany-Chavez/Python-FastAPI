from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies.user_dependencies import get_user_or_404
from app.schemas.user_schema import (
    UserCreate,
    UserPatch,
    UserResponse,
    UserUpdate
)
from app.services.user_service import (
    create_user,
    delete_user,
    email_exists,
    get_all_users,
    patch_user,
    update_user
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/",
    response_model=list[UserResponse],
    summary="Listar usuarios",
    description="Obtiene todos los usuarios registrados y permite filtrarlos por rol o estado.",
    response_description="Lista de usuarios registrados"
)
def get_users(
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None)
):
    users = get_all_users()

    if role is not None:
        users = [user for user in users if user["role"] == role]

    if is_active is not None:
        users = [user for user in users if user["is_active"] == is_active]

    return users


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Consultar usuario por ID",
    description="Obtiene la información de un usuario utilizando su identificador.",
    response_description="Información del usuario solicitado"
)
def get_user(user=Depends(get_user_or_404)):
    return user


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201,
    summary="Crear usuario",
    description="Registra un nuevo usuario en el sistema.",
    response_description="Usuario creado correctamente"
)
def create_new_user(user: UserCreate):

    if email_exists(user.email):
        raise HTTPException(
            status_code=400,
            detail="El correo electrónico ya está registrado"
        )

    return create_user(user)


@router.put(
    "/{user_id}",
    response_model=UserResponse,
    status_code=200,
    summary="Actualizar usuario completamente",
    description="Reemplaza completamente la información de un usuario existente.",
    response_description="Usuario actualizado correctamente"
)
def update_complete_user(
    user_data: UserUpdate,
    user=Depends(get_user_or_404)
):
    if email_exists(user_data.email, exclude_user_id=user["id"]):
        raise HTTPException(
            status_code=400,
            detail="El correo electrónico ya está registrado"
        )

    return update_user(user["id"], user_data)


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    status_code=200,
    summary="Actualizar usuario parcialmente",
    description="Modifica únicamente los campos enviados por el cliente.",
    response_description="Usuario actualizado parcialmente"
)
def update_partial_user(
    user_data: UserPatch,
    user=Depends(get_user_or_404)
):
    update_data = user_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="Debe enviar al menos un campo para actualizar"
        )

    if "email" in update_data:
        if email_exists(
            update_data["email"],
            exclude_user_id=user["id"]
        ):
            raise HTTPException(
                status_code=400,
                detail="El correo electrónico ya está registrado"
            )

    return patch_user(user["id"], update_data)


@router.delete(
    "/{user_id}",
    status_code=204,
    summary="Eliminar usuario",
    description="Elimina un usuario existente del sistema.",
    response_description="Usuario eliminado correctamente"
)
def remove_user(user=Depends(get_user_or_404)):
    delete_user(user["id"])
    return None