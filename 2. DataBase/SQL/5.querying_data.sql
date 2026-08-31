USE startersql;
SELECT * FROM users;

SELECT name,gender FROM users;

-- WHERE basically gives us thw way by which we could find the rows which can satisfy certain condition

SELECT * FROM users WHERE gender='Female'; 
-- Here we only display those which have Female as there Gender

SELECT * FROM users WHERE salary>='50000.00';

SELECT * FROM users WHERE email IS NULL;

SELECT * FROM users WHERE date_of_birth BETWEEN '1990-09-09'AND'1999-09-09';

SELECT * FROM users WHERE gender in('Male','Female');

SELECT * FROM users WHERE gender='Female' AND salary>'50000';

SELECT * FROM users WHERE gender='Male' OR salary<'60000';

SELECT * FROM users ORDER BY date_of_birth ASC LIMIT 10;