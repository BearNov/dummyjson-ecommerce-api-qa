# API Test Cases

In this folder, I document the API test cases covered by the Postman collection.

The goal of this section is to make the testing work readable outside of Postman.  
Instead of only showing the exported collection file, I use this documentation to explain what I tested, which endpoints were covered, and what results were expected.

## Files

| File | Purpose |
|---|---|
| [`api-test-cases.md`](./api-test-cases.md) | Documents the API test cases, expected results, validation types, authentication flow, negative testing, and current execution result |

## Test Case Coverage

The documented test cases cover:

- Products
- Product search
- Product pagination
- Product categories
- Carts
- Cart calculations
- Users
- User/cart relationships
- Authentication
- Invalid login negative testing

## What I Validate

The test cases are written to cover more than basic status-code checks.

I validate:

- HTTP status codes
- Response structure
- Required fields
- Data types
- Non-empty values
- Pagination behavior
- Product search behavior
- Product category filtering
- Cart totals
- Cart discounted totals
- Cart quantity calculations
- User identity fields
- User/cart relationships
- Authentication token behavior
- Invalid login error handling

## Related Files

| File | Purpose |
|---|---|
| [`02-postman-collection/README.md`](../02-postman-collection/README.md) | Explains how to import and run the Postman collection |
| [`02-postman-collection/DummyJSON-E-Commerce-API-QA.postman_collection.json`](../02-postman-collection/DummyJSON-E-Commerce-API-QA.postman_collection.json) | Exported Postman collection |
| [`06-test-summary/postman-test-run-summary.md`](../06-test-summary/postman-test-run-summary.md) | Documents the first full Postman test run result |

## Current Status

The first version of the API test case documentation is complete.

Current documented coverage:

| Metric | Result |
|---|---:|
| Total requests | 15 |
| Total Postman assertions | 114 |
| Passed tests | 114 |
| Failed tests | 0 |
| Errors | 0 |
