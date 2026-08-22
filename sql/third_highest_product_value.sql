-- Assumed table: Product(prod_code, prod_name, price, qty)
-- Third-highest DISTINCT price * quantity value. Handles ties correctly.
SELECT prod_code, prod_name, price, qty, price * qty AS total_value
FROM (
    SELECT p.*,
           DENSE_RANK() OVER (ORDER BY price * qty DESC) AS value_rank
    FROM Product p
) AS ranked_products
WHERE value_rank = 3;
