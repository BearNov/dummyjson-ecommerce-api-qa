# Postman Collection

This folder contains the exported Postman assets for the DummyJSON E-Commerce API QA project.

## Files

| File | Purpose |
|---|---|
| `DummyJSON-E-Commerce-API-QA.postman_collection.json` | Exported Postman collection containing API requests and test scripts |
| `DummyJSON-Environment.postman_environment.json` | Sanitized Postman environment file with required variables |

## Collection Coverage

The Postman collection currently includes 15 API requests across four areas:

| Area | Covered Requests |
|---|---|
| Products | Product list, product by ID, search, pagination, categories, products by category |
| Carts | Cart list, cart by ID, carts by user |
| Users | User list, user by ID, user carts |
| Authentication | Login, current authenticated user, invalid login |

## Test Coverage

The collection includes 114 automated Postman assertions.

The assertions validate:

- HTTP status codes
- Response structure
- Required fields
- Product data fields
- Pagination fields
- Category filtering
- Cart totals
- Cart discounted totals
- Cart product quantities
- User identity fields
- User-cart relationship
- Authentication token response
- Invalid login error handling

## How to Import and Run

1. Open Postman.
2. Import `DummyJSON-E-Commerce-API-QA.postman_collection.json`.
3. Import `DummyJSON-Environment.postman_environment.json`.
4. Select the `DummyJSON Environment` environment.
5. Run the full collection from the Collection Runner.

## Environment Variables

| Variable | Purpose |
|---|---|
| `base_url` | Base API URL: `https://dummyjson.com` |
| `access_token` | Filled automatically after successful login |
| `auth_user_id` | Filled automatically from the login response |
| `auth_username` | Filled automatically from the login response |
| `auth_email` | Filled automatically from the login response |

## Security Note

The environment file is sanitized.

Actual authentication token values are not committed to this repository.

The `access_token` value is generated during the collection run by the `Login user` request and reused by the `Get current auth user` request.

## Latest Test Run

The first full Postman collection run completed successfully:

| Metric | Result |
|---|---:|
| Total requests | 15 |
| Total tests | 114 |
| Passed tests | 114 |
| Failed tests | 0 |
| Errors | 0 |

The detailed run summary is documented in:

`06-test-summary/postman-test-run-summary.md`
