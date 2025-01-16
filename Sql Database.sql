-- Create the database
CREATE DATABASE shipping_db;

-- Use the created database
USE shipping_db;

-- Create Users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    country VARCHAR(255) NOT NULL
);

-- Create Countries table
CREATE TABLE countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(255) UNIQUE NOT NULL,
    max_size FLOAT NOT NULL,
    max_weight FLOAT NOT NULL,
    custom_duty_tax FLOAT NOT NULL,
    banned_items TEXT
);

-- Create Orders table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    parcel_size FLOAT NOT NULL,
    parcel_weight FLOAT NOT NULL,
    destination_country_id INT,
    shipping_charge FLOAT NOT NULL,
    order_status VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (destination_country_id) REFERENCES countries(country_id)
);
