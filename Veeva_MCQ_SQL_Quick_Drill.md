# Veeva MCQ and SQL Quick Drill

Use this after coding revision. Goal: maximize easy marks in MCQs and SQL.

## Java/OOP MCQ Drill

1. Which keyword is used to inherit a class? - `extends`
2. Which keyword is used to implement an interface? - `implements`
3. Can constructor have return type? - No
4. Can abstract class have constructor? - Yes
5. Can interface have constructor? - No
6. Return type alone can overload method. True/False? - False
7. Method overriding needs inheritance. True/False? - True
8. `static` belongs to what? - Class
9. `this` refers to what? - Current object
10. Which access modifier is most restrictive? - `private`
11. Which access modifier allows same package and subclass access? - `protected`
12. Java supports multiple inheritance through what? - Interfaces
13. Which block always executes in exception handling? - `finally`
14. Invalid array index causes which exception? - `ArrayIndexOutOfBoundsException`
15. Calling method on null causes which exception? - `NullPointerException`

## Java Tricky Output Drill

16. What is output?
```java
System.out.println("5" + 5);
```
Answer: `55`

17. What is output?
```java
System.out.println(5 + 5 + "5");
```
Answer: `105`

18. What is output?
```java
System.out.println("5" + 5 + 5);
```
Answer: `555`

19. What is output?
```java
String s = "Java";
s.replace('J', 'P');
System.out.println(s);
```
Answer: `Java`

20. What is output?
```java
String s = "Java";
s = s.replace('J', 'P');
System.out.println(s);
```
Answer: `Pava`

21. What is output?
```java
int[] arr = {1, 2, 3};
System.out.println(arr[3]);
```
Answer: Error / `ArrayIndexOutOfBoundsException`

22. How many times does this loop run?
```java
for (int i = 0; i <= 100; i += 5)
```
Answer: 21

23. What does `continue` do? - Skips current iteration
24. What does `break` do? - Exits loop/switch
25. What is output?
```java
int a = 10, b = 5, c = 20;
System.out.println(a + b * c);
```
Answer: 110

## Collections MCQ Drill

26. Which map maintains insertion order? - `LinkedHashMap`
27. Which map sorts keys? - `TreeMap`
28. Which collection stores unique values? - `Set`
29. Which collection uses key-value pairs? - `Map`
30. Which class is commonly used for frequency count? - `HashMap`
31. Which class is commonly used for uniqueness/presence? - `HashSet`
32. Stack follows which order? - LIFO
33. Queue follows which order? - FIFO
34. Stack insertion operation? - `push`
35. Stack deletion operation? - `pop`
36. Stack top read operation? - `peek`
37. Queue insertion operation? - `offer` / enqueue
38. Queue deletion operation? - `poll` / dequeue
39. Modifying collection during fail-fast iteration throws? - `ConcurrentModificationException`
40. Root interface of collection hierarchy? - `Collection`

## Complexity MCQ Drill

41. Single loop from `1` to `n` complexity? - `O(n)`
42. Nested loop `n` and `n` complexity? - `O(n^2)`
43. Nested loop `n` and `m` complexity? - `O(nm)`
44. Binary search best case? - `O(1)`
45. Binary search worst case? - `O(log n)`
46. Loop `i = i * 2` until `n`? - `O(log n)`
47. Loop condition `j * j <= n`? - `O(sqrt(n))`
48. Sorting complexity usually? - `O(n log n)`
49. HashMap average lookup? - `O(1)`
50. Huffman tree build complexity? - `O(n log n)`

## DBMS/SQL MCQ Drill

51. Primary key allows null? - No
52. Foreign key refers to what? - Primary key of another table
53. 1NF removes what? - Repeating groups / non-atomic values
54. 2NF removes what? - Partial dependency
55. 3NF removes what? - Transitive dependency
56. ACID full form? - Atomicity, Consistency, Isolation, Durability
57. Committed data remains saved after failure. Which ACID property? - Durability
58. Transaction happens fully or not at all. Which property? - Atomicity
59. `WHERE` filters what? - Rows before grouping
60. `HAVING` filters what? - Groups after grouping
61. `INNER JOIN` returns what? - Matching rows only
62. `LEFT JOIN` returns what? - All left rows plus matching right rows
63. `CROSS JOIN` returns what? - Cartesian product
64. `EXCEPT` does what? - Rows in first query but not in second
65. `DISTINCT` removes what? - Duplicates

## SQL Query Templates

### 1. Second Highest Salary
```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
);
```

### 2. Employees Above Average Salary
```sql
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

### 3. Employee With Department Name
```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;
```

### 4. All Employees Even Without Department
```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;
```

### 5. Department-Wise Employee Count Including Zero
```sql
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
```

### 6. Filter Groups Using HAVING
```sql
SELECT dept_id, COUNT(*) AS total
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 5;
```

### 7. Online Customers But Not Store Customers
```sql
SELECT customer_id
FROM orders
WHERE order_type = 'Online'

EXCEPT

SELECT customer_id
FROM orders
WHERE order_type = 'Store';
```

### 8. Customers Who Bought Electronics But Not Clothing/Footwear
```sql
SELECT c.customer_id, c.name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items i ON o.order_id = i.order_id
JOIN Products p ON i.product_id = p.product_id
GROUP BY c.customer_id, c.name
HAVING SUM(CASE WHEN p.category = 'Electronics' THEN 1 ELSE 0 END) > 0
AND SUM(CASE WHEN p.category IN ('Clothing', 'Footwear') THEN 1 ELSE 0 END) = 0;
```

### 9. Average Per Item
```sql
SELECT Item,
       ROUND(AVG(Cook_time), 1) AS Average_cook,
       ROUND(AVG(Pack_time), 1) AS Average_pack,
       ROUND(AVG(Delay_time), 1) AS Average_delay
FROM Orders
GROUP BY Item;
```

### 10. Third Transaction Per User
```sql
WITH ranktran AS (
    SELECT user_id, spend, transaction_date,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY transaction_date ASC
           ) AS rn
    FROM transactions
)
SELECT user_id, spend, transaction_date
FROM ranktran
WHERE rn = 3;
```

## One-Hour Revision Plan

1. 20 minutes - Java/OOP tricky MCQs
2. 15 minutes - Complexity MCQs
3. 25 minutes - SQL templates from memory
