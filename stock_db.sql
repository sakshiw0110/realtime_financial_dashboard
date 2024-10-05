CREATE DATABASE stock_db;
USE stock_db;
CREATE TABLE stock_prices (
    Date DATETIME,
    Open DECIMAL(10, 2),
    High DECIMAL(10, 2),
    Low DECIMAL(10, 2),
    Close DECIMAL(10, 2),
    Volume BIGINT,
    SMA_10 DECIMAL(10, 2)
);
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
SHOW GRANTS FOR 'root'@'localhost';
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Sakshiw@01';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';
CREATE USER 'root'@'localhost' IDENTIFIED BY 'Sakshiw@01';
DESCRIBE stock_prices;
DROP TABLE IF EXISTS stock_prices;
SELECT * FROM stock_prices LIMIT 5;






