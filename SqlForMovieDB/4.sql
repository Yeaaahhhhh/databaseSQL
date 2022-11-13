-- Question 4 xiangita
SELECT COUNT(S.Title) numOfMovies
FROM StreamedMovies S
WHERE (S.Netflix + S.PrimeVideo + S.Hulu + S.Disney > 2)
