USE startersql;

-- ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE(email);
-- When we want to add some contraints to the Variable we use this the ADD CONSTRAINTS
-- Also we can name the CONSTRAINT like we have given the name unique_email
-- ALTER TABLE users ADD CONSTRAINT "Constraint-Name" UNIQUE("Column-Name")

-- ALTER TABLE users MODIFY COLUMN name VARCHAR(100) NULL;
-- Here we have made the Column name to NULL from NOT NULL 

ALTER TABLE users ADD CONSTRAINT chk_dob CHECK (date_of_birth>'1920-01-01');
SELECT * FROM users;