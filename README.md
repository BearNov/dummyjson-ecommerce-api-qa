# DummyJSON E-Commerce API QA Portfolio

I built this project to demonstrate API testing, backend validation thinking, SQL-based data validation, and beginner-level Python automation around one realistic e-commerce API domain.

The project uses the [DummyJSON E-Commerce API](https://dummyjson.com) and focuses on practical QA areas such as products, product search, categories, carts, users, and authentication.

Because DummyJSON does not provide direct database access, I will use a local API-like dataset in the SQL section. This keeps the project honest while still showing how SQL can support backend-style validation and data consistency checks.

## Project Goals

In this project, I aim to show that I can:

- Test REST API endpoints using Postman
- Write clear API test cases and expected results
- Validate e-commerce business rules such as cart totals, quantities, prices, and product references
- Use SQL to check local API-like data for consistency and data quality
- Connect QA testing with data validation and analytical thinking
- Later add beginner Python automation using `requests` and `pytest`
- Build a clean QA portfolio project that can be reviewed through GitHub

## Scope

This project currently covers:

- Product listing API testing
- Product details API testing
- Product search testing
- Product category testing
- Cart validation scenarios
- User and cart relationship checks
- Basic authentication testing
- Positive and negative API test cases
- Postman assertions
- SQL validation using local API-like datasets
- Python automation in a later phase

## Out of Scope

This project does not include:

- Real database validation against DummyJSON internal data
- Performance or load testing
- Advanced security testing
- Full UI testing
- Production-level automation framework design

## Tools Planned / Used

- [GitHub](https://github.com/)
- [Postman](https://www.postman.com/)
- SQL
- [SQLite](https://www.sqlite.org/)
- [Python](https://www.python.org/)
- [`pytest`](https://docs.pytest.org/)
- [`requests`](https://requests.readthedocs.io/)

## Project Structure

```text
dummyjson-ecommerce-api-qa
├── 01-api-test-plan
│   ├── README.md
│   ├── selected-endpoints.md
│   └── api-exploration-notes.md
├── 02-postman-collection
│   ├── README.md
│   ├── DummyJSON-E-Commerce-API-QA.postman_collection.json
│   └── DummyJSON-Environment.postman_environment.json
├── 03-api-test-cases
│   ├── README.md
│   └── api-test-cases.md
├── 04-sql-validation
│   ├── README.md
│   ├── sql-validation-plan.md
│   ├── schema.sql
│   ├── sample-data.sql
│   ├── validation-queries.sql
│   └── sql-validation-results.md
├── 05-python-automation
│   └── README.md
├── 06-test-summary
│   ├── README.md
│   └── postman-test-run-summary.md
└── README.md
```

## Folder Purpose

| Folder | Purpose |
|---|---|
| [`01-api-test-plan`](./01-api-test-plan) | Documents the API testing scope, selected endpoints, risks, and test approach |
| [`02-postman-collection`](./02-postman-collection) | Stores the exported Postman collection and sanitized environment file |
| [`03-api-test-cases`](./03-api-test-cases) | Contains documented API test cases and expected results |
| [`04-sql-validation`](./04-sql-validation) | Contains the local SQL validation plan, schema, sample data, validation queries, and results || [`05-python-automation`](./05-python-automation) | Will contain Python API automation in a later phase |
| [`06-test-summary`](./06-test-summary) | Summarizes test execution results, findings, and project limitations |

## Current Status

The first version of the Postman API testing phase is complete.

Current Postman coverage:

- 15 API requests
- 114 automated assertions
- 114 passed tests
- 0 failed tests
- Positive and negative API testing
- Authentication token flow
- Cart business-rule validation
- User/cart relationship checks

The SQL validation phase is also complete.

Current SQL validation coverage:

- Local SQLite database schema
- Local API-like sample data
- Record count validation
- Duplicate ID checks
- Required-field checks
- Email format check
- Numeric value checks
- Relationship checks between users, carts, cart items, and products
- Cart item total validation
- Cart total validation
- Cart discounted total validation
- Cart product count validation
- Cart quantity validation
- Joined cart detail view

The SQL validation results are documented in:

[`04-sql-validation/sql-validation-results.md`](./04-sql-validation/sql-validation-results.md)

The next planned phase is beginner-level Python API automation.
