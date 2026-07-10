# DummyJSON E-Commerce API QA Portfolio

## Project Highlights

| Area | Result |
|---|---:|
| Postman API requests | 15 |
| Postman assertions passed | 114 |
| Python automation tests passed | 15 |
| SQL validation checks | 15 checks + joined view |
| Main testing layers | Postman, SQL, Python |

I built this project to demonstrate API testing, backend validation thinking, SQL-based data validation, and beginner-level Python automation around one realistic e-commerce API domain.

The project uses the [DummyJSON E-Commerce API](https://dummyjson.com) and focuses on practical QA areas such as products, product search, categories, carts, users, and authentication.

Because DummyJSON does not provide direct database access, I use a local API-like dataset in the SQL section. This keeps the project honest while still showing how SQL can support backend-style validation and data consistency checks.

## Project Goals

In this project, I aim to show that I can:

- Test REST API endpoints using Postman
- Write clear API test cases and expected results
- Validate e-commerce business rules such as cart totals, quantities, prices, and product references
- Use SQL to check local API-like data for consistency and data quality
- Connect QA testing with data validation and analytical thinking
- Automate API tests with Python using `requests` and `pytest`
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
- Python API automation with `requests` and `pytest`

## Out of Scope

This project does not include:

- Real database validation against DummyJSON internal data
- Performance or load testing
- Advanced security testing
- Full UI testing
- Production-level automation framework design

## Tools Used

- [GitHub](https://github.com/)
- [Postman](https://www.postman.com/)
- SQL
- [SQLite](https://www.sqlite.org/)
- [DB Browser for SQLite](https://sqlitebrowser.org/)
- [Python](https://www.python.org/)
- [`pytest`](https://docs.pytest.org/)
- [`requests`](https://requests.readthedocs.io/)

## How to Run

### Postman Collection

1. Open [Postman](https://www.postman.com/).
2. Import the collection file:

   [`02-postman-collection/DummyJSON-E-Commerce-API-QA.postman_collection.json`](./02-postman-collection/DummyJSON-E-Commerce-API-QA.postman_collection.json)

3. Import the environment file:

   [`02-postman-collection/DummyJSON-Environment.postman_environment.json`](./02-postman-collection/DummyJSON-Environment.postman_environment.json)

4. Select `DummyJSON Environment`.
5. Run the full collection from the Postman Collection Runner.

### SQL Validation

1. Open [DB Browser for SQLite](https://sqlitebrowser.org/).
2. Create a local SQLite database file.
3. Run the SQL files in this order:

   - [`04-sql-validation/schema.sql`](./04-sql-validation/schema.sql)
   - [`04-sql-validation/sample-data.sql`](./04-sql-validation/sample-data.sql)
   - [`04-sql-validation/validation-queries.sql`](./04-sql-validation/validation-queries.sql)

4. Review the documented results here:

   [`04-sql-validation/sql-validation-results.md`](./04-sql-validation/sql-validation-results.md)

### Python Automation

1. Open a terminal inside the `05-python-automation` folder.
2. Create and activate a virtual environment.
3. Install the required packages:

   ```bash
   py -m pip install -r requirements.txt
   ```

4. Run the Python test suite:

   ```bash
   py -m pytest
   ```

5. Review the documented results here:

   [`06-test-summary/python-test-run-summary.md`](./06-test-summary/python-test-run-summary.md)

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
│   ├── README.md
│   ├── requirements.txt
│   └── tests
│       ├── test_products_api.py
│       ├── test_carts_api.py
│       ├── test_users_api.py
│       └── test_auth_api.py
├── 06-test-summary
│   ├── README.md
│   ├── postman-test-run-summary.md
│   ├── python-test-run-summary.md
│   └── final-project-summary.md
├── .gitignore
└── README.md
```

## Folder Purpose

| Folder | Purpose |
|---|---|
| [`01-api-test-plan`](./01-api-test-plan) | Documents the API testing scope, selected endpoints, risks, and test approach |
| [`02-postman-collection`](./02-postman-collection) | Stores the exported Postman collection and sanitized environment file |
| [`03-api-test-cases`](./03-api-test-cases) | Contains documented API test cases and expected results |
| [`04-sql-validation`](./04-sql-validation) | Contains the local SQL validation plan, schema, sample data, validation queries, and results |
| [`05-python-automation`](./05-python-automation) | Contains Python API automation tests using `requests` and `pytest` |
| [`06-test-summary`](./06-test-summary) | Summarizes test execution results, findings, project limitations, and final project summary |

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

The Python automation phase is complete for the first project version.

Current Python automation coverage:

- 15 Python API tests
- 15 passed tests
- 0 failed tests
- Product API tests
- Cart API tests
- User API tests
- Authentication tests
- Invalid login negative test
- Cart calculation validation
- User/cart relationship validation

Detailed results are documented in:

- [`04-sql-validation/sql-validation-results.md`](./04-sql-validation/sql-validation-results.md)
- [`06-test-summary/postman-test-run-summary.md`](./06-test-summary/postman-test-run-summary.md)
- [`06-test-summary/python-test-run-summary.md`](./06-test-summary/python-test-run-summary.md)
- [`06-test-summary/final-project-summary.md`](./06-test-summary/final-project-summary.md)
