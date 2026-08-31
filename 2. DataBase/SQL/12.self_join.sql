USE startersql;

ALTER TABLE users ADD COLUMN refered_by_id INT;

UPDATE users SET refered_by_id = 1 WHERE id IN(2,6,8,10,12,13);
UPDATE users SET refered_by_id = 2 WHERE id IN(7,13,15,19);

SELECT 
a.id,
a.name AS USER_NAME,
b.name AS REFERED_NAME

FROM users a INNER JOIN users b ON a.refered_by_id=b.id;
SELECT * FROM users;