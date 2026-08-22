-- Assumed tables:
-- Salesman(sid, name, city)
-- Customer(cid, name, city)

-- Number of salesmen who live in the same city as Davis.
SELECT COUNT(*) AS salesman_count
FROM Salesman
WHERE city IN (
    SELECT city
    FROM Customer
    WHERE name = 'Davis'
);

-- Salespeople who do not live in the cities of Carmen, Green, or John.
SELECT sid, name, city
FROM Salesman
WHERE city NOT IN (
    SELECT city
    FROM Customer
    WHERE name IN ('Carmen', 'Green', 'John')
);
