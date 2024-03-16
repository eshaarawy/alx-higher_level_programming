-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS genre,
    COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_shows
ON tv_show_genres.id = tv_genres.genre_id
GROUB BY tv_show_genres.name
ORDER BY number_of_shows DESC;
