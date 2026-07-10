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


def test_get_cart_by_id():
    response = requests.get(f"{BASE_URL}/carts/1")

    assert response.status_code == 200

    cart = response.json()

    assert cart["id"] == 1

    assert "products" in cart
    assert "total" in cart
    assert "discountedTotal" in cart
    assert "userId" in cart
    assert "totalProducts" in cart
    assert "totalQuantity" in cart

    assert isinstance(cart["products"], list)
    assert len(cart["products"]) > 0

    calculated_total_products = len(cart["products"])
    calculated_total_quantity = sum(
        product["quantity"] for product in cart["products"]
    )
    calculated_total = sum(
        product["total"] for product in cart["products"]
    )
    calculated_discounted_total = sum(
        product["discountedTotal"] for product in cart["products"]
    )

    assert cart["totalProducts"] == calculated_total_products
    assert cart["totalQuantity"] == calculated_total_quantity
    assert round(cart["total"], 2) == round(calculated_total, 2)
    assert round(cart["discountedTotal"], 2) == round(calculated_discounted_total, 2)


def test_get_carts_by_user():
    user_id = 5

    response = requests.get(f"{BASE_URL}/carts/user/{user_id}")

    assert response.status_code == 200

    data = response.json()

    assert "carts" in data
    assert "total" in data
    assert "skip" in data
    assert "limit" in data

    assert isinstance(data["carts"], list)
    assert len(data["carts"]) > 0

    for cart in data["carts"]:
        assert cart["userId"] == user_id

        assert "products" in cart
        assert "total" in cart
        assert "discountedTotal" in cart
        assert "totalProducts" in cart
        assert "totalQuantity" in cart

        calculated_total_products = len(cart["products"])
        calculated_total_quantity = sum(
            product["quantity"] for product in cart["products"]
        )
        calculated_total = sum(
            product["total"] for product in cart["products"]
        )
        calculated_discounted_total = sum(
            product["discountedTotal"] for product in cart["products"]
        )

        assert cart["totalProducts"] == calculated_total_products
        assert cart["totalQuantity"] == calculated_total_quantity
        assert round(cart["total"], 2) == round(calculated_total, 2)
        assert round(cart["discountedTotal"], 2) == round(calculated_discounted_total, 2)
