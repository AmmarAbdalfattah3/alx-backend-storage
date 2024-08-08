SELECT band_name, 
       CASE 
           WHEN split IS NULL THEN 2022 - formed  -- Calculate lifespan for active bands
           ELSE split - formed  -- Calculate lifespan for bands that have split
       END AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'  -- Filter by Glam rock as the main style
ORDER BY lifespan DESC;  -- Order by lifespan in descending order
