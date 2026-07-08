# Postman Test Run Summary

## Test Run Overview

I created this summary to document the first full Postman collection run for the DummyJSON E-Commerce API QA project.

This file shows that I did not only create API requests and test scripts, but also ran the full collection and recorded the execution result.

## Related Files

| File | Purpose |
|---|---|
| [`02-postman-collection/README.md`](../02-postman-collection/README.md) | Explains how to import and run the Postman collection |
| [`DummyJSON-E-Commerce-API-QA.postman_collection.json`](../02-postman-collection/DummyJSON-E-Commerce-API-QA.postman_collection.json) | Exported Postman collection |
| [`DummyJSON-Environment.postman_environment.json`](../02-postman-collection/DummyJSON-Environment.postman_environment.json) | Sanitized Postman environment file |
| [`03-api-test-cases/api-test-cases.md`](../03-api-test-cases/api-test-cases.md) | Documents the API test cases and expected results |

## Collection

| Item | Value |
|---|---|
| Collection name | DummyJSON E-Commerce API QA |
| Environment | DummyJSON Environment |
| Run type | Manual Postman collection run |
| Iterations | 1 |

## Execution Results

| Metric | Result |
|---|---:|
| Total requests | 15 |
| Total tests | 114 |
| Passed tests | 114 |
| Failed tests | 0 |
| Errors | 0 |
| Duration | 3s 57ms |
| Average response time | 110 ms |

## Tested Areas

The collection run covered:

- Products
- Product search
- Product pagination
- Product categories
- Carts
- Cart calculations
- User data
- User/cart relationship
- Authentication
- Invalid login negative testing

## Important Note About Negative Testing

The request `Login with invalid credentials` is expected to return `400 Bad Request`.

This is not a failed test case.

I included this request to verify that the API rejects invalid credentials correctly and does not return authentication tokens for an invalid login attempt.

## Result

The first full Postman collection run completed successfully.

All 114 automated Postman assertions passed.
