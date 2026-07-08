# Postman Test Run Summary

## Test Run Overview

This file summarizes the first full Postman collection run for the DummyJSON E-Commerce API QA project.

## Collection

**Collection name:** DummyJSON E-Commerce API QA  
**Environment:** DummyJSON Environment  
**Run type:** Manual Postman collection run  
**Iterations:** 1  

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

The collection currently covers:

- Products
- Product search
- Product pagination
- Product categories
- Carts
- Cart calculations
- User data
- User-cart relationship
- Authentication
- Invalid login negative testing

## Important Notes

The request `Login with invalid credentials` is expected to return:

```text
400 Bad Request
