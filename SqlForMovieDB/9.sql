-- Question 9 xiangtia
SELECT 'Netflix' Platform,S.Title, MAX(M.Revenue) Revenue
FROM StreamedMovies S, MovieData M
WHERE S.Title = M.Title AND
Netflix = 1
UNION
SELECT 'Hulu' Platform,S.Title, MAX(M.Revenue) Revenue
FROM StreamedMovies S, MovieData M
WHERE S.Title = M.Title AND
Hulu = 1
UNION
SELECT 'PrimeVideo' Platform,S.Title, MAX(M.Revenue) Revenue
FROM StreamedMovies S, MovieData M
WHERE S.Title = M.Title AND
PrimeVideo = 1
UNION
SELECT 'Disney' Platform,S.Title, MAX(M.Revenue) Revenue
FROM StreamedMovies S, MovieData M
WHERE S.Title = M.Title AND
Disney = 1
