USE startersql;

-- SELECT * FROM users;

-- SELECT COUNT(*) FROM users WHERE gender='Male';

-- SELECT MIN(salary) AS min_salary,MAX(salary) AS max_salary FROM users;

-- SELECT SUM(salary) AS total_salary FROM users;

-- SELECT AVG(salary) AS avg_salary FROM users;
-- SELECT gender,AVG(salary) AS avg_salary FROM users GROUP BY gender;

SELECT LOWER(name) AS lower_name, CONCAT(LOWER(name),id,LENGTH(NAME)) AS username, YEAR(date_of_birth) AS birth_year,LENGTH(name) AS name_length FROM users;