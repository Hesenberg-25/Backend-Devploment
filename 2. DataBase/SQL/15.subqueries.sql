USE startersql;

SELECT AVG(salary) FROM users ;
-- Simple Query

SELECT * FROM users WHERE salary > (SELECT AVG(salary) AS AVERAGE_SALARY FROM users);
-- SubQuery " SELECT AVG(salary) FROM users " which seems like a Condition for another Query

SELECT * FROM users WHERE salary > (SELECT AVG(salary) AS AVERAGE_SALARY FROM users WHERE gender='Female');
-- SubQuery " SELECT AVG(salary) FROM users " which seems like a Condition for another Query