import pytest #type: ignore
from fastapi.testclient import TestClient

from app.database.connection import SessionLocal
from app.main import app
from app.models.user_model import User
from app.services.user_service import create_user, email_exists, get_user_by_email

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_users():
    with SessionLocal() as db:
        db.query(User).delete()
        db.commit()
    yield
    with SessionLocal() as db:
        db.query(User).delete()
        db.commit()


def test_create_list_filter_and_get_by_id():
    payload = {
        'name': 'Ana Gómez',
        'email': 'ana@example.com',
        'role': 'admin',
        'is_active': True,
    }

    created = client.post('/users/', json=payload)
    assert created.status_code == 201, created.text
    data = created.json()
    assert data['email'] == 'ana@example.com'
    assert data['role'] == 'admin'

    list_response = client.get('/users/')
    assert list_response.status_code == 200
    assert any(item['id'] == data['id'] for item in list_response.json())

    by_role = client.get('/users/', params={'role': 'admin'})
    assert by_role.status_code == 200
    assert any(item['id'] == data['id'] for item in by_role.json())

    by_state = client.get('/users/', params={'is_active': True})
    assert by_state.status_code == 200
    assert any(item['id'] == data['id'] for item in by_state.json())

    fetched = client.get(f"/users/{data['id']}")
    assert fetched.status_code == 200
    assert fetched.json()['name'] == 'Ana Gómez'

    with SessionLocal() as db:
        assert get_user_by_email(db, 'ana@example.com') is not None
        assert email_exists(db, 'ana@example.com') is True


def test_duplicate_email_and_invalid_payloads():
    payload = {
        'name': 'Luis Pérez',
        'email': 'luis@example.com',
        'role': 'support',
        'is_active': True,
    }

    first = client.post('/users/', json=payload)
    assert first.status_code == 201

    duplicate = client.post('/users/', json=payload)
    assert duplicate.status_code == 400
    assert 'correo' in duplicate.json()['detail'].lower()

    invalid_role = client.post('/users/', json={
        'name': 'X',
        'email': 'bad@example.com',
        'role': 'guest',
        'is_active': True,
    })
    assert invalid_role.status_code == 422

    invalid_email = client.post('/users/', json={
        'name': 'Name User',
        'email': 'not-an-email',
        'role': 'user',
        'is_active': True,
    })
    assert invalid_email.status_code == 422


def test_update_user_full_and_partial():
    payload = {
        'name': 'María López',
        'email': 'maria@example.com',
        'role': 'user',
        'is_active': True,
    }

    created = client.post('/users/', json=payload)
    assert created.status_code == 201
    user_id = created.json()['id']

    full_update = client.put(
        f'/users/{user_id}',
        json={
            'name': 'María Actualizada',
            'email': 'maria.nueva@example.com',
            'role': 'support',
            'is_active': False,
        },
    )
    assert full_update.status_code == 200
    assert full_update.json()['role'] == 'support'
    assert full_update.json()['is_active'] is False

    partial_update = client.patch(
        f'/users/{user_id}',
        json={'name': 'María Parcial'},
    )
    assert partial_update.status_code == 200
    assert partial_update.json()['name'] == 'María Parcial'

    empty_patch = client.patch(f'/users/{user_id}', json={})
    assert empty_patch.status_code == 400

    email_lookup = client.get('/users/email/maria.nueva@example.com')
    assert email_lookup.status_code == 200
    assert email_lookup.json()['email'] == 'maria.nueva@example.com'


def test_delete_and_missing_users():
    payload = {
        'name': 'Pedro Ruiz',
        'email': 'pedro@example.com',
        'role': 'admin',
        'is_active': True,
    }

    created = client.post('/users/', json=payload)
    assert created.status_code == 201
    user_id = created.json()['id']

    delete_response = client.delete(f'/users/{user_id}')
    assert delete_response.status_code in (200, 204)

    missing_get = client.get(f'/users/{user_id}')
    assert missing_get.status_code == 404

    missing_delete = client.delete(f'/users/{user_id}')
    assert missing_delete.status_code == 404

    missing_update = client.put(
        f'/users/{user_id}',
        json={
            'name': 'Inexistente',
            'email': 'nada@example.com',
            'role': 'user',
            'is_active': True,
        },
    )
    assert missing_update.status_code == 404


def test_ordering_and_service_helpers():
    first = client.post('/users/', json={
        'name': 'Zoe',
        'email': 'zoe@example.com',
        'role': 'user',
        'is_active': True,
    })
    second = client.post('/users/', json={
        'name': 'Ana',
        'email': 'ana2@example.com',
        'role': 'support',
        'is_active': False,
    })

    assert first.status_code == 201
    assert second.status_code == 201

    ordered_name = client.get('/users/', params={'sort_by': 'name'})
    assert ordered_name.status_code == 200
    names = [u['name'] for u in ordered_name.json()]
    assert names == sorted(names)

    ordered_created = client.get('/users/', params={'sort_by': 'created_at'})
    assert ordered_created.status_code == 200

    with SessionLocal() as db:
        created_user = create_user(db, type('Payload', (), {
            'name': 'Test Service',
            'email': 'service@example.com',
            'role': 'admin',
            'is_active': True,
        })())
        assert created_user.id is not None
        assert get_user_by_email(db, 'service@example.com').email == 'service@example.com'
        assert email_exists(db, 'service@example.com') is True

