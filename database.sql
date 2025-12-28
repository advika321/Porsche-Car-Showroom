-- Porsche Car Showroom Database

CREATE DATABASE IF NOT EXISTS car_showroom;
USE car_showroom;

-- Drop table if it already exists
DROP TABLE IF EXISTS cars;

-- Create cars table
CREATE TABLE cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    engine_in_hp INT,
    topspeed_in_mph INT,
    year_released INT,
    image_path VARCHAR(255)
);

-- Insert Porsche car data
INSERT INTO cars 
(model_name, price, engine_in_hp, topspeed_in_mph, year_released, image_path)
VALUES
('Macan', 78800, 375, 169, 2014, 'images/macan.png'),
('Cayenne', 79200, 541, 177, 2002, 'images/cayenne.png'),
('911', 114400, 572, 191, 1964, 'images/911.png'),
('Taycan', 99400, 750, 161, 2019, 'images/taycan.png'),
('Panamera', 99900, 325, 196, 2009, 'images/panamera.png'),
('718 Boxster', 68300, 350, 170, 2016, 'images/718boxster.png'),
('718 Cayman', 68300, 350, 170, 2016, 'images/718cayman.png'),
('911 Turbo', 230400, 640, 205, 1974, 'images/911turbo.png'),
('911 GT3', 222500, 502, 197, 1999, 'images/911gt3.png'),
('911 Carrera', 114400, 379, 187, 1964, 'images/911carrera.png');
