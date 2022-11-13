-- Question 6 xiangtia
SELECT (M.Director)
FROM MovieData M, StreamedMovies S
WHERE M.Title = S.Title AND
S.Disney = 1
GROUP BY M.Director
HAVING COUNT(M.Director) >=2 
