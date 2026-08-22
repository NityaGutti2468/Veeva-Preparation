# Veeva Technical Assessment Last-Night Prep

Focus target: answer at least 20 MCQs correctly, solve SQL first, then medium coding, then attempt hard coding.

## High-Yield MCQ Question Bank

### Java Basics and OOP
1. Which keyword is used for inheritance in Java? - extends
2. Which keyword is used to implement an interface? - implements
3. What is polymorphism? - Ability of an object/method to take many forms
4. What is encapsulation? - Binding data and methods together and protecting data
5. Which access modifier supports encapsulation most? - private
6. What is abstraction? - Hiding internal details and showing essential features
7. What is inheritance? - Child class acquiring parent class properties
8. What is a class? - Blueprint for objects
9. What is an object? - Instance of a class
10. Which keyword creates an object? - new
11. Can constructor have return type? - No
12. Constructor name must be same as what? - Class name
13. When is constructor called? - When object is created
14. If no constructor is written, what does Java provide? - Default constructor
15. What does this keyword refer to? - Current object
16. What does static mean? - Belongs to class, not object
17. Are static variables shared by all objects? - Yes
18. Why is main method static? - JVM can call it without object creation
19. Method overloading means what? - Same method name, different parameters
20. Method overriding means what? - Child class redefines parent method
21. Can return type alone overload a method? - No
22. Is inheritance required for overriding? - Yes
23. Compile-time polymorphism is also called? - Method overloading
24. Runtime polymorphism is also called? - Method overriding
25. In `Animal a = new Dog(); a.sound();`, overridden method of which class runs? - Dog
26. Can Java support multiple inheritance using classes? - No
27. Can Java support multiple inheritance using interfaces? - Yes
28. Abstract class can have constructor? - Yes
29. Interface can have constructor? - No
30. Abstract class uses which keyword in child class? - extends
31. Interface uses which keyword in child class? - implements
32. Interface methods are by default what? - public and abstract
33. Can abstract class have normal methods? - Yes
34. Can abstract class have abstract methods? - Yes
35. What is final variable? - Value cannot be changed
36. What is final method? - Cannot be overridden
37. What is final class? - Cannot be inherited
38. What is super keyword used for? - Access parent class members/constructor
39. Which access modifier is accessible everywhere? - public
40. Which access modifier is accessible only inside same class? - private
41. Which modifier allows same package and subclasses? - protected
42. Default access is also called? - package-private
43. What is exception? - Runtime error/event disrupting normal flow
44. Which block always executes in exception handling? - finally
45. Which keywords are used in exception handling? - try, catch, finally, throw, throws
46. `10 / 0` causes which exception? - ArithmeticException
47. Accessing invalid array index causes what? - ArrayIndexOutOfBoundsException
48. Calling method on null causes what? - NullPointerException
49. What is garbage collection? - Reclaiming memory from unreachable objects
50. Which method suggests garbage collection? - System.gc()

### Java Strings, Arrays, Operators, Loops
51. Are Java strings mutable or immutable? - Immutable
52. Which method gives string length? - length()
53. Which method gets character at index? - charAt()
54. Which method compares string content? - equals()
55. `==` compares what for objects? - References
56. `"5" + 5` gives what? - 55
57. `"Java".replace('J','P')` gives what? - Pava
58. Which class is best for mutable string operations? - StringBuilder
59. Array index starts from what? - 0
60. Last index of array is what? - length - 1
61. Accessing `arr[arr.length]` causes what? - ArrayIndexOutOfBoundsException
62. `int[] arr = {1,2,3}; arr.length` is what? - 3
63. Operator precedence: multiplication or addition first? - Multiplication
64. `10 + 5 * 20` equals what? - 110
65. `if (a == 2)` checks what? - Equality
66. `if (a = 2)` is valid for int in Java? - No
67. Loop `for(int i=0;i<=100;i+=5)` runs how many times? - 21
68. What does continue do? - Skips current iteration and moves to next
69. What does break do? - Exits loop/switch
70. `while(x > 0)` with x increasing from 1 is what? - Infinite loop
71. Enhanced for loop is used for what? - Iterating arrays/collections
72. Default value of int instance variable? - 0
73. Default value of boolean instance variable? - false
74. Default value of object reference? - null
75. Local variables have default values? - No

### Collections, Generics, Threads
76. Root interface of collection hierarchy? - Collection
77. Which collection stores key-value pairs? - Map
78. Which class stores key-value pairs without sorted order? - HashMap
79. Which map maintains insertion order? - LinkedHashMap
80. Which map sorts by natural ordering of keys? - TreeMap
81. Which collection stores unique values? - Set
82. Which set usually has no order guarantee? - HashSet
83. Which collection allows duplicates and index access? - ArrayList
84. Which collection follows LIFO? - Stack
85. Which collection follows FIFO? - Queue
86. Stack insertion operation is called? - push
87. Stack deletion operation is called? - pop
88. Stack top read operation is called? - peek
89. Queue insertion operation is called? - enqueue/offer
90. Queue deletion operation is called? - dequeue/poll
91. Empty stack pop/peek causes what? - Invalid operation/exception
92. Can linked list implement stack? - Yes
93. Can linked list implement queue? - Yes
94. What is generic type erasure? - Generic type info removed at runtime
95. What is type inference? - Compiler infers generic type automatically
96. What is functional interface? - Interface with exactly one abstract method
97. Lambda captured local variables must be what? - final or effectively final
98. Which stream operation is terminal: collect or map? - collect
99. Purpose of Optional? - Handle possible null values safely
100. Structural modification during fail-fast iteration causes what? - ConcurrentModificationException
101. What is thread pool advantage? - Reuses existing threads and improves performance
102. Deadlock happens when? - Threads wait on locks held by each other
103. synchronized keyword is used for what? - Thread-safe access/locking
104. Local variables are stored where? - Stack memory
105. Objects are stored where? - Heap memory

### DSA and Complexity
106. O(1) means what? - Constant time
107. O(n) means what? - Linear time
108. O(n^2) usually comes from what? - Nested loops
109. O(log n) usually comes from what? - Halving/doubling each step
110. Binary search best case complexity? - O(1)
111. Binary search average/worst complexity? - O(log n)
112. Sorting generally takes what time? - O(n log n)
113. Two nested loops n and m give what? - O(nm)
114. Outer n with inner m and inner k sequentially gives what? - O(nm + nk)
115. Loop `i = i * 2` until n gives what? - O(log n)
116. Loop `j*j <= n` gives what? - O(sqrt(n))
117. First block n sqrt(m), second block m sqrt(n) gives what? - O(n√m + m√n)
118. Huffman tree building complexity? - O(n log n)
119. Linear search complexity? - O(n)
120. HashMap average search complexity? - O(1)
121. HashSet average contains complexity? - O(1)
122. Stack push/pop complexity? - O(1)
123. Queue enqueue/dequeue complexity? - O(1)
124. Array random access complexity? - O(1)
125. Linked list random access complexity? - O(n)
126. Linked list insertion at head complexity? - O(1)
127. Maximum subarray problem uses which algorithm? - Kadane's algorithm
128. Kadane's algorithm complexity? - O(n)
129. Two sum optimized uses what? - HashMap/HashSet
130. Two sum optimized complexity? - O(n)
131. Pair sum in sorted array uses what? - Two pointers
132. Palindrome check uses what? - Two pointers
133. Longest substring without repeating uses what? - Sliding window + HashSet
134. Fixed-size subarray max sum uses what? - Sliding window
135. Move zeroes to end uses what? - Two pointer/index pointer
136. Rotate array optimized uses what? - Reverse method
137. Count frequency uses what? - HashMap or frequency array
138. Anagram lowercase optimized uses what? - Frequency array
139. General anagram uses what? - HashMap
140. First non-repeating character uses what? - Frequency map/array
141. Remove duplicates uses what? - HashSet
142. Reverse string uses what? - Two pointers/StringBuilder
143. Check subsequence uses what? - Two pointers
144. Merge sorted arrays uses what? - Two pointers
145. Greedy means what? - Choose locally best option at each step
146. DP means what? - Store answers to overlapping subproblems
147. Climbing stairs recurrence? - dp[i] = dp[i-1] + dp[i-2]
148. 0/1 knapsack uses which technique? - Dynamic Programming
149. First Fit Decreasing bin packing first step? - Sort items descending
150. Group consecutive cards uses what? - Sort + HashMap frequency

### DBMS and SQL MCQs
151. DBMS stands for what? - Database Management System
152. Table stores data in what? - Rows and columns
153. Row is also called what? - Record/tuple
154. Column is also called what? - Attribute/field
155. Primary key property? - Unique and not null
156. Foreign key is used for what? - Refers to primary key of another table
157. Candidate key means what? - Possible unique identifier
158. Super key means what? - Any set of attributes uniquely identifying row
159. Unique key can allow null? - Yes, depending on DBMS
160. Primary key can allow null? - No
161. Normalization reduces what? - Redundancy/duplication
162. 1NF removes what? - Repeating groups/non-atomic values
163. 2NF removes what? - Partial dependency
164. 3NF removes what? - Transitive dependency
165. ACID full form? - Atomicity, Consistency, Isolation, Durability
166. Atomicity means what? - All or nothing
167. Consistency means what? - Valid state to valid state
168. Isolation means what? - Transactions do not interfere
169. Durability means what? - Committed data remains saved
170. DDL commands? - CREATE, ALTER, DROP, TRUNCATE
171. DML commands? - INSERT, UPDATE, DELETE
172. DQL command? - SELECT
173. TCL commands? - COMMIT, ROLLBACK, SAVEPOINT
174. DCL commands? - GRANT, REVOKE
175. WHERE filters what? - Rows before grouping
176. HAVING filters what? - Groups after GROUP BY
177. ORDER BY does what? - Sorts result
178. GROUP BY does what? - Groups rows by column values
179. JOIN does what? - Combines rows from tables
180. INNER JOIN returns what? - Matching rows only
181. LEFT JOIN returns what? - All left rows plus matching right rows
182. RIGHT JOIN returns what? - All right rows plus matching left rows
183. FULL OUTER JOIN returns what? - All matching and non-matching rows from both tables
184. CROSS JOIN returns what? - Cartesian product
185. MySQL supports FULL OUTER JOIN directly? - No
186. Subquery means what? - Query inside another query
187. IN operator checks what? - Value exists in a list/subquery result
188. EXISTS checks what? - Whether subquery returns rows
189. DISTINCT removes what? - Duplicate rows
190. MAX returns what? - Maximum value
191. AVG returns what? - Average value
192. COUNT counts what? - Rows/non-null values depending usage
193. EXCEPT does what? - Returns rows from first query not in second
194. UNION does what? - Combines results and removes duplicates
195. UNION ALL does what? - Combines results keeping duplicates
196. Window function for ranking transactions? - ROW_NUMBER()
197. PARTITION BY does what in window functions? - Divides rows into groups
198. ORDER BY inside ROW_NUMBER does what? - Decides numbering order
199. `CASE WHEN` in SQL is used for what? - Conditional logic
200. ROUND(AVG(x),1) returns what? - Average rounded to 1 decimal

### Mock-Pattern Direct Questions
201. Which keyword is used to inherit a class? - extends
202. Which answer best describes polymorphism? - Object can take many forms
203. Which is not valid overloading? - Changing only return type
204. Which is true about abstract classes and interfaces? - Abstract classes can have constructors, interfaces cannot
205. Which modifier allows same package and subclass access? - protected
206. `int d = 10 + 5 * 20` output? - 110
207. Most likely deadlock scenario? - Thread holding one lock and waiting for another held by another thread
208. Primary advantage of thread pool? - Reusing existing threads
209. Java feature omitting generic method type arguments? - Type inference
210. Generic type information at runtime? - Completely erased
211. How are TreeMap elements ordered? - Natural ordering of keys
212. Binary search best case? - O(1)
213. Outer n with inner m and k loops complexity? - O(nm + nk)
214. Linked list efficiently implements what? - Stack and Queue
215. Huffman tree build complexity? - O(n log n)
216. Loss exactly 1/5 of revenue means what equation? - Expenditure - Revenue = Revenue / 5
217. Online orders but never store orders uses which set operation? - Online EXCEPT Store
218. Committed transaction saved after failure is which ACID property? - Durability
219. Join without specific matching column condition? - CROSS JOIN
220. First Fit Decreasing starts by sorting how? - Descending order
221. Consecutive card grouping requires divisibility by what? - hand.length % groupSize == 0
222. SQL customer category filter can use what clause after grouping? - HAVING
223. Third transaction per user uses what function? - ROW_NUMBER()
224. `ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY transaction_date)` gives what? - Chronological transaction rank per user
225. Average cook/pack/delay per item uses what? - GROUP BY Item with AVG

## Must-Practice Coding Problems

1. Count frequency of array elements - HashMap
2. Find duplicates in array - HashSet
3. Two Sum - HashMap
4. Pair sum in sorted array - Two pointers
5. Reverse array/string - Two pointers
6. Move zeroes to end - Two pointers
7. Rotate array by k - Reverse method
8. Second largest element - One pass
9. Maximum subarray sum - Kadane's algorithm
10. Palindrome string - Two pointers
11. Anagram - Frequency array/HashMap
12. First non-repeating character - Frequency map
13. Remove duplicate characters - HashSet
14. Longest substring without repeating - Sliding window + HashSet
15. Maximum sum subarray of size k - Fixed sliding window
16. Minimum size subarray sum - Variable sliding window
17. Valid parentheses - Stack
18. Next greater element - Stack
19. Queue operation tracing - Queue
20. Reverse linked list - Iterative pointers
21. Merge two sorted linked lists - Two pointers
22. Climbing stairs - DP
23. Coin change basics - DP
24. First Fit Decreasing bin packing - Greedy + sorting
25. Group consecutive cards - Sorting + HashMap

## Must-Know SQL Query Templates

### 1. Employee with department name
```sql
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```

### 2. All employees even without department
```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
```

### 3. Salary above average
```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### 4. Second highest salary
```sql
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

### 5. Count employees department-wise including zero
```sql
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;
```

### 6. Customers who bought Electronics but not Clothing/Footwear
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

### 7. Average values per item
```sql
SELECT Item,
       ROUND(AVG(Cook_time), 1) AS Average_cook,
       ROUND(AVG(Pack_time), 1) AS Average_pack,
       ROUND(AVG(Delay_time), 1) AS Average_delay
FROM Orders
GROUP BY Item;
```

### 8. Third transaction per user
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

### 9. Online-only customers using EXCEPT
```sql
SELECT customer_id
FROM orders
WHERE order_type = 'Online'
EXCEPT
SELECT customer_id
FROM orders
WHERE order_type = 'Store';
```

### 10. Highest paid job titles
```sql
SELECT DISTINCT worker_title
FROM title
WHERE worker_ref_id IN (
    SELECT worker_id
    FROM worker
    WHERE salary = (SELECT MAX(salary) FROM worker)
)
ORDER BY worker_title;
```

## Final Night Priority

1. Memorize MCQs 1-225.
2. Revise SQL templates 1-10.
3. Code only these: Two Sum, longest substring, valid parentheses, Kadane, rotate array, move zeroes, group consecutive cards.
4. Sleep enough. Tomorrow morning, revise formulas and templates only.
