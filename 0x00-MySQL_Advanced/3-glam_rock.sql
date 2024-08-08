-- Create a temporary table to store the imported data
CREATE TEMPORARY TABLE metal_bands (
    band_name VARCHAR(255),
    style VARCHAR(255),
    formed INT,
    split INT
);

-- Import the data from the provided metal_bands.sql file
-- Example command (depends on your database and its tools):
-- SOURCE /path/to/metal_bands.sql;

-- Query to list Glam Rock bands with calculated lifespan
SELECT
    band_name,
    (CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
