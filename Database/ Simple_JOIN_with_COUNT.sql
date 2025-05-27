SELECT p.id, p.name, COUNT(t.id) AS toy_count
FROM people p
LEFT JOIN toys t ON p.id = t.people_id
GROUP BY p.id, p.name;