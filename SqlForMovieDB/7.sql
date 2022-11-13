-- Question 7 xiangtia
SELECT M.Title FROM MovieData M
WHERE (SELECT COUNT(1) FROM StreamedMovies S WHERE S.Title = M.Title) = 0 AND
INSTR(M.Actors,M.Director)