# SQL Validation Plan

## Purpose

This phase demonstrates SQL-based validation logic using local API-like datasets based on the DummyJSON e-commerce domain.

DummyJSON does not provide access to its real internal database.  
Therefore, this project does not claim to validate DummyJSON's real backend database.

Instead, this phase uses a small local dataset that represents API-like data for:

- Users
- Products
- Carts
- Cart items

The goal is to demonstrate how a QA tester can use SQL to validate backend-style data rules, relationships, calculations, and data quality.

## Why Local SQL Validation Is Used

The DummyJSON API returns JSON responses, but it does not provide direct database access.

Because of that, SQL validation in this project is performed on a local dataset created from sample API response structures.

This is useful for showing:

- Data validation thinking
- Relationship checks
- Cart calculation checks
- Duplicate detection
- Missing data checks
- Invalid value detection
- SQL query writing ability

## Planned Tables

| Table | Purpose |
|---|---|
| `users` | Stores user identity data |
| `products` | Stores product data |
| `carts` | Stores cart-level data |
| `cart_items` | Stores product lines inside carts |

## Planned Validation Areas

| Validation Area | Example Checks |
|---|---|
| User data | Missing names, duplicate user IDs, invalid emails |
| Product data | Duplicate product IDs, negative prices, missing product names |
| Cart data | Missing user IDs, invalid cart totals, invalid quantities |
| Cart items | Product quantity checks, product total checks, discounted total checks |
| Relationships | Cart user ID exists in users table, cart item product ID exists in products table |
| Calculations | Cart total equals sum of item totals, total quantity equals sum of item quantities |

## Example SQL Validation Questions

The SQL queries will answer questions such as:

- Are there duplicate user IDs?
- Are there products with missing titles?
- Are there products with negative prices?
- Are there carts connected to missing users?
- Are there cart items connected to missing products?
- Does each cart total match the sum of its product line totals?
- Does each cart total quantity match the sum of item quantities?
- Are there invalid product quantities?
- Are there invalid discounted totals?

## Data Analyst Connection

This phase also demonstrates data analyst skills because it uses SQL to inspect, validate, and summarize structured data.

The focus is not only on whether the API responds successfully, but also whether the returned business data is internally consistent.

This connects QA testing with data validation and analytical thinking.

## Tools Planned

The SQL validation phase may use:

- SQLite
- DB Browser for SQLite
- SQL scripts
- Local CSV or insert-based sample data
- Markdown documentation

## Important Limitation

This phase is a local validation simulation based on API-like data.

It does not validate DummyJSON's production database and does not claim direct database access.
