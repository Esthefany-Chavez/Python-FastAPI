from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.device_model import Device
from app.models.loan_model import Loan


def get_all_devices(
    db: Session,
    device_type: str | None = None,
    is_available: bool | None = None,
    brand: str | None = None,
    search: str | None = None,
    sort_by: str | None = "created_at",
):
    query = db.query(Device)

    if device_type is not None:
        query = query.filter(Device.device_type == device_type)

    if is_available is not None:
        query = query.filter(Device.is_available == is_available)

    if brand is not None:
        query = query.filter(Device.brand.ilike(f"%{brand}%"))

    if search is not None:
        query = query.filter(
            (Device.name.ilike(f"%{search}%"))
            | (Device.serial_number.ilike(f"%{search}%"))
            | (Device.device_type.ilike(f"%{search}%"))
        )

    if sort_by == "name":
        query = query.order_by(asc(Device.name))
    elif sort_by == "created_at":
        query = query.order_by(desc(Device.created_at))

    return query.all()


def get_device_by_id(db: Session, device_id: int):
    return db.query(Device).filter(Device.id == device_id).first()


def get_device_by_serial_number(db: Session, serial_number: str):
    return db.query(Device).filter(Device.serial_number == serial_number).first()


def create_device(db: Session, device_data):
    new_device = Device(
        name=device_data.name,
        serial_number=device_data.serial_number,
        device_type=device_data.device_type,
        brand=device_data.brand,
        is_available=device_data.is_available,
    )
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device


def update_device(db: Session, device_id: int, device_data):
    device = get_device_by_id(db, device_id)
    if device is None:
        return None

    device.name = device_data.name
    device.serial_number = device_data.serial_number
    device.device_type = device_data.device_type
    device.brand = device_data.brand
    device.is_available = device_data.is_available

    db.commit()
    db.refresh(device)
    return device


def patch_device(db: Session, device_id: int, update_data: dict):
    device = get_device_by_id(db, device_id)
    if device is None:
        return None

    for field, value in update_data.items():
        setattr(device, field, value)

    db.commit()
    db.refresh(device)
    return device


def delete_device(db: Session, device_id: int):
    device = get_device_by_id(db, device_id)
    if device is None:
        return False

    if db.query(Loan.id).filter(Loan.device_id == device_id).first() is not None:
        raise ValueError("No se puede eliminar un dispositivo con préstamos registrados")

    db.delete(device)
    db.commit()
    return True
