# Python Automation

In this folder, I document the Python API automation phase of the DummyJSON E-Commerce API QA project.

The goal of this section is to show how I took part of the API testing work from Postman and automated it with Python using `requests` and `pytest`.

## Files

| File | Purpose |
|---|---|
| [`requirements.txt`](./requirements.txt) | Lists the Python packages required to run the automation suite |
| [`tests/test_products_api.py`](./tests/test_products_api.py) | Contains Python tests for product endpoints |
| [`tests/test_carts_api.py`](./tests/test_carts_api.py) | Contains Python tests for cart endpoints and cart calculations |
| [`tests/test_users_api.py`](./tests/test_users_api.py) | Contains Python tests for user endpoints and user/cart relationships |
| [`tests/test_auth_api.py`](./tests/test_auth_api.py) | Contains Python tests for authentication and invalid login behavior |

## Tools Used

| Tool | Purpose |
|---|---|
| [Python](https://www.python.org/) | Main programming language for the automation scripts |
| [`requests`](https://requests.readthedocs.io/) | Sends HTTP API requests |
| [`pytest`](https://docs.pytest.org/) | Runs the automated test suite |

## Test Coverage

The Python automation suite currently includes 15 tests.

| Area | Test Count | Covered Behavior |
|---|---:|---|
| Products API | 6 | Product list, product by ID, search, pagination, categories, products by category |
| Carts API | 3 | Cart list, cart by ID, carts by user, cart totals, quantities, discounted totals |
| Users API | 3 | User list, user by ID, user carts, user/cart relationship |
| Authentication API | 3 | Valid login, current authenticated user, invalid login negative test |

## What I Validate

The Python tests validate:

- HTTP status codes
- Response structure
- Required fields
- Non-empty values
- Product search relevance
- Product pagination behavior
- Product category filtering
- Cart total product calculations
- Cart total quantity calculations
- Cart total calculations
- Cart discounted total calculations
- User identity fields
- User/cart relationships
- Authentication token generation
- Authenticated user retrieval
- Invalid login error handling

## How to Run the Tests Locally

From inside the Python automation folder, install the required packages:

`py -m pip install -r requirements.txt`

Then run the test suite:

`py -m pytest`

## Current Result

The first Python automation run completed successfully.

| Metric | Result |
|---|---:|
| Total tests | 15 |
| Passed tests | 15 |
| Failed tests | 0 |
| Errors | 0 |

The detailed Python test run summary is documented here:

[`06-test-summary/python-test-run-summary.md`](../06-test-summary/python-test-run-summary.md)

## Important Note

These tests run against the public [DummyJSON API](https://dummyjson.com).

Because this is a public API, response data may change over time. The tests focus on stable API structure, relationships, and business-rule checks rather than fragile assumptions about every returned value.
