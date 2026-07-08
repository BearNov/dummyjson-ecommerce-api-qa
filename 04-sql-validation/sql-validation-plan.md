# SQL Validation Plan

## Purpose

In this phase, I use SQL to demonstrate backend-style data validation around the DummyJSON e-commerce domain.

DummyJSON provides API responses, but it does not provide direct access to its real internal database. Because of that, I am not claiming to validate DummyJSON's production database.

Instead, I will create a small local API-like dataset that reflects the same business areas tested in Postman:

- Users
- Products
- Carts
- Cart items

I use this local dataset to show how SQL can support QA work by checking relationships, calculations, missing values, duplicates, and data consistency.

## Why I Use Local SQL Validation

The API returns JSON data, but I cannot query the real backend database behind DummyJSON.

To keep the project realistic and honest, I use local SQL validation as a simulation of backend data checks.

This allows me to demonstrate how I would validate e-commerce data if I had access to structured database tables.

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
| User data | Missing names, duplicate user IDs, invalid email format |
| Product data | Duplicate product IDs, missing titles, negative prices |
| Cart data | Missing users, invalid totals, invalid quantities |
| Cart items | Invalid product references, incorrect line totals, invalid discounted totals |
| Relationships | Cart user ID exists in users table, cart item product ID exists in products table |
| Calculations | Cart total equals sum of item totals, total quantity equals sum of item quantities |

## SQL Validation Questions

The SQL queries will help me answer questions such as:

- Are there duplicate user IDs?
- Are there users with missing names or invalid emails?
- Are there duplicate product IDs?
- Are there products with missing titles?
- Are there products with negative prices?
- Are there carts connected to users that do not exist?
- Are there cart items connected to products that do not exist?
- Does each cart total match the sum of its product line totals?
- Does each cart discounted total match the sum of discounted item totals?
- Does each cart total quantity match the sum of item quantities?
- Are there invalid product quantities?

## Data Analyst Connection

I use this SQL phase to connect QA testing with data validation and analytical thinking.

The Postman collection checks whether the API responds correctly.

The SQL validation phase goes one step deeper by checking whether the business data is internally consistent.

This is useful because many QA issues are not only technical API failures. Some issues appear as incorrect totals, missing relationships, duplicate records, invalid values, or inconsistent data.

## Tools Planned

For this phase, I plan to use:

- SQLite
- DB Browser for SQLite
- SQL scripts
- Local sample data
- Markdown documentation

## Important Limitation

This phase is a local validation simulation based on API-like data.

It does not validate DummyJSON's real production database and does not claim direct database access.
