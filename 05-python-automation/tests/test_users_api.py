import requests


BASE_URL = "https://dummyjson.com"


def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    data = response.json()

    assert "users" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0

    first_user = data["users"][0]

    assert "id" in first_user
    assert "firstName" in first_user
    assert "lastName" in first_user
    assert "email" in first_user
    assert "username" in first_user
    assert "role" in first_user

    assert first_user["firstName"] != ""
    assert first_user["lastName"] != ""
    assert "@" in first_user["email"]

    user_ids = [user["id"] for user in data["users"]]

    assert len(user_ids) == len(set(user_ids))
    assert 5 in user_ids
