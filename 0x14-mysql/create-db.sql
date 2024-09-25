-- Create db on the master server
CREATE DATABASE IF NOT EXISTS tyrell_corp;

USE tyrell_corp;
-- Create table
CREATE TABLE IF NOT EXISTS nexus6
(
        id INT UNIQUE AUTO_INCREMENT NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id));

-- Insert an entry
INSERT INTO nexus6 (name) VALUES ('Emmastro');

REVOKE REPLICATION CLIENT ON *.* FROM 'holberton_user'@'localhost';
GRANT SELECT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'holberton_user'@'localhost';
