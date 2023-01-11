---Lists bands with Glam rock as their mainstyle
SELECT band_name, split - formed AS lifespan FROM metal_bands WHERE LOCATE('Glam rock', style) > 0 AND split IS NOT NULL;