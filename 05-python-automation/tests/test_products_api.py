import requests


BASE_URL = "https://dummyjson.com"


def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200

    data = response.json()

    assert "products" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["products"], list)
    assert len(data["products"]) > 0

    first_product = data["products"][0]

    assert "id" in first_product
    assert "title" in first_product
    assert "category" in first_product
    assert "price" in first_product
