USE startersql;

-- SELECT * FROM users;
-- SELECT * FROM address;

-- INNER JOIN :
-- In this Join we get only those entries which are common in both and others are eliminated
SELECT address.id AS address_id ,users.name, address.street,address.city,address.state 
FROM users INNER JOIN address ON users.id= address.user_id;

-- LEFT JOIN :
-- In LEFT JOIN the table written after the word FROM is givne more IMPORTANCE
-- And all the row of that TABLE is display regardless of the fact if they are matched or not
-- If the matched is not MATCHED the data from the remeining table is considerd as NULL
SELECT address.id AS address_id ,users.name, address.street,address.city,address.state 
FROM users LEFT JOIN address ON users.id= address.user_id; 

-- RIGHT JOIN :
-- In RIGHT JOIN the table written after the word FROM is givne more IMPORTANCE
-- And all the row of that TABLE is display regardless of the fact if they are matched or not
-- If the matched is not MATCHED the data from the remeining table is considerd as NULL
SELECT address.id AS address_id ,users.name, address.street,address.city,address.state 
FROM address RIGHT JOIN users ON users.id= address.user_id;  

