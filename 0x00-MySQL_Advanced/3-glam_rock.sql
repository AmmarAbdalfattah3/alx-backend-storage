-- List bands with Glam rock style, ranked by longevity
SELECT
    band_name,
    (2022 - formation_year) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
