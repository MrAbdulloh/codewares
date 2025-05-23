PREPARE generate_factorial(int) AS
WITH RECURSIVE factorials AS (
    SELECT 1 AS n, 1 AS result
    UNION ALL
    SELECT n + 1, (n + 1) * result
    FROM factorials
    WHERE n < $1
)
SELECT n, result
FROM factorials;