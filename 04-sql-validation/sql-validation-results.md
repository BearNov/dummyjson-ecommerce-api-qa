# SQL Validation Results

## Overview

I created this file to document the results of the local SQL validation phase for the DummyJSON E-Commerce API QA project.

The SQL validation was executed locally using [DB Browser for SQLite](https://sqlitebrowser.org/) and a local SQLite database file.

The local database was created from the project SQL scripts:

| File | Purpose |
|---|---|
| [`schema.sql`](./schema.sql) | Creates the local database tables |
| [`sample-data.sql`](./sample-data.sql) | Inserts local API-like e-commerce sample data |
| [`validation-queries.sql`](./validation-queries.sql) | Contains SQL checks for data quality, relationships, calculations, and joined views |

## Important Limitation

DummyJSON does not provide direct access to its real production database.

Because of that, I used a local API-like SQLite dataset to demonstrate how SQL can support QA validation.

This phase does not claim to validate DummyJSON's internal database.

## Local Database Tables

The local database contains four main tables:

| Table | Purpose |
|---|---|
| `users` | Stores local user identity data |
| `products` | Stores local product data |
| `carts` | Stores cart-level data |
| `cart_items` | Stores product lines inside carts |

SQLite also created `sqlite_sequence` automatically because `cart_items.cart_item_id` uses `AUTOINCREMENT`.

## Record Count Check

The first query confirmed that the local sample data was inserted correctly.

| Table | Expected Rows | Actual Rows | Result |
|---|---:|---:|---|
| `users` | 3 | 3 | PASS |
| `products` | 5 | 5 | PASS |
| `carts` | 3 | 3 | PASS |
| `cart_items` | 6 | 6 | PASS |

## Validation Result Summary

For most validation checks, the expected result was `0 rows returned`.

In these checks, `0 rows` means the query did not find a data issue.

| # | Validation Check | Expected Result | Actual Result | Status |
|---:|---|---|---|---|
| 1 | Duplicate user ID check | 0 rows | 0 rows | PASS |
| 2 | Duplicate product ID check | 0 rows | 0 rows | PASS |
| 3 | Missing required user fields | 0 rows | 0 rows | PASS |
| 4 | Missing required product fields | 0 rows | 0 rows | PASS |
| 5 | Invalid email format check | 0 rows | 0 rows | PASS |
| 6 | Invalid product numeric values | 0 rows | 0 rows | PASS |
| 7 | Carts connected to missing users | 0 rows | 0 rows | PASS |
| 8 | Cart items connected to missing carts | 0 rows | 0 rows | PASS |
| 9 | Cart items connected to missing products | 0 rows | 0 rows | PASS |
| 10 | Invalid cart item numeric values | 0 rows | 0 rows | PASS |
| 11 | Cart item total calculation check | 0 rows | 0 rows | PASS |
| 12 | Cart total calculation check | 0 rows | 0 rows | PASS |
| 13 | Cart discounted total calculation check | 0 rows | 0 rows | PASS |
| 14 | Cart totalProducts check | 0 rows | 0 rows | PASS |
| 15 | Cart totalQuantity check | 0 rows | 0 rows | PASS |

## Joined Cart View Result

The final query was not an issue-detection query.

Instead, I used it to create a readable joined view across the main e-commerce tables:

- `users`
- `carts`
- `cart_items`
- `products`

Expected result:

| Query | Expected Rows | Actual Rows | Status |
|---|---:|---:|---|
| Full cart detail join | 6 | 6 | PASS |

The joined result showed:

- Cart ID
- User ID
- Customer name
- Product ID
- Product title
- Quantity
- Price
- Line total
- Discounted line total

This confirms that the local tables can be joined successfully and that the relationships between users, carts, cart items, and products are working as expected.

## SQL Validation Conclusion

The local SQL validation phase passed successfully.

The validation checks confirmed that:

- The expected sample records were inserted
- User and product IDs were unique
- Required user and product fields were populated
- Product numeric values were valid
- Cart items had valid numeric values
- Carts were connected to existing users
- Cart items were connected to existing carts
- Cart items were connected to existing products
- Cart item totals matched `price * quantity`
- Cart totals matched the sum of cart item totals
- Cart discounted totals matched the sum of discounted item totals
- Cart product counts matched the number of cart item rows
- Cart quantity totals matched the sum of item quantities
- The main e-commerce tables could be joined into a readable validation view

This phase shows how I used SQL to validate data quality, relationships, and business-rule calculations in a local e-commerce dataset.
