# API Test Plan

## Project Name

DummyJSON E-Commerce API QA Portfolio

## Test Objective

I created this test plan to define the API testing scope for the DummyJSON e-commerce domain before building the Postman collection, SQL validation files, and Python automation tests.

The goal of this phase was to show a structured QA approach: selecting relevant endpoints, defining what should be tested, separating in-scope and out-of-scope areas, and documenting risks before execution.

This project covers:

- API testing
- Backend validation thinking
- Business-rule validation
- SQL-based data checks using local API-like data
- Python API automation using `requests` and `pytest`

## API Under Test

Base URL:

[https://dummyjson.com](https://dummyjson.com)

## Business Domain

The project focuses on an e-commerce API domain.

I selected API areas that represent common e-commerce behavior:

- Product catalog
- Product search
- Product categories
- Shopping carts
- User/cart relationships
- Basic authentication

## In Scope

The following API areas are included in this project.

### Products

| Endpoint | Purpose |
|---|---|
| [`GET /products`](https://dummyjson.com/products) | Retrieve product list |
| [`GET /products/1`](https://dummyjson.com/products/1) | Retrieve a single product by ID |
| [`GET /products/search?q=phone`](https://dummyjson.com/products/search?q=phone) | Search products by keyword |
| [`GET /products?limit=10&skip=10`](https://dummyjson.com/products?limit=10&skip=10) | Test pagination behavior |
| [`GET /products/categories`](https://dummyjson.com/products/categories) | Retrieve product categories |
| [`GET /products/category/smartphones`](https://dummyjson.com/products/category/smartphones) | Retrieve products by category |

### Carts

| Endpoint | Purpose |
|---|---|
| [`GET /carts`](https://dummyjson.com/carts) | Retrieve cart list |
| [`GET /carts/1`](https://dummyjson.com/carts/1) | Retrieve a single cart by ID |
| [`GET /carts/user/5`](https://dummyjson.com/carts/user/5) | Retrieve carts for a specific user |

### Users

| Endpoint | Purpose |
|---|---|
| [`GET /users`](https://dummyjson.com/users) | Retrieve user list |
| [`GET /users/1`](https://dummyjson.com/users/1) | Retrieve a single user by ID |
| [`GET /users/5/carts`](https://dummyjson.com/users/5/carts) | Retrieve carts connected to a user |

### Authentication

| Endpoint | Purpose |
|---|---|
| [`POST /auth/login`](https://dummyjson.com/auth/login) | Test valid and invalid login behavior |
| [`GET /auth/me`](https://dummyjson.com/auth/me) | Retrieve authenticated user details |

## Out of Scope

I did not include the following areas in the first project version:

- Real database validation against DummyJSON internal data
- Full UI testing
- Performance or load testing
- Advanced security testing
- Production-level automation framework design
- Full CRUD coverage for all resources
- Payment, checkout, shipping, or order processing flows

## Test Approach

I used a phased testing approach:

1. Explore the API and define endpoint scope
2. Create a structured API test plan
3. Build a Postman collection with selected requests
4. Add Postman assertions for response validation
5. Document positive, negative, and edge-case API test cases
6. Create local SQL validation data based on API-like e-commerce structures
7. Write SQL checks for business-rule and data-quality validation
8. Add Python API automation with `requests` and `pytest`
9. Summarize test execution results and project limitations

## Test Types

The project includes:

- Positive API testing
- Negative API testing
- Response status validation
- Response body validation
- Required field validation
- Search behavior validation
- Pagination validation
- Cart total and quantity validation
- User/cart relationship validation
- SQL-based data validation using local datasets
- Python API automation testing
- Basic authentication testing

## Test Data Approach

The API testing and Python automation phases use data returned by DummyJSON endpoints.

The SQL validation phase uses a small local dataset based on realistic DummyJSON-style API response structures.

I do not claim direct access to DummyJSON internal databases.

## Risks and Assumptions

| Item | Description |
|---|---|
| Public API dependency | DummyJSON is a public API, so behavior or data may change over time |
| No real database access | SQL checks are performed on local API-like data, not DummyJSON internal data |
| Limited business flow | DummyJSON does not represent a full real e-commerce checkout system |
| Authentication limitations | Auth testing stays basic and focuses on login/token behavior |
| Beginner automation scope | Python automation is intentionally kept beginner-friendly and readable |

## Entry Criteria

Testing could begin when:

- The project repository structure was created
- The API scope was defined
- The selected endpoints were accessible
- The API test plan was documented

## Exit Criteria

This phase was complete when:

- The selected API areas were clearly documented
- In-scope and out-of-scope items were defined
- Risks and assumptions were listed
- The project was ready for Postman collection setup, SQL validation, and Python automation
