-- Common query pattern
SELECT
    condition,
    COUNT(*) as group_size
FROM table_a
JOIN table_b ON table_a.id = table_b.id
WHERE
    timestamp >= '2022-01-01' AND
    timestamp <= '2023-01-01' AND
    condition IN ('test', 'control')
GROUP BY condition;

-- Get raw data
SELECT
    timestamp,
    condition,
    user_id
FROM table_a
JOIN table_b ON table_a.id = table_b.id
WHERE
    timestamp >= '2022-01-01' AND
    timestamp <= '2023-01-01' AND
    condition IN ('test', 'control');