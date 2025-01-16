CREATE DATABASE shipping_db;
USE shipping_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    parcel_size FLOAT,
    parcel_weight FLOAT,
    destination_country VARCHAR(255),
    shipping_charge FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
