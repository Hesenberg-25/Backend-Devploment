USE startersql;

-- Always try to use WHERE keyword when you are using UPDATE

UPDATE users SET salary = '45000' ,email='aarav@aarav.com' WHERE id='1';

UPDATE users SET salary = '70000' WHERE id='5';

UPDATE users SET name='Aisha Khan' WHERE email='aisha@example.com';

UPDATE users SET salary=salary+10000 WHERE salary<60000;

SELECT * FROM users;