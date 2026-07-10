import requests


BASE_URL = "https://dummyjson.com"


def test_get_all_carts():
    response = requests.get(f"{BASE_URL}/carts")

    assert response.status_code == 200

    data = response.json()

    assert "carts" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["carts"], list)
    assert len(data["carts"]) > 0

    first_cart = data["carts"][0]

    assert "id" in first_cart
    assert "products" in first_cart
    assert "total" in first_cart
    assert "discountedTotal" in first_cart
    assert "userId" in first_cart
    assert "totalProducts" in first_cart
    assert "totalQuantity" in first_cart

    assert isinstance(first_cart["products"], list)
    assert len(first_cart["products"]) > 0

    calculated_total_products = len(first_cart["products"])
    calculated_total_quantity = sum(
        product["quantity"] for product in first_cart["products"]
    )

    assert first_cart["totalProducts"] == calculated_total_products
    assert first_cart["totalQuantity"] == calculated_total_quantity
