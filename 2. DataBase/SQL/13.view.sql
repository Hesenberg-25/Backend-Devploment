USE startersql;

-- VIEW is a Virtual Table which is used we perfrom complex QUERY in SQL and is needed to be performed MULTIPLE TIMES
-- VIEW gives us live feedback when we Create some change in the PARENT TABLE

CREATE VIEW rich_users AS
SELECT * FROM users WHERE salary > 70000;

-- CREATE VIEW (table-name) AS
-- (condition)

SELECT * FROM rich_users;

DROP VIEW rich_users;