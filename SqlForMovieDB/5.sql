-- Question 5 xiangita
SELECT COUNT(S.Title) netflixDrama
FROM StreamedMovies S, MovieData M
WHERE M.Title = S.Title AND
S.Netflix = 1 AND
(S.PrimeVideo + S.Hulu + S.Disney = 0) AND
M.Genre LIKE '%Drama%'