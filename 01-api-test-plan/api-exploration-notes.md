# API Exploration Notes

I used this file to document my initial exploration of the DummyJSON E-Commerce API before building the Postman collection and detailed test cases.

The goal of this step was to understand the available API responses, identify useful fields for testing, and decide which parts of the API should be included in the first version of the project.

## Base URL

[https://dummyjson.com](https://dummyjson.com)

## Explored Endpoints

| Endpoint | Observation | QA Relevance |
|---|---|---|
| [`GET /products`](https://dummyjson.com/products) | Returns a list of products with pagination metadata such as `total`, `skip`, and `limit` | Useful for validating response structure, required fields, product list behavior, and pagination |
| [`GET /products/1`](https://dummyjson.com/products/1) | Returns a single product object | Useful for validating product details and required product fields |
| [`GET /products/search?q=phone`](https://dummyjson.com/products/search?q=phone) | Returns products matching a search keyword | Useful for testing search behavior and result relevance |
| [`GET /products?limit=10&skip=10`](https://dummyjson.com/products?limit=10&skip=10) | Returns a limited product list with skipped records | Useful for validating pagination behavior |
| [`GET /products/categories`](https://dummyjson.com/products/categories) | Returns available product categories | Useful for testing category availability and category structure |
| [`GET /products/category/smartphones`](https://dummyjson.com/products/category/smartphones) | Returns products from the smartphones category | Useful for validating category filtering |
| [`GET /carts`](https://dummyjson.com/carts) | Returns a list of carts with totals, products, quantities, and user IDs | Useful for cart validation and later SQL business-rule checks |
| [`GET /carts/1`](https://dummyjson.com/carts/1) | Returns a single cart object | Useful for validating cart structure and product details inside a cart |
| [`GET /carts/user/5`](https://dummyjson.com/carts/user/5) | Returns carts connected to a specific user ID | Useful for testing user/cart relationship logic |
| [`GET /users`](https://dummyjson.com/users) | Returns a list of users | Useful for validating user structure and checking that user ID 5 exists for cart relationship testing |
| [`GET /users/1`](https://dummyjson.com/users/1) | Returns a single user object with identity, address, company, and profile data | Useful for validating user structure |
| [`GET /users/5/carts`](https://dummyjson.com/users/5/carts) | Returns carts connected to user ID 5 | Useful for validating the same user/cart relationship from the user side |
| [`POST /auth/login`](https://dummyjson.com/auth/login) | Returns authentication tokens for valid demo credentials | Useful for testing login and token generation |
| [`GET /auth/me`](https://dummyjson.com/auth/me) | Returns the authenticated user when a valid Bearer token is provided | Useful for testing token-based authentication |
| [`POST /auth/login` with invalid credentials](https://dummyjson.com/auth/login) | Returns an error response | Useful for negative authentication testing |

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

## Nested Product Dimensions Structure

Each product may include a `dimensions` object.

The `dimensions` object may include:

- `width`
- `height`
- `depth`

## Nested Product Review Structure

Each product may include a `reviews` array.

Each review object may include:

- `rating`
- `comment`
- `date`
- `reviewerName`
- `reviewerEmail`

I treated these fields as product review data, not as main user endpoint data.

## Nested Product Meta Structure

Each product may include a `meta` object.

The `meta` object may include:

- `createdAt`
- `updatedAt`
- `barcode`
- `qrCode`

## Product Fields Most Relevant for Testing

Not every product field needs deep validation in this beginner portfolio project.

I focused mainly on fields that support API behavior, product data quality, search, category filtering, and later SQL validation:

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

## Product Validation Ideas

Product data can support API validation checks such as:

- Product list response returns status code `200`
- Product list response contains `products`, `total`, `skip`, and `limit`
- Each product has a valid `id`
- Each product has a non-empty `title`
- Each product has a valid `category`
- Product `price` is greater than or equal to `0`
- Product `discountPercentage` is not negative
- Product `rating` is within a logical range
- Product `stock` is not negative
- Product search returns results related to the search keyword
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

I treated carts as one of the most important areas in this project because they support both API validation and business-rule validation.

The most important cart fields are:

- cart `id`
- cart `products`
- cart `total`
- cart `discountedTotal`
- cart `userId`
- cart `totalProducts`
- cart `totalQuantity`
- cart product `id`
- cart product `title`
- cart product `price`
- cart product `quantity`
- cart product `total`
- cart product `discountPercentage`
- cart product `discountedTotal`
- cart product `thumbnail`

## Cart Validation Ideas

Cart data is useful for business-rule validation because I can check:

- Product line total
- Product discounted total
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

The user endpoints help me validate relationships between:

- Users
- Carts
- User-specific cart results

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

## Nested User Address Structure

Each user may include an `address` object.

The `address` object may include:

- `address`
- `city`
- `state`
- `stateCode`
- `postalCode`
- `coordinates`
- `country`

## Nested User Company Structure

Each user may include a `company` object.

The `company` object may include:

- `department`
- `name`
- `title`
- `address`

## User Fields Most Relevant for Testing

Not every user field needs deep validation in this project.

I focused mainly on user identity fields that support basic user validation and user/cart relationship testing:

- `id`
- `firstName`
- `lastName`
- `email`
- `username`
- `role`

Fields such as `password`, `bank`, `crypto`, `ssn`, and `ein` are not the main testing focus for this beginner portfolio project.

## User Validation Ideas

User data can support checks such as:

- User list response returns status code `200`
- Single user endpoint returns the requested user ID
- User response contains required identity fields
- User `id` is numeric
- User `email` is not empty and contains `@`
- User `username` is not empty
- User IDs are unique
- Cart `userId` connects to an existing user
- User carts endpoint returns carts related to the selected user

## Authentication Exploration Notes

Authentication was tested in Postman because login requires a `POST` request body and token handling.

The authentication flow includes:

1. Sending valid login credentials
2. Receiving an `accessToken` and `refreshToken`
3. Saving the token into the Postman environment
4. Using the token in `GET /auth/me`
5. Comparing the authenticated user response against the login response

I also added a negative authentication test for invalid credentials.

## Initial QA Conclusions

After exploring the API, I selected products, carts, users, and authentication as the main project areas.

The strongest validation areas are:

- Product catalog validation
- Product search validation
- Product category validation
- Pagination validation
- Cart calculation validation
- User/cart relationship validation
- Token-based authentication
- Invalid login negative testing

Products and carts are especially useful because they allow the project to go beyond simple status-code checks.

Cart data supports deeper QA validation because it includes:

- Quantities
- Prices
- Totals
- Discounts
- User IDs
- Product IDs

These fields also connect naturally to the later SQL validation phase.

## Important Limitation

DummyJSON does not provide direct database access.

Because of that, the SQL validation phase will use local API-like data and will not claim access to DummyJSON internal databases.
