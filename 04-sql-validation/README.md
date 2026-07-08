# SQL Validation

In this folder, I document the SQL validation phase of the DummyJSON E-Commerce API QA project.

Because DummyJSON does not provide direct access to its internal database, I use a small local API-like dataset instead of claiming real backend database access.

The goal of this section is to show how SQL can support QA work by validating data quality, relationships, and business rules around e-commerce data.

## Files

| File | Purpose |
|---|---|
| [`sql-validation-plan.md`](./sql-validation-plan.md) | Explains the SQL validation approach, planned tables, validation areas, and project limitation |

## What I Plan to Validate

The SQL validation phase will focus on:

- Local user data
- Local product data
- Local cart data
- Local cart item data
- Duplicate ID checks
- Missing value checks
- Invalid product references
- Invalid user references
- Negative price checks
- Negative quantity checks
- Cart total validation
- Cart discounted total validation
- Cart quantity validation
- Basic product/category analysis

## Why This Section Matters

The Postman collection validates API responses directly.

The SQL validation section shows how I would check the same type of e-commerce data from a structured database perspective.

This helps demonstrate that I can think beyond simple API status codes and also validate:

- Data consistency
- Data relationships
- Business-rule calculations
- Data quality issues

## Important Limitation

This section uses local API-like data.

It does not validate DummyJSON's real production database and does not claim direct database access.
