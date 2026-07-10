import requests


BASE_URL = "https://dummyjson.com"


def test_login_user():
    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }

    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "accessToken" in data
    assert "refreshToken" in data

    assert data["id"] == 1
    assert data["username"] == "emilys"

    assert "email" in data
    assert "firstName" in data
    assert "lastName" in data

    assert data["email"] != ""
    assert data["firstName"] != ""
    assert data["lastName"] != ""


def test_get_current_auth_user():
    login_payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }

    login_response = requests.post(f"{BASE_URL}/auth/login", json=login_payload)

    assert login_response.status_code == 200

    login_data = login_response.json()

    assert "accessToken" in login_data

    access_token = login_data["accessToken"]

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(f"{BASE_URL}/auth/me", headers=headers)

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == login_data["id"]
    assert user["username"] == login_data["username"]
    assert user["email"] == login_data["email"]

    assert "firstName" in user
    assert "lastName" in user
    assert "role" in user

    assert user["firstName"] != ""
    assert user["lastName"] != ""
    assert user["role"] != ""
