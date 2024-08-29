SELECT title, rating FROM movies JOIN ratings WHERE
   (id = movie_id AND year = 2010)
   ORDER BY rating DESC, title LIMIT 30;
