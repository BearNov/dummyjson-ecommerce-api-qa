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


def test_get_product_by_id():
    response = requests.get(f"{BASE_URL}/products/1")

    assert response.status_code == 200

    product = response.json()

    assert product["id"] == 1

    assert "title" in product
    assert "category" in product
    assert "price" in product
    assert "stock" in product

    assert product["title"] != ""
    assert product["category"] != ""

    assert isinstance(product["price"], (int, float))
    assert product["price"] >= 0
