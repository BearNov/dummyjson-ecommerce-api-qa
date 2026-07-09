# SQL Validation

In this folder, I document the SQL validation phase of the DummyJSON E-Commerce API QA project.

Because DummyJSON does not provide direct access to its internal database, I used a small local API-like SQLite dataset instead of claiming real backend database access.

The goal of this section is to show how SQL can support QA work by validating data quality, relationships, and business rules around e-commerce data.

## Files

| File | Purpose |
|---|---|
| [`sql-validation-plan.md`](./sql-validation-plan.md) | Explains the SQL validation approach, planned tables, validation areas, and project limitation |
| [`schema.sql`](./schema.sql) | Creates the local SQLite database tables |
| [`sample-data.sql`](./sample-data.sql) | Inserts local API-like e-commerce sample data |
| [`validation-queries.sql`](./validation-queries.sql) | Contains SQL validation queries for record counts, duplicates, missing values, relationships, calculations, and joins |
| [`sql-validation-results.md`](./sql-validation-results.md) | Documents the SQL validation execution results |

## Local Database Structure

The local SQLite database contains four main tables:

| Table | Purpose |
|---|---|
| `users` | Stores local user identity data |
| `products` | Stores local product data |
| `carts` | Stores cart-level data |
| `cart_items` | Stores product lines inside carts |

These tables support validation across the same e-commerce areas tested in Postman:

- Users
- Products
- Carts
- Cart items
- User/cart relationships
- Product references
- Cart calculations

## What I Validated

The SQL validation phase checks:

- Record counts
- Duplicate user IDs
- Duplicate product IDs
- Missing required user fields
- Missing required product fields
- Invalid email format
- Invalid product numeric values
- Carts connected to missing users
- Cart items connected to missing carts
- Cart items connected to missing products
- Invalid cart item numeric values
- Cart item total calculations
- Cart total calculations
- Cart discounted total calculations
- Cart product count calculations
- Cart quantity calculations
- Joined cart/user/product view

## Execution Tool

I ran the SQL scripts locally using [DB Browser for SQLite](https://sqlitebrowser.org/).

The execution flow was:

1. Run `schema.sql` to create the database tables.
2. Run `sample-data.sql` to insert the local sample data.
3. Run `validation-queries.sql` query by query.
4. Document the results in `sql-validation-results.md`.

## Result Summary

The local SQL validation phase passed successfully.

| Area | Result |
|---|---|
| Record count checks | PASS |
| Duplicate checks | PASS |
| Required-field checks | PASS |
| Numeric validation checks | PASS |
| Relationship checks | PASS |
| Cart calculation checks | PASS |
| Joined cart view | PASS |

## Important Limitation

This section uses local API-like data.

It does not validate DummyJSON's real production database and does not claim direct database access.

The purpose is to demonstrate how I can use SQL for QA-style data validation when working with structured e-commerce data.
