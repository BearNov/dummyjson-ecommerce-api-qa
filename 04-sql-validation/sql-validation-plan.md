# SQL Validation Plan

## Overview

I created this plan to explain how I use SQL validation in the DummyJSON E-Commerce API QA Portfolio project.

Because DummyJSON does not provide direct access to its internal database, I used a local API-like SQLite dataset instead of claiming real backend database access.

The purpose of this phase is to show how SQL can support QA work by validating data quality, relationships, and business-rule calculations around e-commerce data.

## Tools Used

| Tool | Purpose |
|---|---|
| [SQLite](https://www.sqlite.org/) | Local relational database engine |
| [DB Browser for SQLite](https://sqlitebrowser.org/) | Visual tool used to create and run the local SQLite database |
| SQL | Used for validation queries, joins, calculations, and data-quality checks |

## Related Files

| File | Purpose |
|---|---|
| [`schema.sql`](./schema.sql) | Creates the local database tables |
| [`sample-data.sql`](./sample-data.sql) | Inserts local API-like e-commerce sample data |
| [`validation-queries.sql`](./validation-queries.sql) | Contains the SQL validation checks |
| [`sql-validation-results.md`](./sql-validation-results.md) | Documents the SQL validation execution results |

## Local Database Tables

The local SQLite database contains four main tables.

| Table | Purpose |
|---|---|
| `users` | Stores local user identity data |
| `products` | Stores local product data |
| `carts` | Stores cart-level data |
| `cart_items` | Stores product lines inside carts |

These tables represent the same e-commerce areas tested in Postman and Python automation.

## Data Relationship Model

The local dataset follows this relationship structure:

| Relationship | Meaning |
|---|---|
| `users.user_id` → `carts.user_id` | A cart belongs to a user |
| `carts.cart_id` → `cart_items.cart_id` | A cart contains cart item rows |
| `products.product_id` → `cart_items.product_id` | A cart item references a product |

This structure allows me to validate user/cart relationships, product references, and cart-level business rules.

## Validation Areas

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
- Joined cart detail view

## Business Rules Checked

The SQL queries validate business rules such as:

| Business Rule | Validation Logic |
|---|---|
| Cart item total | `price * quantity = total` |
| Cart total | Cart total equals the sum of cart item totals |
| Cart discounted total | Cart discounted total equals the sum of item discounted totals |
| Total products | `total_products` equals the number of product lines in the cart |
| Total quantity | `total_quantity` equals the sum of item quantities |
| User/cart relationship | Every cart should belong to an existing user |
| Product/cart relationship | Every cart item should reference an existing product |

## Expected Results

For most issue-detection queries, the expected result is:

`0 rows returned`

In this project, `0 rows returned` means the query did not find a data issue.

For the final joined cart view, the expected result is rows returned, because that query is used to display connected user, cart, cart item, and product data.

## Execution Summary

I ran the SQL scripts locally in this order:

1. `schema.sql`
2. `sample-data.sql`
3. `validation-queries.sql`

The validation results were documented in:

[`sql-validation-results.md`](./sql-validation-results.md)

## Important Limitation

This SQL validation phase uses local API-like sample data.

It does not validate DummyJSON's real production database and does not claim direct access to DummyJSON internal data.

The goal is to demonstrate SQL-based QA thinking, data validation, relationship checks, and business-rule validation in a realistic local e-commerce dataset.
