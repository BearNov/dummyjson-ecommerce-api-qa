# API Test Plan

## Project Name

DummyJSON E-Commerce API QA Portfolio

## Test Objective

The objective of this project is to test selected DummyJSON e-commerce API endpoints using a structured QA approach.

The project focuses on API testing, backend validation thinking, business-rule validation, SQL-based data checks using local API-like data, and later beginner-level Python automation.

The goal is to demonstrate practical QA skills in a realistic e-commerce API domain.

## API Under Test

Base URL: `https://dummyjson.com`

## Business Domain

E-Commerce

The selected API areas are related to common e-commerce behavior:

- Product catalog
- Product search
- Product categories
- Shopping carts
- User/cart relationships
- Basic authentication

## In Scope

The following API areas are included in this project:

### Products

| Endpoint | Purpose |
|---|---|
| `GET /products` | Retrieve product list |
| `GET /products/{id}` | Retrieve a single product by ID |
| `GET /products/search?q=phone` | Search products by keyword |
| `GET /products?limit=10&skip=10` | Test pagination behavior |
| `GET /products/categories` | Retrieve product categories |
| `GET /products/category/smartphones` | Retrieve products by category |

### Carts

| Endpoint | Purpose |
|---|---|
| `GET /carts` | Retrieve cart list |
| `GET /carts/{id}` | Retrieve a single cart by ID |
| `GET /carts/user/{userId}` | Retrieve carts for a specific user |

### Users

| Endpoint | Purpose |
|---|---|
| `GET /users` | Retrieve user list |
| `GET /users/{id}` | Retrieve a single user by ID |
| `GET /users/{id}/carts` | Retrieve carts connected to a user |

### Authentication

| Endpoint | Purpose |
|---|---|
| `POST /auth/login` | Test login behavior |
| `GET /auth/me` | Retrieve authenticated user details |

## Out of Scope

The following areas are not included in the initial project scope:

- Real database validation against DummyJSON internal data
- Full UI testing
- Performance or load testing
- Advanced security testing
- Production-level automation framework design
- Full CRUD coverage for all resources
- Payment, checkout, shipping, or order processing flows

## Test Approach

The project will use a phased testing approach:

1. Explore the API and define endpoint scope
2. Create a structured API test plan
3. Build a Postman collection with selected requests
4. Add Postman assertions for response validation
5. Document positive, negative, and edge-case API test cases
6. Create local SQL validation data based on API-like e-commerce structures
7. Write SQL checks for business-rule and data-quality validation
8. Add beginner-level Python automation after the Postman and SQL sections are complete
9. Summarize test execution results and project limitations

## Test Types

The project will include:

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
- Basic authentication testing

## Test Data Approach

The API testing phase will use data returned by DummyJSON endpoints.

The SQL validation phase will use a small local dataset based on realistic DummyJSON-style API response structures.

This project will not claim direct access to DummyJSON internal databases.

## Risks and Assumptions

| Item | Description |
|---|---|
| Public API dependency | DummyJSON is a public API, so behavior or data may change over time |
| No real database access | SQL checks must be performed on local API-like data, not DummyJSON internal data |
| Limited business flow | DummyJSON does not represent a full real e-commerce checkout system |
| Authentication limitations | Auth testing will stay basic and focused on login/token behavior |
| Beginner automation scope | Python automation will be added later and kept beginner-friendly |

## Entry Criteria

Testing can begin when:

- The project repository structure is created
- The API scope is approved
- The selected endpoints are accessible in the browser
- The API test plan is documented

## Exit Criteria

This phase is complete when:

- The selected API areas are clearly documented
- In-scope and out-of-scope items are defined
- Risks and assumptions are listed
- The project is ready for Postman collection setup
