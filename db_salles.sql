CREATE DATABASE IF NOT EXISTS db_salles;

CREATE USER IF NOT EXISTS 'user_python'@'localhost' IDENTIFIED BY 'Python2026';

GRANT ALL PRIVILEGES ON *.* TO 'user_python'@'localhost';

FLUSH PRIVILEGES;

USE db_salles;

CREATE TABLE IF NOT EXISTS salle (
    code VARCHAR(5) PRIMARY KEY,
    libelle VARCHAR(50),
    type VARCHAR(50),
    capacite INT
);