CREATE DATABASE startersql;
-- we creating a Database called as startersql

USE startersql;
-- now we are commmanding to use starersql as my Database

CREATE TABLE user (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE NOT NULL,
    GENDER ENUM('MALE','FEMALE','OTHER')
)
-- we have created a table called as 'user' and created some column with name and datatye just succeding it

SELECT * FROM user;
SELECT ID,NAME FROM user;
-- above two lines commands to display selcted row or rows

RENAME TABLE user TO coders;
-- this command to change the name of current table