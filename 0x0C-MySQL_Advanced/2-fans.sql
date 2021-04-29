-- dummy comment dummy comment dummy comment
-- dummy comment dummy comment dummy comment
CREATE DATABASE IF NOT EXISTS holberton;
-- Query fans by origin
SELECT origin, SUM(fans) as nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
