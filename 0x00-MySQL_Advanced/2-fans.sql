-- Create a temporary table to aggregate the number of fans by country origin
CREATE TEMPORARY TABLE IF NOT EXISTS tmp_band_fans AS
SELECT origin, SUM(nb_fans) AS nb_fans
FROM bands
GROUP BY origin;

-- Select and order the results by the number of fans
SELECT origin, nb_fans
FROM tmp_band_fans
ORDER BY nb_fans DESC;
