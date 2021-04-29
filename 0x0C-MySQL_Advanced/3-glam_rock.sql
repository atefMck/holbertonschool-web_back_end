-- dummy comment dummy comment dummy comment
-- dummy comment dummy comment dummy comment
CREATE DATABASE IF NOT EXISTS holberton;
-- all bands with Glam rock 
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
