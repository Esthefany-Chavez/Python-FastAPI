from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies.loan_dependencies import get_loan_or_404
from app.models.user_model import User
from app.schemas.loan_schema import LoanCreate, LoanDetailResponse, LoanResponse
from app.services.loan_service import (
    create_loan,
    get_all_loans,
    get_device_loans,
    get_loans_with_details,
    get_user_loans,
    return_loan,
)

router = APIRouter(prefix="/loans", tags=["Loans"])


@router.get(
    "/",
    response_model=list[LoanResponse],
    summary="Listar préstamos",
    description="Obtiene los préstamos registrados y permite filtrar por estado, correo del usuario, tipo de dispositivo o texto libre.",
    response_description="Listado de préstamos.",
)
def get_loans(
    status: Literal["active", "returned", "overdue"] | None = Query(default=None),
    user_email: str | None = Query(default=None),
    device_type: str | None = Query(default=None),
    search: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    return get_all_loans(db, status=status, user_email=user_email, device_type=device_type, search=search)


@router.get(
    "/details",
    response_model=list[LoanDetailResponse],
    summary="Consultar préstamos con información de usuario y dispositivo",
)
def get_loans_details(
    status: Literal["active", "returned", "overdue"] | None = Query(default=None),
    user_email: str | None = Query(default=None),
    device_type: str | None = Query(default=None),
    search: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    return get_loans_with_details(
        db,
        status=status,
        user_email=user_email,
        device_type=device_type,
        search=search,
    )


@router.get(
    "/{loan_id}",
    response_model=LoanDetailResponse,
    summary="Consultar préstamo por ID",
    description="Retorna el préstamo junto con la información del usuario y del dispositivo asociado.",
    response_description="Préstamo con datos relacionados.",
)
def get_loan(loan=Depends(get_loan_or_404), db: Session = Depends(get_db)):
    rows = get_loans_with_details(db, user_id=loan.user_id, device_id=loan.device_id)
    for item in rows:
        if item["loan_id"] == loan.id:
            return item
    raise HTTPException(status_code=404, detail="Préstamo no encontrado")


@router.get(
    "/users/{user_id}",
    response_model=list[LoanDetailResponse],
    summary="Consultar préstamos por usuario",
)
def get_user_loan_details(
    user_id: int,
    status: Literal["active", "returned", "overdue"] | None = Query(default=None),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return get_user_loans(db, user_id=user_id, status=status)


@router.get(
    "/devices/{device_id}",
    response_model=list[LoanDetailResponse],
    summary="Consultar préstamos por dispositivo",
)
def get_device_loan_details(
    device_id: int,
    status: Literal["active", "returned", "overdue"] | None = Query(default=None),
    db: Session = Depends(get_db),
):
    from app.models.device_model import Device as DeviceModel

    device = db.query(DeviceModel).filter(DeviceModel.id == device_id).first()
    if device is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return get_device_loans(db, device_id=device_id, status=status)


@router.post(
    "/",
    response_model=LoanResponse,
    status_code=201,
    summary="Crear préstamo",
    description="Crea un préstamo validando que el usuario y el dispositivo existan y que el equipo esté disponible.",
    response_description="Préstamo registrado correctamente.",
)
def create_new_loan(loan_data: LoanCreate, db: Session = Depends(get_db)):
    try:
        return create_loan(db, loan_data)
    except ValueError as exc:
        if str(exc) == "Usuario no encontrado":
            raise HTTPException(status_code=404, detail=str(exc))
        if str(exc) == "Dispositivo no encontrado":
            raise HTTPException(status_code=404, detail=str(exc))
        if str(exc) == "El dispositivo no está disponible":
            raise HTTPException(status_code=409, detail=str(exc))
        raise HTTPException(status_code=400, detail=str(exc))


@router.patch(
    "/{loan_id}/return",
    response_model=LoanResponse,
    summary="Registrar devolución del préstamo",
    description="Marca el préstamo como devuelto, registra la fecha de devolución y vuelve a dejar disponible el dispositivo.",
    response_description="Devolución registrada correctamente.",
)
def return_loan_route(loan=Depends(get_loan_or_404), db: Session = Depends(get_db)):
    try:
        return return_loan(db, loan.id)
    except ValueError as exc:
        if str(exc) == "Préstamo no encontrado":
            raise HTTPException(status_code=404, detail=str(exc))
        if str(exc) == "El préstamo ya fue devuelto":
            raise HTTPException(status_code=409, detail=str(exc))
        raise HTTPException(status_code=400, detail=str(exc))
