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
