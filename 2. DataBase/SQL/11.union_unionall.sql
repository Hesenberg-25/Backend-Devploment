USE startersql;

-- UNION is used when we want to Display both of the content from the table and do not want duplicate
SELECT name AS NAME , email AS EMAIL FROM users 
UNION 
SELECT name AS NAME , email AS EMAIL FROM admin_users;

-- UNION ALL is used when it works even if we have Duplicates in the Required Data

-- We can also add new Column in the Display TABLE

SELECT name AS NAME,email AS EMAIL ,'USER' AS ROLE FROM users
UNION ALL
SELECT name AS NAME, email AS EMAIL ,'ADMIN' AS ROLE FROM admin_users;