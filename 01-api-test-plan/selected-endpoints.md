# Selected API Endpoints

This document lists the selected DummyJSON E-Commerce API endpoints included in the project scope.

The purpose of this file is to keep the API scope clear before creating Postman requests and detailed test cases.

## Base URL

`https://dummyjson.com`

## Products Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| GET | `/products` | Retrieve product list | Status code, response structure, required fields, pagination metadata |
| GET | `/products/{id}` | Retrieve a single product by ID | Valid ID, invalid ID, required product fields |
| GET | `/products/search?q=phone` | Search products by keyword | Search behavior, relevant results, empty/no-match scenarios |
| GET | `/products?limit=10&skip=10` | Retrieve paginated products | Limit, skip, result count, pagination metadata |
| GET | `/products/categories` | Retrieve product categories | Category list structure and availability |
| GET | `/products/category/smartphones` | Retrieve products by category | Category filtering and product consistency |

## Carts Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| GET | `/carts` | Retrieve cart list | Status code, response structure, cart fields |
| GET | `/carts/{id}` | Retrieve a single cart by ID | Valid ID, invalid ID, cart product structure |
| GET | `/carts/user/{userId}` | Retrieve carts by user ID | User/cart relationship and empty user cart scenarios |

## Users Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| GET | `/users` | Retrieve user list | Status code, response structure, required user fields |
| GET | `/users/{id}` | Retrieve a single user by ID | Valid ID, invalid ID, required user fields |
| GET | `/users/{id}/carts` | Retrieve carts connected to a user | User/cart relationship validation |

## Authentication Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| POST | `/auth/login` | Test user login | Valid login, invalid login, token response |
| GET | `/auth/me` | Retrieve authenticated user details | Authorization token behavior and authenticated user response |

## Notes

- The selected endpoints focus on one business domain: e-commerce.
- Products and carts will be the main API testing areas.
- Carts will also support the later SQL validation section because they contain product quantities, totals, discounted totals, and user IDs.
- Users are included mainly to support user/cart relationship testing.
- Authentication is included only at a basic level.
- Add, update, and delete flows are not included in the initial scope.
