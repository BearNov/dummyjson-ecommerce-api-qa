# API Exploration Notes

This document contains initial API exploration notes for the DummyJSON E-Commerce API QA Portfolio project.

The purpose of this step is to understand the available API responses before creating Postman requests and detailed test cases.

## Base URL

`https://dummyjson.com`

## Explored Endpoints

| Endpoint | Observation | QA Relevance |
|---|---|---|
| `GET /products` | Returns a list of products with pagination metadata such as `total`, `skip`, and `limit` | Useful for validating response structure, required fields, product list behavior, and pagination |
| `GET /products/1` | Returns a single product object | Useful for validating product details and required product fields |
| `GET /products/search?q=phone` | Returns products matching a search keyword | Useful for testing search behavior and result relevance |
| `GET /products/categories` | Returns available product categories | Useful for testing category availability and structure |
| `GET /carts` | Returns a list of carts with cart totals, products, quantities, and user IDs | Useful for cart validation and later SQL business-rule checks |
| `GET /carts/1` | Returns a single cart object | Useful for validating cart structure and product details inside a cart |
| `GET /carts/user/5` | Returns carts connected to a specific user ID | Useful for testing user/cart relationship logic |

## Important Product Fields Observed

Product responses may include fields such as:

- `id`
- `title`
- `description`
- `category`
- `price`
- `discountPercentage`
- `rating`
- `stock`
- `brand`
- `thumbnail`
- `images`

These fields are useful for API response validation and required-field checks.

## Important Cart Fields Observed

Cart responses may include fields such as:

- `id`
- `products`
- `total`
- `discountedTotal`
- `userId`
- `totalProducts`
- `totalQuantity`

Each product inside a cart may include fields such as:

- `id`
- `title`
- `price`
- `quantity`
- `total`
- `discountPercentage`
- `discountedTotal`

These fields are useful for business-rule validation, especially cart total checks, quantity checks, and discount calculations.

## Initial QA Notes

- Products and carts are the strongest areas for this project.
- Product endpoints support catalog, search, category, and pagination testing.
- Cart endpoints support deeper validation because they include quantities, prices, totals, discounts, and user IDs.
- User endpoints are useful mainly for validating relationships between users and carts.
- Authentication will be tested later at a basic level only.
- SQL validation will use local API-like data and will not claim access to DummyJSON internal databases.
