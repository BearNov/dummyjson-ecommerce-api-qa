# Final Project Summary

## Overview

I built this project to demonstrate a complete beginner-friendly QA workflow around one realistic e-commerce API domain.

The project uses the public [DummyJSON API](https://dummyjson.com) and focuses on products, carts, users, authentication, API validation, SQL-based data validation, and Python API automation.

## What I Built

In this project, I created:

- API test planning documentation
- API exploration notes
- Selected endpoint documentation
- Postman collection with automated assertions
- API test case documentation
- Local SQL validation schema
- Local API-like sample data
- SQL validation queries
- SQL validation results documentation
- Python API automation tests
- Postman and Python test run summaries

## Main Testing Layers

| Layer | What I Used | Result |
|---|---|---|
| API testing | Postman | 114 assertions passed |
| SQL validation | SQLite and DB Browser for SQLite | All local validation checks passed |
| Python automation | Python, `requests`, and `pytest` | 15 tests passed |

## Postman Testing Summary

The Postman collection covers:

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

The first full Postman collection run completed successfully with:

- 15 API requests
- 114 automated assertions
- 114 passed assertions
- 0 failed assertions

## SQL Validation Summary

Because DummyJSON does not provide direct access to its internal database, I created a local API-like SQLite dataset.

The SQL validation phase checks:

- Record counts
- Duplicate IDs
- Missing required fields
- Invalid email format
- Invalid numeric values
- User/cart relationships
- Cart item/product relationships
- Cart total calculations
- Cart discounted total calculations
- Cart quantity calculations
- Joined cart detail view

This phase shows how I used SQL to validate data quality, relationships, and business-rule calculations.

## Python Automation Summary

The Python automation suite covers:

- Product list
- Product by ID
- Product search
- Product pagination
- Product categories
- Products by category
- Cart list
- Cart by ID
- Carts by user
- User list
- User by ID
- User carts
- Valid login
- Current authenticated user
- Invalid login negative test

The first Python automation run completed successfully with:

- 15 tests
- 15 passed
- 0 failed
- 0 errors

## What This Project Demonstrates

This project shows that I can:

- Plan API testing scope
- Explore API responses before writing tests
- Write clear API test cases
- Build Postman requests and assertions
- Validate response structure and required fields
- Test positive and negative API behavior
- Validate cart business rules
- Use SQL for local backend-style data validation
- Join tables and validate relationships
- Write beginner-level Python API automation tests
- Run and document test results
- Keep project documentation clear and portfolio-ready

## Important Limitations

This project uses the public DummyJSON API.

Because of that:

- I do not have access to DummyJSON's real production database
- SQL validation is performed on a local API-like dataset
- API response data may change over time
- The project does not include performance testing
- The project does not include UI testing
- The project does not include advanced security testing

## Final Result

The first version of the DummyJSON E-Commerce API QA Portfolio project is complete.

The project includes manual API testing with Postman, local SQL validation, and Python API automation around one consistent e-commerce domain.
