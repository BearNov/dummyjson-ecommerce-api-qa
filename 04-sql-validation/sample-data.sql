PRAGMA foreign_keys = ON;

DELETE FROM cart_items;
DELETE FROM carts;
DELETE FROM products;
DELETE FROM users;

INSERT INTO users (
    user_id,
    first_name,
    last_name,
    email,
    username,
    role
)
VALUES
    (1, 'Emily', 'Johnson', 'emily.johnson@example.com', 'emilyj', 'user'),
    (5, 'David', 'Miller', 'david.miller@example.com', 'davidm', 'user'),
    (7, 'Sophia', 'Brown', 'sophia.brown@example.com', 'sophiab', 'user');

INSERT INTO products (
    product_id,
    title,
    category,
    price,
    discount_percentage,
    rating,
    stock,
    brand,
    availability_status
)
VALUES
    (101, 'Wireless Mouse', 'accessories', 100.00, 10.00, 4.5, 50, 'Logitech', 'In Stock'),
    (102, 'USB-C Hub', 'accessories', 50.00, 20.00, 4.2, 30, 'Anker', 'In Stock'),
    (103, 'Phone Case', 'smartphones', 20.00, 0.00, 4.0, 100, 'Generic', 'In Stock'),
    (104, 'Screen Protector', 'smartphones', 30.00, 5.00, 4.1, 80, 'Spigen', 'In Stock'),
    (105, 'Bluetooth Speaker', 'audio', 200.00, 15.00, 4.7, 20, 'JBL', 'In Stock');

INSERT INTO carts (
    cart_id,
    user_id,
    total,
    discounted_total,
    total_products,
    total_quantity
)
VALUES
    (1, 5, 250.00, 220.00, 2, 3),
    (2, 1, 120.00, 117.00, 2, 5),
    (3, 7, 300.00, 260.00, 2, 2);

INSERT INTO cart_items (
    cart_id,
    product_id,
    title,
    price,
    quantity,
    total,
    discount_percentage,
    discounted_total
)
VALUES
    (1, 101, 'Wireless Mouse', 100.00, 2, 200.00, 10.00, 180.00),
    (1, 102, 'USB-C Hub', 50.00, 1, 50.00, 20.00, 40.00),
    (2, 103, 'Phone Case', 20.00, 3, 60.00, 0.00, 60.00),
    (2, 104, 'Screen Protector', 30.00, 2, 60.00, 5.00, 57.00),
    (3, 105, 'Bluetooth Speaker', 200.00, 1, 200.00, 15.00, 170.00),
    (3, 101, 'Wireless Mouse', 100.00, 1, 100.00, 10.00, 90.00);
