-- Today's practice questions.
-- Assumed tables:
-- Customer(cust_id, name, city)
-- CustomerOrders(ord_id, cust_id, order_date, order_amount)

-- 1. Total number of non-June orders placed by each customer.
SELECT c.cust_id, c.name, COUNT(o.ord_id) AS total_orders
FROM Customer c
LEFT JOIN CustomerOrders o
       ON o.cust_id = c.cust_id
      AND MONTH(o.order_date) <> 6
GROUP BY c.cust_id, c.name;

-- 2. Customer(s) having the highest total order value.
WITH customer_totals AS (
    SELECT c.cust_id, c.name, SUM(o.order_amount) AS total_value
    FROM Customer c
    JOIN CustomerOrders o ON o.cust_id = c.cust_id
    GROUP BY c.cust_id, c.name
)
SELECT cust_id, name, total_value
FROM customer_totals
WHERE total_value = (SELECT MAX(total_value) FROM customer_totals);

-- 3. Orders placed between two dates, inclusive.
SELECT ord_id, cust_id, order_date, order_amount
FROM CustomerOrders
WHERE order_date BETWEEN '2023-07-04' AND '2023-07-06';

-- 4. Average order value for each city.
SELECT c.city, AVG(o.order_amount) AS average_order_value
FROM Customer c
JOIN CustomerOrders o ON o.cust_id = c.cust_id
GROUP BY c.city;

-- 5. Customers who have not placed any order.
SELECT c.cust_id, c.name, c.city
FROM Customer c
LEFT JOIN CustomerOrders o ON o.cust_id = c.cust_id
WHERE o.ord_id IS NULL;

-- 6. Month with the highest total order value.
WITH monthly_totals AS (
    SELECT DATE_FORMAT(order_date, '%Y-%m') AS order_month,
           SUM(order_amount) AS total_value
    FROM CustomerOrders
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT order_month, total_value
FROM monthly_totals
WHERE total_value = (SELECT MAX(total_value) FROM monthly_totals);

-- 7. Top two customers with the most orders in the last 30 days.
SELECT c.cust_id, c.name, COUNT(o.ord_id) AS order_count
FROM Customer c
JOIN CustomerOrders o ON o.cust_id = c.cust_id
WHERE o.order_date >= CURDATE() - INTERVAL 30 DAY
GROUP BY c.cust_id, c.name
ORDER BY order_count DESC
LIMIT 2;

-- 8. All orders placed on a chosen date with the corresponding customer name.
SELECT o.ord_id, o.order_date, o.order_amount, c.name AS customer_name
FROM CustomerOrders o
JOIN Customer c ON c.cust_id = o.cust_id
WHERE o.order_date = '2023-07-04';
