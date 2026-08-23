-- Set 2 SQL solutions (MySQL 8+).

-- 1. Repeated payments at the same merchant using the same card and amount
-- within ten minutes. Assumed table:
-- Transactions(transaction_id, merchant_id, card_id, transaction_date, amount,
--              transaction_timestamp)
WITH ordered_payments AS (
    SELECT t.*,
           LAG(transaction_timestamp) OVER (
               PARTITION BY merchant_id, card_id, amount
               ORDER BY transaction_timestamp
           ) AS previous_payment_time
    FROM Transactions t
)
SELECT transaction_id, merchant_id, card_id, amount, transaction_timestamp
FROM ordered_payments
WHERE TIMESTAMPDIFF(MINUTE, previous_payment_time, transaction_timestamp) <= 10;

-- Count of such repeated payments.
WITH ordered_payments AS (
    SELECT t.*,
           LAG(transaction_timestamp) OVER (
               PARTITION BY merchant_id, card_id, amount
               ORDER BY transaction_timestamp
           ) AS previous_payment_time
    FROM Transactions t
)
SELECT COUNT(*) AS repeated_payment_count
FROM ordered_payments
WHERE TIMESTAMPDIFF(MINUTE, previous_payment_time, transaction_timestamp) <= 10;

-- 2. Median searches made by a user from the frequency summary table.
-- Assumed table: SearchFrequency(searches, num_users)
WITH ranges AS (
    SELECT searches,
           num_users,
           SUM(num_users) OVER (ORDER BY searches) AS cumulative_users,
           SUM(num_users) OVER (ORDER BY searches) - num_users AS previous_users,
           SUM(num_users) OVER () AS total_users
    FROM SearchFrequency
)
SELECT AVG(searches) AS median_searches
FROM ranges
WHERE cumulative_users >= FLOOR((total_users + 1) / 2)
  AND previous_users < CEIL((total_users + 1) / 2);

-- 3. Odd- and even-numbered measurement totals for each date.
-- Assumed table: Measurements(measurement_id, measurement_value, measurement_time)
WITH numbered_measurements AS (
    SELECT DATE(measurement_time) AS measurement_date,
           measurement_value,
           ROW_NUMBER() OVER (
               PARTITION BY DATE(measurement_time)
               ORDER BY measurement_time
           ) AS measurement_number
    FROM Measurements
)
SELECT measurement_date,
       SUM(CASE WHEN measurement_number % 2 = 1 THEN measurement_value ELSE 0 END)
           AS odd_measurements,
       SUM(CASE WHEN measurement_number % 2 = 0 THEN measurement_value ELSE 0 END)
           AS even_measurements
FROM numbered_measurements
GROUP BY measurement_date
ORDER BY measurement_date;
