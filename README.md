# DummyJSON E-Commerce API QA Portfolio

This project demonstrates API testing, backend validation thinking, SQL-based data validation, and beginner-level Python automation using the DummyJSON E-Commerce API.

The project focuses on realistic e-commerce API areas such as products, product search, categories, carts, users, and authentication.

Since DummyJSON does not provide direct database access, the SQL section will use a local API-like dataset to demonstrate data validation logic honestly and transparently.

## Project Goals

- Practice API testing using Postman
- Write clear API test cases and expected results
- Validate e-commerce business rules such as cart totals, quantities, prices, and product references
- Demonstrate SQL-based data validation logic
- Later add beginner Python automation using requests and pytest
- Build a clean QA portfolio project suitable for GitHub and CV usage

## Scope

This project will cover:

- Product listing API testing
- Product details API testing
- Product search testing
- Product category testing
- Cart validation scenarios
- User and cart relationship checks
- Basic authentication testing if suitable
- Positive and negative API test cases
- Postman assertions
- SQL validation using local API-like datasets
- Python automation in a later phase

## Out of Scope

This project will not include:

- Real database validation against DummyJSON internal data
- Performance or load testing
- Advanced security testing
- Full UI testing
- Production-level automation framework design

## Tools Planned

- GitHub
- Postman
- SQL
- Python
- pytest
- requests

## Project Structure

```text
dummyjson-ecommerce-api-qa
├── 01-api-test-plan
│   └── README.md
├── 02-postman-collection
│   └── README.md
├── 03-api-test-cases
│   └── README.md
├── 04-sql-validation
│   └── README.md
├── 05-python-automation
│   └── README.md
├── 06-test-summary
│   └── README.md
└── README.md
```

### Folder Purpose

| Folder | Purpose |
|---|---|
| `01-api-test-plan` | Defines the API testing scope, selected endpoints, risks, and test approach |
| `02-postman-collection` | Stores the Postman collection and environment files |
| `03-api-test-cases` | Contains documented API test cases and expected results |
| `04-sql-validation` | Demonstrates local SQL validation using API-like e-commerce data |
| `05-python-automation` | Contains Python API automation added later in the project |
| `06-test-summary` | Summarizes test execution results, findings, and limitations |
