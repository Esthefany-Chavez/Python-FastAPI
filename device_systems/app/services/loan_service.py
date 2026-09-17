from datetime import datetime

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from app.models.device_model import Device
from app.models.loan_model import Loan
from app.models.user_model import User


def get_all_loans(
    db: Session,
    status: str | None = None,
    user_email: str | None = None,
    device_type: str | None = None,
    search: str | None = None,
):
    query = db.query(Loan)

    if status is not None:
        query = query.filter(Loan.status == status)

    if user_email is not None:
        query = query.join(User, Loan.user_id == User.id).filter(User.email.ilike(f"%{user_email}%"))

    if device_type is not None:
        query = query.join(Device, Loan.device_id == Device.id).filter(Device.device_type.ilike(f"%{device_type}%"))

    if search is not None:
        query = query.join(User, Loan.user_id == User.id).join(Device, Loan.device_id == Device.id).filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                Device.name.ilike(f"%{search}%"),
                Device.serial_number.ilike(f"%{search}%"),
            )
        )

    return query.all()


def get_loan_by_id(db: Session, loan_id: int):
    return db.query(Loan).filter(Loan.id == loan_id).first()


def get_loans_with_details(
    db: Session,
    status: str | None = None,
    user_email: str | None = None,
    device_type: str | None = None,
    search: str | None = None,
    user_id: int | None = None,
    device_id: int | None = None,
):
    query = (
        db.query(
            Loan.id.label("loan_id"),
            Loan.user_id,
            Loan.device_id,
            Loan.loan_date,
            Loan.return_date,
            Loan.status,
            User.id.label("user_model_id"),
            User.name.label("user_name"),
            User.email.label("user_email"),
            Device.id.label("device_model_id"),
            Device.name.label("device_name"),
            Device.serial_number,
            Device.device_type,
        )
        .join(User, Loan.user_id == User.id)
        .join(Device, Loan.device_id == Device.id)
    )

    filters = []

    if status is not None:
        filters.append(Loan.status == status)
    if user_email is not None:
        filters.append(User.email.ilike(f"%{user_email}%"))
    if device_type is not None:
        filters.append(Device.device_type.ilike(f"%{device_type}%"))
    if user_id is not None:
        filters.append(User.id == user_id)
    if device_id is not None:
        filters.append(Device.id == device_id)
    if search is not None:
        filters.append(
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                Device.name.ilike(f"%{search}%"),
                Device.serial_number.ilike(f"%{search}%"),
                Device.device_type.ilike(f"%{search}%"),
            )
        )

    if filters:
        query = query.filter(and_(*filters))

    rows = query.all()
    return [
        {
            "loan_id": row.loan_id,
            "user_id": row.user_id,
            "device_id": row.device_id,
            "loan_date": row.loan_date,
            "return_date": row.return_date,
            "status": row.status,
            "user": {
                "id": row.user_model_id,
                "name": row.user_name,
                "email": row.user_email,
                "role": "user",
                "is_active": True,
                "created_at": datetime.utcnow(),
            },
            "device": {
                "id": row.device_model_id,
                "name": row.device_name,
                "serial_number": row.serial_number,
                "device_type": row.device_type,
                "brand": None,
                "is_available": True,
                "created_at": datetime.utcnow(),
            },
        }
        for row in rows
    ]


def get_user_loans(db: Session, user_id: int, status: str | None = None):
    return get_loans_with_details(db, user_id=user_id, status=status)


def get_device_loans(db: Session, device_id: int, status: str | None = None):
    return get_loans_with_details(db, device_id=device_id, status=status)


def create_loan(db: Session, loan_data):
    user = db.query(User).filter(User.id == loan_data.user_id).first()
    if user is None:
        raise ValueError("Usuario no encontrado")

    device = db.query(Device).filter(Device.id == loan_data.device_id).first()
    if device is None:
        raise ValueError("Dispositivo no encontrado")

    if not device.is_available:
        raise ValueError("El dispositivo no está disponible")

    loan = Loan(
        user_id=loan_data.user_id,
        device_id=loan_data.device_id,
        loan_date=loan_data.loan_date,
        return_date=loan_data.return_date,
        status=loan_data.status,
    )

    device.is_available = False

    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan


def return_loan(db: Session, loan_id: int):
    loan = get_loan_by_id(db, loan_id)
    if loan is None:
        raise ValueError("Préstamo no encontrado")

    if loan.status == "returned":
        raise ValueError("El préstamo ya fue devuelto")

    loan.status = "returned"
    loan.return_date = datetime.utcnow()

    device = db.query(Device).filter(Device.id == loan.device_id).first()
    if device is not None:
        device.is_available = True

    db.commit()
    db.refresh(loan)
    return loan
