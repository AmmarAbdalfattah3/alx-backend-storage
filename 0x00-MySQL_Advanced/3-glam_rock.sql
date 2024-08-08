-- Assuming the metal_bands table already exists and contains the necessary columns

-- Query to list Glam Rock bands with their lifespan, sorted by longevity
SELECT
    band_name,
    COALESCE(split, 2022) - formed AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
