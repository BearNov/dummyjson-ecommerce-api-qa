# API Test Cases

This document summarizes the API test cases covered in the Postman collection for the DummyJSON E-Commerce API QA project.

The test cases focus on functional API behavior, response structure, data validation, relationship validation, authentication, and negative testing.

## Test Case Summary

| TC ID | Area | Test Case | Method | Endpoint | Expected Result |
|---|---|---|---|---|---|
| API-TC-001 | Products | Get all products | GET | `/products` | Product list is returned with pagination fields |
| API-TC-002 | Products | Get product by ID | GET | `/products/1` | Product ID 1 is returned with required product fields |
| API-TC-003 | Products | Search products by keyword | GET | `/products/search?q=phone` | Products related to the search keyword are returned |
| API-TC-004 | Products | Get products with pagination | GET | `/products?limit=10&skip=10` | API returns 10 products and correct pagination values |
| API-TC-005 | Products | Get product categories | GET | `/products/categories` | Category list is returned with slug, name, and URL |
| API-TC-006 | Products | Get products by category | GET | `/products/category/smartphones` | Returned products belong to the smartphones category |
| API-TC-007 | Carts | Get all carts | GET | `/carts` | Cart list is returned with cart totals and product lines |
| API-TC-008 | Carts | Get cart by ID | GET | `/carts/1` | Cart ID 1 is returned with valid totals and quantities |
| API-TC-009 | Carts | Get carts by user | GET | `/carts/user/5` | Returned carts belong to user ID 5 |
| API-TC-010 | Users | Get all users | GET | `/users` | User list is returned with identity fields and unique user IDs |
| API-TC-011 | Users | Get user by ID | GET | `/users/1` | User ID 1 is returned with identity, address, and company data |
| API-TC-012 | Users | Get user carts | GET | `/users/5/carts` | User ID 5 carts are returned and cart totals are valid |
| API-TC-013 | Authentication | Login user | POST | `/auth/login` | Valid login returns user data, access token, and refresh token |
| API-TC-014 | Authentication | Get current authenticated user | GET | `/auth/me` | Bearer token returns the authenticated user profile |
| API-TC-015 | Authentication | Login with invalid credentials | POST | `/auth/login` | Invalid credentials return 400 and no tokens |

## Validation Types Covered

The Postman tests validate:

- HTTP status codes
- Response body structure
- Required fields
- Data types
- Non-empty values
- Pagination fields
- Product search relevance
- Category filtering
- Cart totals
- Cart discounted totals
- Cart quantity calculations
- User identity fields
- Unique user IDs
- User-cart relationships
- Authentication token generation
- Authenticated user retrieval
- Invalid login negative behavior

## Cart Calculation Checks

Several cart-related tests validate business logic, not only response structure.

The tests check that:

| Validation | Description |
|---|---|
| `totalProducts` | Matches the number of product lines in the cart |
| `totalQuantity` | Matches the sum of all product quantities |
| `total` | Matches the sum of product totals |
| `discountedTotal` | Matches the sum of product discounted totals |
| Numeric values | Prices, quantities, totals, discounts, and IDs are valid numbers |

A small calculation tolerance is used for total comparisons because API responses may include decimal rounding differences.

## Authentication Flow

The authentication tests cover a basic token-based flow:

1. `Login user` sends valid credentials.
2. The response returns an `accessToken`.
3. The token is saved into the Postman environment as `access_token`.
4. `Get current auth user` uses `{{access_token}}` as a Bearer token.
5. The authenticated user response is compared against values saved from the login response.

## Negative Testing

The collection includes a negative authentication test:

| Test | Expected Result |
|---|---|
| Login with invalid credentials | `400 Bad Request` with error message `Invalid credentials` |

This test also verifies that invalid login does not return:

- `accessToken`
- `refreshToken`

## Current Execution Result

The first full Postman collection run completed successfully:

| Metric | Result |
|---|---:|
| Total requests | 15 |
| Total tests | 114 |
| Passed tests | 114 |
| Failed tests | 0 |
| Errors | 0 |
