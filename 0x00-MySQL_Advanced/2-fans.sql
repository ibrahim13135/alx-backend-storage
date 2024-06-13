-- Write SQL script that ranks country origins of bands
-- Ordered by the number of (non-unique) fans
-- Column must be origin and nb_fans
-- Script can be executed on any database
-- 2-fans.sql

SELECT 
  origin, 
  SUM(*) AS nb_bands
FROM 
  metal_bands
GROUP BY 
  origin
ORDER BY 
  nb_bands DESC;
