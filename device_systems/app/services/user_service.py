from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.models.user_model import User


def get_all_users(
    db: Session,
    role: str | None = None,
    is_active: bool | None = None,
    sort_by: str | None = "created_at",
):
    query = db.query(User)

    if role is not None:
        query = query.filter(User.role == role)

    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    if sort_by == "name":
        query = query.order_by(asc(User.name))
    elif sort_by == "created_at":
        query = query.order_by(desc(User.created_at))

    return query.all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_data):
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
        is_active=user_data.is_active,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def email_exists(db: Session, email: str, exclude_user_id: int | None = None):
    query = db.query(User).filter(User.email == email)
    if exclude_user_id is not None:
        query = query.filter(User.id != exclude_user_id)
    return query.first() is not None


def update_user(db: Session, user_id: int, user_data):
    user = get_user_by_id(db, user_id)
    if user is None:
        return None

    user.name = user_data.name
    user.email = user_data.email
    user.role = user_data.role
    user.is_active = user_data.is_active

    db.commit()
    db.refresh(user)
    return user


def patch_user(db: Session, user_id: int, update_data: dict):
    user = get_user_by_id(db, user_id)
    if user is None:
        return None

    for field, value in update_data.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user is None:
        return False

    db.delete(user)
    db.commit()
    return True