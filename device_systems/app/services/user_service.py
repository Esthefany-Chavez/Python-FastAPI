from app.data.users_db import users


def get_all_users():
    return users


def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def create_user(user_data):
    new_id = max([user["id"] for user in users], default=0) + 1

    new_user = {
        "id": new_id,
        "name": user_data.name,
        "email": user_data.email,
        "role": user_data.role,
        "is_active": user_data.is_active
    }

    users.append(new_user)

    return new_user


def email_exists(email: str, exclude_user_id: int | None = None):
    for user in users:
        if user["email"] == email and user["id"] != exclude_user_id:
            return True

    return False


def update_user(user_id: int, user_data):
    user = get_user_by_id(user_id)

    if user is None:
        return None

    user["name"] = user_data.name
    user["email"] = user_data.email
    user["role"] = user_data.role
    user["is_active"] = user_data.is_active

    return user


def patch_user(user_id: int, update_data: dict):
    user = get_user_by_id(user_id)

    if user is None:
        return None

    user.update(update_data)

    return user


def delete_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        return False

    users.remove(user)

    return True