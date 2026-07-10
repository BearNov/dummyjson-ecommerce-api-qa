# Python Test Run Summary

## Test Run Overview

I created this summary to document the first Python API automation test run for the DummyJSON E-Commerce API QA project.

This file shows that I did not only write Python test files, but also ran the test suite locally with `pytest` and verified the result.

## Related Files

| File | Purpose |
|---|---|
| [`05-python-automation/README.md`](../05-python-automation/README.md) | Explains the Python automation section |
| [`05-python-automation/requirements.txt`](../05-python-automation/requirements.txt) | Lists the Python packages required to run the tests |
| [`test_products_api.py`](../05-python-automation/tests/test_products_api.py) | Contains the Python product API tests |
| [`test_carts_api.py`](../05-python-automation/tests/test_carts_api.py) | Contains the Python cart API tests |
| [`test_users_api.py`](../05-python-automation/tests/test_users_api.py) | Contains the Python user API tests |
| [`test_auth_api.py`](../05-python-automation/tests/test_auth_api.py) | Contains the Python authentication API tests |

## Execution Tool

I ran the Python automation suite locally using `pytest`.

| Item | Value |
|---|---|
| Python version | Python 3.12.6 |
| Test runner | pytest 9.1.1 |
| HTTP library | requests 2.34.2 |
| Run type | Local command-line test run |

## Test Coverage Summary

| Area | Test Count | Status |
|---|---:|---|
| Products API | 6 | PASS |
| Carts API | 3 | PASS |
| Users API | 3 | PASS |
| Authentication API | 3 | PASS |
| Total | 15 | PASS |

## Execution Results

| Metric | Result |
|---|---:|
| Total tests | 15 |
| Passed tests | 15 |
| Failed tests | 0 |
| Errors | 0 |

## Tested Areas

The Python automation suite covers:

- Product list response
- Product by ID response
- Product search
- Product pagination
- Product categories
- Products by category
- Cart list response
- Cart by ID response
- Carts by user
- User list response
- User by ID response
- User carts
- Valid login
- Current authenticated user
- Invalid login negative test

## Validation Types

The Python tests validate:

- HTTP status codes
- Response body structure
- Required fields
- Non-empty values
- Product category filtering
- Product search relevance
- Pagination behavior
- Cart total product calculations
- Cart total quantity calculations
- Cart total calculations
- Cart discounted total calculations
- User identity fields
- User/cart relationships
- Authentication token generation
- Authenticated user retrieval
- Invalid login error handling

## Negative Testing

The Python suite includes an invalid login negative test.

The invalid login test verifies that:

- Invalid credentials return `400 Bad Request`
- The response contains the error message `Invalid credentials`
- The response does not return `accessToken`
- The response does not return `refreshToken`

This confirms that invalid login attempts are rejected correctly.

## Result

The first Python API automation run completed successfully.

All 15 Python tests passed.
