SELECT AVG(energy) from songs WHERE name IN
   (SELECT DISTINCT songs.name FROM songs JOIN artists ON artist_ID IN
   (SELECT id FROM artists WHERE name = 'Drake'));
