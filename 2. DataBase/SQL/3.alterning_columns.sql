USE startersql;

ALTER TABLE user ADD COLUMN ACTIVITY BOOLEAN DEFAULT True;
-- If we want to insert new Column in the Dataset
-- ALTER TABLE user ADD COLUMN 'column-name' 'data-type' 'contraints'

ALTER TABLE user DROP COLUMN ACTIVITY;
-- If we want to delete a Column from Dataset
-- ALTER TABLE user DROP COLUMN 'column-name'

ALTER TABLE user MODIFY COLUMN NAME VARCHAR(150);
-- If we want to Modify the Column Datatype
-- ALTER TABLE user DROP COLUMN 'column-name' 'new-datatype'

ALTER TABLE user MODIFY COLUMN EMAIL VARCHAR(100) AFTER ID;
-- When want to change order of the Column
-- ALTER TABLE user MODIFY COLUMN 'column-name' 'datatype' AFTER 'after-which-column'

ALTER TABLE user MODIFY COLUMN NAME VARCHAR(150) FIRST;
SELECT * FROM user;