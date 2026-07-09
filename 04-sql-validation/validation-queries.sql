-- ============================================================
-- SQL Validation Queries
-- DummyJSON E-Commerce API QA Portfolio
--
-- These queries validate the local API-like e-commerce dataset.
-- Expected result for most issue-detection queries: 0 rows.
-- ============================================================


-- ============================================================
-- 1. Basic record counts
-- Purpose: confirm that the local dataset contains records
-- ============================================================

SELECT
    'users' AS table_name,
    COUNT(*) AS record_count
FROM users

UNION ALL

SELECT
    'products' AS table_name,
    COUNT(*) AS record_count
FROM products

UNION ALL

SELECT
    'carts' AS table_name,
    COUNT(*) AS record_count
FROM carts

UNION ALL

SELECT
    'cart_items' AS table_name,
    COUNT(*) AS record_count
FROM cart_items;


-- ============================================================
-- 2. Duplicate user ID check
-- Expected result: 0 rows
-- ============================================================

SELECT
    user_id,
    COUNT(*) AS duplicate_count
FROM users
GROUP BY user_id
HAVING COUNT(*) > 1;


-- ============================================================
-- 3. Duplicate product ID check
-- Expected result: 0 rows
-- ============================================================

SELECT
    product_id,
    COUNT(*) AS duplicate_count
FROM products
GROUP BY product_id
HAVING COUNT(*) > 1;


-- ============================================================
-- 4. Missing required user fields
-- Expected result: 0 rows
-- ============================================================

SELECT
    user_id,
    first_name,
    last_name,
    email,
    username,
    role
FROM users
WHERE
    first_name IS NULL OR TRIM(first_name) = ''
    OR last_name IS NULL OR TRIM(last_name) = ''
    OR email IS NULL OR TRIM(email) = ''
    OR username IS NULL OR TRIM(username) = ''
    OR role IS NULL OR TRIM(role) = '';


-- ============================================================
-- 5. Invalid email format check
-- Expected result: 0 rows
-- ============================================================

SELECT
    user_id,
    email
FROM users
WHERE email NOT LIKE '%@%.%';


-- ============================================================
-- 6. Missing required product fields
-- Expected result: 0 rows
-- ============================================================

SELECT
    product_id,
    title,
    category,
    price,
    stock
FROM products
WHERE
    title IS NULL OR TRIM(title) = ''
    OR category IS NULL OR TRIM(category) = ''
    OR price IS NULL
    OR stock IS NULL;


-- ============================================================
-- 7. Invalid product numeric values
-- Expected result: 0 rows
-- ============================================================

SELECT
    product_id,
    title,
    price,
    discount_percentage,
    rating,
    stock
FROM products
WHERE
    price < 0
    OR discount_percentage < 0
    OR discount_percentage > 100
    OR stock < 0
    OR rating < 0
    OR rating > 5;


-- ============================================================
-- 8. Carts connected to missing users
-- Expected result: 0 rows
-- ============================================================

SELECT
    c.cart_id,
    c.user_id
FROM carts c
LEFT JOIN users u
    ON c.user_id = u.user_id
WHERE u.user_id IS NULL;


-- ============================================================
-- 9. Cart items connected to missing carts
-- Expected result: 0 rows
-- ============================================================

SELECT
    ci.cart_item_id,
    ci.cart_id
FROM cart_items ci
LEFT JOIN carts c
    ON ci.cart_id = c.cart_id
WHERE c.cart_id IS NULL;


-- ============================================================
-- 10. Cart items connected to missing products
-- Expected result: 0 rows
-- ============================================================

SELECT
    ci.cart_item_id,
    ci.cart_id,
    ci.product_id,
    ci.title
FROM cart_items ci
LEFT JOIN products p
    ON ci.product_id = p.product_id
WHERE p.product_id IS NULL;


-- ============================================================
-- 11. Invalid cart item numeric values
-- Expected result: 0 rows
-- ============================================================

SELECT
    cart_item_id,
    cart_id,
    product_id,
    price,
    quantity,
    total,
    discount_percentage,
    discounted_total
FROM cart_items
WHERE
    price < 0
    OR quantity <= 0
    OR total < 0
    OR discount_percentage < 0
    OR discount_percentage > 100
    OR discounted_total < 0;


-- ============================================================
-- 12. Cart item total calculation check
-- Formula: price * quantity = total
-- Expected result: 0 rows
-- ============================================================

SELECT
    cart_item_id,
    cart_id,
    product_id,
    price,
    quantity,
    total AS stored_total,
    ROUND(price * quantity, 2) AS calculated_total
FROM cart_items
WHERE ROUND(total, 2) != ROUND(price * quantity, 2);


-- ============================================================
-- 13. Cart total calculation check
-- Formula: cart total = sum of cart item totals
-- Expected result: 0 rows
-- ============================================================

SELECT
    c.cart_id,
    c.total AS stored_cart_total,
    ROUND(SUM(ci.total), 2) AS calculated_cart_total
FROM carts c
JOIN cart_items ci
    ON c.cart_id = ci.cart_id
GROUP BY
    c.cart_id,
    c.total
HAVING ROUND(c.total, 2) != ROUND(SUM(ci.total), 2);


-- ============================================================
-- 14. Cart discounted total calculation check
-- Formula: cart discounted total = sum of item discounted totals
-- Expected result: 0 rows
-- ============================================================

SELECT
    c.cart_id,
    c.discounted_total AS stored_discounted_total,
    ROUND(SUM(ci.discounted_total), 2) AS calculated_discounted_total
FROM carts c
JOIN cart_items ci
    ON c.cart_id = ci.cart_id
GROUP BY
    c.cart_id,
    c.discounted_total
HAVING ROUND(c.discounted_total, 2) != ROUND(SUM(ci.discounted_total), 2);


-- ============================================================
-- 15. Cart totalProducts check
-- Formula: total_products = number of product lines in cart
-- Expected result: 0 rows
-- ============================================================

SELECT
    c.cart_id,
    c.total_products AS stored_total_products,
    COUNT(ci.cart_item_id) AS calculated_total_products
FROM carts c
JOIN cart_items ci
    ON c.cart_id = ci.cart_id
GROUP BY
    c.cart_id,
    c.total_products
HAVING c.total_products != COUNT(ci.cart_item_id);


-- ============================================================
-- 16. Cart totalQuantity check
-- Formula: total_quantity = sum of all item quantities
-- Expected result: 0 rows
-- ============================================================

SELECT
    c.cart_id,
    c.total_quantity AS stored_total_quantity,
    SUM(ci.quantity) AS calculated_total_quantity
FROM carts c
JOIN cart_items ci
    ON c.cart_id = ci.cart_id
GROUP BY
    c.cart_id,
    c.total_quantity
HAVING c.total_quantity != SUM(ci.quantity);


-- ============================================================
-- 17. Full cart detail join
-- Purpose: show users, carts, cart items, and products together
-- This is not an issue check. It is a readable joined view.
-- ============================================================

SELECT
    c.cart_id,
    u.user_id,
    u.first_name || ' ' || u.last_name AS customer_name,
    p.product_id,
    p.title AS product_title,
    ci.quantity,
    ci.price,
    ci.total,
    ci.discounted_total
FROM carts c
JOIN users u
    ON c.user_id = u.user_id
JOIN cart_items ci
    ON c.cart_id = ci.cart_id
JOIN products p
    ON ci.product_id = p.product_id
ORDER BY
    c.cart_id,
    p.product_id;
