SELECT c.capital
FROM countries c
WHERE (c.continent = 'Africa' OR c.continent = 'Afrika') AND c.country LIKE 'E%'
ORDER BY c.capital
LIMIT 3;