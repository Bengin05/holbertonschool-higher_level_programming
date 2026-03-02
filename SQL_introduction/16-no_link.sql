-- list scores with no NULL values
SELECT score, name FROM second_table
WHERE score IS NOT NULL AND name IS NOT NULL
ORDER BY score DESC;
