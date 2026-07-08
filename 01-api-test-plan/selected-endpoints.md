# Selected API Endpoints

I selected these DummyJSON E-Commerce API endpoints to keep the project focused on one clear business domain: e-commerce.

Before building the Postman collection, I used this file to define which endpoints are included in the first version of the project and what each endpoint is meant to validate.

## Base URL

`https://dummyjson.com`

## Products Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| GET | `/products` | Retrieve product list | Status code, response structure, required fields, pagination metadata |
| GET | `/products/{id}` | Retrieve a single product by ID | Valid ID, required product fields, product data structure |
| GET | `/products/search?q=phone` | Search products by keyword | Search behavior and result relevance |
| GET | `/products?limit=10&skip=10` | Retrieve paginated products | Limit, skip, result count, pagination metadata |
| GET | `/products/categories` | Retrieve product categories | Category list structure and category availability |
| GET | `/products/category/smartphones` | Retrieve products by category | Category filtering and product consistency |

## Carts Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| GET | `/carts` | Retrieve cart list | Status code, response structure, cart fields, cart totals |
| GET | `/carts/{id}` | Retrieve a single cart by ID | Valid ID, cart structure, product lines, totals, quantities |
| GET | `/carts/user/{userId}` | Retrieve carts by user ID | User/cart relationship and cart ownership validation |

## Users Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| GET | `/users` | Retrieve user list | Status code, response structure, required user identity fields |
| GET | `/users/{id}` | Retrieve a single user by ID | Valid ID, required user fields, address data, company data |
| GET | `/users/{id}/carts` | Retrieve carts connected to a user | User/cart relationship validation from the user side |

## Authentication Endpoints

| Method | Endpoint | Purpose | Testing Focus |
|---|---|---|---|
| POST | `/auth/login` | Test user login | Valid login, invalid login, token response |
| GET | `/auth/me` | Retrieve authenticated user details | Bearer token behavior and authenticated user response |

## Selection Notes

I focused the first version of the project on endpoints that support practical QA validation.

The strongest testing areas are:

- Product catalog validation
- Product search validation
- Product category filtering
- Cart calculation validation
- User/cart relationship validation
- Basic authentication flow
- Invalid login negative testing

I did not include add, update, and delete flows in the initial scope because I wanted the first version to stay focused, readable, and realistic for a beginner QA portfolio project.

Carts are especially important for the later SQL validation phase because they include:

- Product quantities
- Product totals
- Discounted totals
- Cart-level totals
- User IDs
- Product IDs

These fields make it possible to demonstrate business-rule validation and data consistency checks.
