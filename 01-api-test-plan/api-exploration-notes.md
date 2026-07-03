# API Exploration Notes

This document contains initial API exploration notes for the DummyJSON E-Commerce API QA Portfolio project.

The purpose of this step is to understand the available API responses before creating Postman requests and detailed test cases.

## Base URL

[https://dummyjson.com](https://dummyjson.com)

## Explored Endpoints

| Endpoint | Observation | QA Relevance |
|---|---|---|
| [`GET /products`](https://dummyjson.com/products) | Returns a list of products with pagination metadata such as `total`, `skip`, and `limit` | Useful for validating response structure, required fields, product list behavior, and pagination |
| [`GET /products/1`](https://dummyjson.com/products/1) | Returns a single product object | Useful for validating product details and required product fields |
| [`GET /products/search?q=phone`](https://dummyjson.com/products/search?q=phone) | Returns products matching a search keyword | Useful for testing search behavior and result relevance |
| [`GET /products/categories`](https://dummyjson.com/products/categories) | Returns available product categories | Useful for testing category availability and structure |
| [`GET /carts`](https://dummyjson.com/carts) | Returns a list of carts with cart totals, products, quantities, and user IDs | Useful for cart validation and later SQL business-rule checks |
| [`GET /carts/1`](https://dummyjson.com/carts/1) | Returns a single cart object | Useful for validating cart structure and product details inside a cart |
| [`GET /carts/user/5`](https://dummyjson.com/carts/user/5) | Returns carts connected to a specific user ID | Useful for testing user/cart relationship logic |
| [`GET /users/1`](https://dummyjson.com/users/1) | Returns a single user object with identity, contact, address, company, and additional profile data | Useful for validating user structure and user/cart relationship logic |

## Product Response Structure Observed

The product list response contains:

- `products`
- `total`
- `skip`
- `limit`

Each product object may include fields such as:

- `id`
- `title`
- `description`
- `category`
- `price`
- `discountPercentage`
- `rating`
- `stock`
- `tags`
- `brand`
- `sku`
- `weight`
- `dimensions`
- `warrantyInformation`
- `shippingInformation`
- `availabilityStatus`
- `reviews`
- `returnPolicy`
- `minimumOrderQuantity`
- `meta`
- `images`
- `thumbnail`

### Nested Product Dimensions Structure

Each product may include a `dimensions` object.

The `dimensions` object may include fields such as:

- `width`
- `height`
- `depth`

### Nested Product Review Structure

Each product may include a `reviews` array.

Each review object may include fields such as:

- `rating`
- `comment`
- `date`
- `reviewerName`
- `reviewerEmail`

These fields belong to product reviews, not to the main user endpoint.

### Nested Product Meta Structure

Each product may include a `meta` object.

The `meta` object may include fields such as:

- `createdAt`
- `updatedAt`
- `barcode`
- `qrCode`

## Product Fields Most Relevant for Testing

Not every product field needs deep validation in this beginner portfolio project.

The most important product fields for API testing are:

- `id`
- `title`
- `description`
- `category`
- `price`
- `discountPercentage`
- `rating`
- `stock`
- `brand`
- `availabilityStatus`
- `images`
- `thumbnail`

These fields are useful for response validation, required-field checks, product search testing, category testing, and basic product data quality checks.

## Product Validation Ideas

Product data can support API validation checks such as:

- Product list response returns status code `200`
- Product list response contains `products`, `total`, `skip`, and `limit`
- Each product has a unique `id`
- Each product has a non-empty `title`
- Each product has a valid `category`
- Product `price` is greater than or equal to `0`
- Product `discountPercentage` is not negative
- Product `rating` is within a logical range
- Product `stock` is not negative
- Product search returns relevant results for the search keyword
- Product category endpoint returns products from the selected category
- Pagination returns the expected number of products based on `limit` and `skip`

## Cart Response Structure Observed

The cart list response contains:

- `carts`
- `total`
- `skip`
- `limit`

Each cart object may include fields such as:

- `id`
- `products`
- `total`
- `discountedTotal`
- `userId`
- `totalProducts`
- `totalQuantity`

Each product inside a cart may include fields such as:

- `id`
- `title`
- `price`
- `quantity`
- `total`
- `discountPercentage`
- `discountedTotal`
- `thumbnail`

## Cart Fields Most Relevant for Testing

The most important cart fields for API and SQL validation are:

- cart `id`
- cart `products`
- cart `total`
- cart `discountedTotal`
- cart `userId`
- cart `totalProducts`
- cart `totalQuantity`
- product `id`
- product `title`
- product `price`
- product `quantity`
- product `total`
- product `discountPercentage`
- product `discountedTotal`
- product `thumbnail`

## Cart Validation Ideas

Cart data is useful for business-rule validation because we can later check:

- Product line total: `price * quantity`
- Product discounted total after discount
- Cart total equals the sum of product totals
- Cart discounted total equals the sum of product discounted totals
- `totalProducts` matches the number of product lines in the cart
- `totalQuantity` matches the sum of product quantities
- Each cart has a valid `userId`
- Each cart product has a valid product `id`
- Quantity values are greater than `0`
- Discount values are not negative

## User Response Structure Observed

User endpoints are included mainly because carts are connected to users through `userId`.

The `GET /users/1` endpoint returns a single user object with identity, contact, address, company, and additional profile-related fields.

A user object may include fields such as:

- `id`
- `firstName`
- `lastName`
- `maidenName`
- `age`
- `gender`
- `email`
- `phone`
- `username`
- `password`
- `birthDate`
- `image`
- `bloodGroup`
- `height`
- `weight`
- `eyeColor`
- `hair`
- `ip`
- `address`
- `macAddress`
- `university`
- `bank`
- `company`
- `ein`
- `ssn`
- `userAgent`
- `crypto`
- `role`

### Nested User Address Structure

Each user may include an `address` object.

The `address` object may include fields such as:

- `address`
- `city`
- `state`
- `stateCode`
- `postalCode`
- `coordinates`
- `country`

### Nested User Company Structure

Each user may include a `company` object.

The `company` object may include fields such as:

- `department`
- `name`
- `title`
- `address`

## User Fields Most Relevant for Testing

Not every user field needs deep validation in this project.

The most important user fields for this project are:

- `id`
- `firstName`
- `lastName`
- `email`
- `username`
- `role`

These fields are enough for basic user response validation and user/cart relationship checks.

Fields such as `password`, `bank`, `crypto`, `ssn`, and `ein` are not the main testing focus for this beginner portfolio project.

## User Validation Ideas

User data can support checks such as:

- User list response returns status code `200`
- Single user endpoint returns the requested user ID
- User response contains required identity fields
- User `id` is numeric
- User `email` is not empty
- User `username` is not empty
- Cart `userId` connects to an existing user
- User carts endpoint returns carts related to the selected user

## Authentication Exploration Note

Authentication endpoints are included in the project scope, but they were not tested in the browser during this initial exploration step.

Authentication will be explored later in Postman because login requires a `POST` request body and token handling.

## Initial QA Notes

- Products and carts are the strongest areas for this project.
- Product endpoints support catalog, search, category, and pagination testing.
- Cart endpoints support deeper validation because they include quantities, prices, totals, discounts, and user IDs.
- User endpoints are useful mainly for validating relationships between users and carts.
- Authentication will be tested later at a basic level only.
- SQL validation will use local API-like data and will not claim access to DummyJSON internal databases.
- Not every returned field needs deep validation. The project will focus on fields that are important for API behavior, business rules, and data validation.
