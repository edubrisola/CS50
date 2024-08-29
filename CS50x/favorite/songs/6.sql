SELECT DISTINCT songs.name FROM songs JOIN artists ON artist_ID IN
   (SELECT id FROM artists WHERE name = 'Post Malone');
