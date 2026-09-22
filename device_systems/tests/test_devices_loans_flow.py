import pytest
from fastapi.testclient import TestClient

from app.database.connection import SessionLocal
from app.main import app
from app.models.device_model import Device
from app.models.loan_model import Loan
from app.models.user_model import User

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_related_data():
    with SessionLocal() as db:
        db.query(Loan).delete()
        db.query(Device).delete()
        db.query(User).delete()
        db.commit()
    yield
    with SessionLocal() as db:
        db.query(Loan).delete()
        db.query(Device).delete()
        db.query(User).delete()
        db.commit()


def test_openapi_docs_and_tags():
    docs = client.get("/docs")
    redoc = client.get("/redoc")
    openapi = client.get("/openapi.json")

    assert docs.status_code == 200
    assert redoc.status_code == 200
    assert openapi.status_code == 200

    tags = [tag["name"] for tag in openapi.json()["tags"]]
    assert "Users" in tags
    assert "Devices" in tags
    assert "Loans" in tags


def test_create_user_device_loan_and_unavailable_device():
    user_payload = {
        "name": "Ana Pérez",
        "email": "ana@sena.edu.co",
        "role": "user",
        "is_active": True,
    }
    device_payload = {
        "name": "Laptop Lenovo ThinkPad",
        "serial_number": "LEN-2024-001",
        "device_type": "laptop",
        "brand": "Lenovo",
        "is_available": True,
    }
    loan_payload = {
        "user_id": 1,
        "device_id": 1,
        "loan_date": "2026-09-17T09:00:00",
        "return_date": None,
        "status": "active",
    }

    user_response = client.post("/users/", json=user_payload)
    assert user_response.status_code == 201, user_response.text
    user_id = user_response.json()["id"]

    device_response = client.post("/devices/", json=device_payload)
    assert device_response.status_code == 201, device_response.text
    device_id = device_response.json()["id"]

    loan_payload["user_id"] = user_id
    loan_payload["device_id"] = device_id

    loan_response = client.post("/loans/", json=loan_payload)
    assert loan_response.status_code == 201, loan_response.text
    loan_id = loan_response.json()["id"]

    duplicate_loan = client.post("/loans/", json=loan_payload)
    assert duplicate_loan.status_code == 409, duplicate_loan.text

    details = client.get("/loans/details")
    assert details.status_code == 200
    assert any(item["loan_id"] == loan_id for item in details.json())

    user_loans = client.get(f"/users/{user_id}/loans")
    assert user_loans.status_code == 200
    assert any(item["loan_id"] == loan_id for item in user_loans.json())

    device_loans = client.get(f"/devices/{device_id}/loans")
    assert device_loans.status_code == 200
    assert any(item["loan_id"] == loan_id for item in device_loans.json())


def test_filter_loans_by_status_and_device_type():
    user_response = client.post(
        "/users/",
        json={"name": "Pedro Ruiz", "email": "pedro@sena.edu.co", "role": "support", "is_active": True},
    )
    device_response = client.post(
        "/devices/",
        json={
            "name": "Tablet Samsung",
            "serial_number": "SAM-2024-005",
            "device_type": "tablet",
            "brand": "Samsung",
            "is_available": True,
        },
    )
    user_id = user_response.json()["id"]
    device_id = device_response.json()["id"]

    client.post(
        "/loans/",
        json={
            "user_id": user_id,
            "device_id": device_id,
            "loan_date": "2026-09-17T10:00:00",
            "return_date": None,
            "status": "active",
        },
    )

    status_filter = client.get("/loans/", params={"status": "active"})
    assert status_filter.status_code == 200
    assert len(status_filter.json()) >= 1

    device_type_filter = client.get("/loans/", params={"device_type": "tablet"})
    assert device_type_filter.status_code == 200
    assert len(device_type_filter.json()) >= 1

    email_filter = client.get("/loans/", params={"user_email": "pedro@sena.edu.co"})
    assert email_filter.status_code == 200
    assert len(email_filter.json()) >= 1


def test_combined_loan_filters_return_real_related_data():
    user_response = client.post(
        "/users/",
        json={"name": "Maria Gomez", "email": "maria@sena.edu.co", "role": "support", "is_active": False},
    )
    device_response = client.post(
        "/devices/",
        json={
            "name": "Laptop Lenovo",
            "serial_number": "LEN-COMBINED-01",
            "device_type": "laptop",
            "brand": "Lenovo",
            "is_available": True,
        },
    )

    loan_response = client.post(
        "/loans/",
        json={
            "user_id": user_response.json()["id"],
            "device_id": device_response.json()["id"],
            "loan_date": "2026-09-17T11:00:00",
            "status": "active",
        },
    )
    assert loan_response.status_code == 201, loan_response.text

    filtered = client.get(
        "/loans/",
        params={
            "user_email": "maria@sena.edu.co",
            "device_type": "laptop",
            "search": "lenovo",
        },
    )
    assert filtered.status_code == 200, filtered.text
    assert len(filtered.json()) == 1

    details = client.get("/loans/details").json()[0]
    assert details["user"]["role"] == "support"
    assert details["user"]["is_active"] is False
    assert details["device"]["brand"] == "Lenovo"
    assert details["device"]["is_available"] is False


def test_return_loan_and_make_device_available_again():
    user_response = client.post(
        "/users/",
        json={"name": "Luis Torres", "email": "luis@sena.edu.co", "role": "user", "is_active": True},
    )
    device_response = client.post(
        "/devices/",
        json={
            "name": "Monitor Dell",
            "serial_number": "DEL-9090-77",
            "device_type": "monitor",
            "brand": "Dell",
            "is_available": True,
        },
    )
    user_id = user_response.json()["id"]
    device_id = device_response.json()["id"]

    loan_response = client.post(
        "/loans/",
        json={
            "user_id": user_id,
            "device_id": device_id,
            "loan_date": "2026-09-17T12:00:00",
            "return_date": None,
            "status": "active",
        },
    )
    loan_id = loan_response.json()["id"]

    return_response = client.patch(f"/loans/{loan_id}/return")
    assert return_response.status_code == 200, return_response.text
    assert return_response.json()["status"] == "returned"

    device_after = client.get(f"/devices/{device_id}")
    assert device_after.status_code == 200
    assert device_after.json()["is_available"] is True

    history = client.get(f"/devices/{device_id}/loans")
    assert history.status_code == 200
    assert any(item["status"] == "returned" for item in history.json())

    repeated_return = client.patch(f"/loans/{loan_id}/return")
    assert repeated_return.status_code == 409
