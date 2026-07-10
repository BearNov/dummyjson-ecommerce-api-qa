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


def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1

    assert "firstName" in user
    assert "lastName" in user
    assert "email" in user
    assert "username" in user
    assert "role" in user

    assert user["firstName"] != ""
    assert user["lastName"] != ""
    assert "@" in user["email"]

    assert "address" in user
    assert isinstance(user["address"], dict)

    assert "city" in user["address"]
    assert "country" in user["address"]

    assert "company" in user
    assert isinstance(user["company"], dict)

    assert "name" in user["company"]
    assert "department" in user["company"]
