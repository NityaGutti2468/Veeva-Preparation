-- Assumed table: Product(product_id, product_code, product_name, category, price)

-- Products in a given category, together with the product count and highest price.
SELECT product_id, product_code, product_name, category, price,
       COUNT(*) OVER (PARTITION BY category) AS products_in_category,
       MAX(price) OVER (PARTITION BY category) AS highest_price_in_category
FROM Product
WHERE category = 'Electronics';

-- Display products category-wise, with expensive products first in each category.
SELECT product_id, product_code, product_name, category, price
FROM Product
ORDER BY category, price DESC;

-- Category containing the product with the highest price.
SELECT DISTINCT category
FROM Product
WHERE price = (SELECT MAX(price) FROM Product);
