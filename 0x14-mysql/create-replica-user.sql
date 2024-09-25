-- Create replica_user with replication permissions
CREATE USER IF NOT EXISTS 'replica_user'@'%'IDENTIFIED BY 'projectcorrection280hbtn';
GRANT  REPLICATION SLAVE, REPLICATION CLIENT  ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;

-- Grant SELECT permissions to holberton_user on mysql.user
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

SELECT user, host FROM mysql.user WHERE user = 'replica_user';
