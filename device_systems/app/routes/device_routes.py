from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies.device_dependencies import get_device_or_404
from app.schemas.device_schema import DeviceCreate, DevicePatch, DeviceResponse, DeviceUpdate
from app.schemas.loan_schema import LoanDetailResponse
from app.services.device_service import (
    create_device,
    delete_device,
    get_all_devices,
    get_device_by_serial_number,
    patch_device,
    update_device,
)
from app.services.loan_service import get_device_loans

router = APIRouter(prefix="/devices", tags=["Devices"])


@router.get(
    "/",
    response_model=list[DeviceResponse],
    summary="Listar dispositivos",
    description="Obtiene todos los dispositivos registrados con filtros por tipo, disponibilidad, marca y búsqueda textual.",
    response_description="Lista de dispositivos disponibles en el sistema.",
)
def get_devices(
    device_type: str | None = Query(default=None),
    is_available: bool | None = Query(default=None),
    brand: str | None = Query(default=None),
    search: str | None = Query(default=None),
    sort_by: str | None = Query(default="created_at"),
    db: Session = Depends(get_db),
):
    return get_all_devices(
        db,
        device_type=device_type,
        is_available=is_available,
        brand=brand,
        search=search,
        sort_by=sort_by,
    )


@router.get(
    "/{device_id}",
    response_model=DeviceResponse,
    summary="Consultar dispositivo por ID",
    description="Consulta la información completa de un equipo tecnológico por su identificador.",
    response_description="Dispositivo encontrado.",
)
def get_device(device=Depends(get_device_or_404)):
    return device


@router.get(
    "/{device_id}/loans",
    response_model=list[LoanDetailResponse],
    summary="Consultar préstamos de un dispositivo",
)
def get_device_loans_route(
    device=Depends(get_device_or_404),
    status: Literal["active", "returned", "overdue"] | None = Query(default=None),
    db: Session = Depends(get_db),
):
    return get_device_loans(db, device_id=device.id, status=status)


@router.post(
    "/",
    response_model=DeviceResponse,
    status_code=201,
    summary="Crear dispositivo",
    description="Registra un equipo tecnológico con su número de serie, tipo, marca y disponibilidad inicial.",
    response_description="Dispositivo creado correctamente.",
)
def create_new_device(device_data: DeviceCreate, db: Session = Depends(get_db)):
    if get_device_by_serial_number(db, device_data.serial_number):
        raise HTTPException(status_code=400, detail="El número de serie ya existe")
    return create_device(db, device_data)


@router.put(
    "/{device_id}",
    response_model=DeviceResponse,
    summary="Actualizar dispositivo completamente",
)
def update_complete_device(
    device_data: DeviceUpdate,
    device=Depends(get_device_or_404),
    db: Session = Depends(get_db),
):
    if device_data.serial_number != device.serial_number:
        existing = get_device_by_serial_number(db, device_data.serial_number)
        if existing:
            raise HTTPException(status_code=400, detail="El número de serie ya existe")

    return update_device(db, device.id, device_data)


@router.patch(
    "/{device_id}",
    response_model=DeviceResponse,
    summary="Actualizar dispositivo parcialmente",
)
def update_partial_device(
    device_data: DevicePatch,
    device=Depends(get_device_or_404),
    db: Session = Depends(get_db),
):
    update_data = device_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(status_code=400, detail="Debe enviar al menos un campo para actualizar")

    if "serial_number" in update_data:
        existing = get_device_by_serial_number(db, update_data["serial_number"])
        if existing and existing.id != device.id:
            raise HTTPException(status_code=400, detail="El número de serie ya existe")

    return patch_device(db, device.id, update_data)


@router.delete(
    "/{device_id}",
    status_code=204,
    summary="Eliminar dispositivo",
)
def remove_device(device=Depends(get_device_or_404), db: Session = Depends(get_db)):
    deleted = delete_device(db, device.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return None