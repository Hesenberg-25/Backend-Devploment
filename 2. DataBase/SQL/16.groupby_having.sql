USE startersql;

SELECT gender AS GENDER, AVG(salary) AS AVG_SALARY, COUNT(*) AS TOTAL FROM users 
GROUP BY gender;
-- GROUP BY is used when we want to group the data in various parameters
-- Like here we have grouped the Data based on Gender so the Display shows us the segregation based on Gender

SELECT gender AS GENDER, AVG(salary) AS AVG_SALARY, COUNT(*) AS TOTAL FROM users 
GROUP BY gender
HAVING AVG_SALARY > 68000;

-- HAVING is used in same way as we use WHERE only the thing is we can't use WHERE after using GROUP BY so we use HAVING ot get same result
-- So in above Query what have we perfromed :
-- 1. Selected GENDER and found out Averge Salary 
-- 2. And grouped them based on GENDER like which gender had how much AVERAGE
-- 3. Then Displayed on that Group whcich was having AVERAGE salary greater than 68000  
