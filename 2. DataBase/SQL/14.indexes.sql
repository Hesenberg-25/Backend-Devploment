USE startersql;

-- INDEXES help us to retrive data from the TABLE 
-- like when we use " SELECT * FROM users WHERE email='aarav@aarav.com' " here the email is a INDEX we are using
-- They are the anchors which are are used to Retrive data from the Database much faster mainly for searches,filters and joins

CREATE INDEX idx_gender ON users(gender);
-- CREATE INDEX {index-name} ON {table-name(column-name)}; 

-- INDEXES consume space in Disk
-- They slow down the operation like INSERT ,UPDATE AND DELETE and mainly used on WHERE ,ORDER BY AND JOIN

CREATE INDEX idx_name_salary ON users(name,salary);  
-- CREATE INDEX {index-name} ON {table-name(column-name-1,column-name-2)};
-- It good to practise to write the WHERE statment in logic to get FASTER response 

DROP INDEX idx_gender ON users;
-- DROP INDEX {index-name} ON {Table-name}; 

SHOW INDEXES FROM users;