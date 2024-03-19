-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS pims_dev_db;
CREATE USER IF NOT EXISTS 'pims_dev'@'localhost' IDENTIFIED BY 'pims_dev_pwd';
GRANT ALL PRIVILEGES ON `pims_dev_db`.* TO 'pims_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pims_dev'@'localhost';
FLUSH PRIVILEGES;