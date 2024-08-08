-- Step 1: Create the table to import data into
CREATE TABLE IF NOT EXISTS metal_bands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    band_name VARCHAR(255) NOT NULL,
    formation_year INT NOT NULL,
    style VARCHAR(255) NOT NULL
);

-- Step 2: Load the data from the metal_bands.sql.zip file

-- Step 3: Compute lifespan and list bands with Glam rock style.
SELECT
    band_name,
    (2022 - formation_year) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
