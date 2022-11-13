-- Question 8 xiangtia
SELECT DISTINCT(S.Year),quatity
FROM StreamedMovies S
LEFT JOIN
(SELECT Year,COUNT(Title) quatity
FROM
(SELECT Year, S.Title,Genre
FROM StreamedMovies S
LEFT JOIN MovieData M
ON S.Title = M.Title
WHERE M.Genre LIKE '%Drama%' AND PrimeVideo = 1)
GROUP BY Year) Movies
ON S.Year = Movies.Year
ORDER BY S.Year