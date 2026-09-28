# Write your MySQL query statement below
SELECT 
    e.employee_id, 
    e.department_id
FROM Employee e
LEFT JOIN (
    SELECT 
        employee_id, 
        COUNT(department_id) AS dept_count
    FROM Employee
    GROUP BY employee_id
) c ON e.employee_id = c.employee_id
WHERE e.primary_flag = 'Y' 
   OR c.dept_count = 1;