from fastapi import APIRouter, HTTPException, Query
from app.schemas.user_schema import UserCreate, UserResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


users = [
    {
        "id": 1,
        "name": "Juan Pérez",
        "email": "juan@gmail.com",
        "role": "admin",
        "is_active": True
    },
    {
        "id": 2,
        "name": "María López",
        "email": "maria@gmail.com",
        "role": "support",
        "is_active": True
    },
    {
        "id": 3,
        "name": "Carlos Gómez",
        "email": "carlos@gmail.com",
        "role": "user",
        "is_active": False
    }
]


@router.get("/", response_model=list[UserResponse])
def get_users(
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None)
):
    result = users

    if role is not None:
        result = [user for user in result if user["role"] == role]

    if is_active is not None:
        result = [user for user in result if user["is_active"] == is_active]

    return result


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado"
    )


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):

    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=409,
                detail="El correo electrónico ya está registrado"
            )

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "is_active": user.is_active
    }

    users.append(new_user)

    return new_user