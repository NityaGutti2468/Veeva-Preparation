SELECT EmpId, Salary, DepartmentId
FROM (
    SELECT EmpId,
           Salary,
           DepartmentId,
           DENSE_RANK() OVER (
               PARTITION BY DepartmentId
               ORDER BY Salary DESC
           ) AS rnk
    FROM Employee
) t
WHERE rnk = 3;
