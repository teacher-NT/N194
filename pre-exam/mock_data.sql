CREATE DATABASE store_db;
USE store_db;


CREATE TABLE products (
	id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
	category VARCHAR(30) NOT NULL,
    price DECIMAL(10,2) NOT NULL ,
    quantity INT NOT NULL,
    manufacturer VARCHAR(50) NOT NULL
);



INSERT INTO products (`name`, category, price, quantity, manufacturer)
VALUES
('Banan', 'Meva', 23000, 150, 'Bananjon'),
('Sut', 'Oziq-ovqat', 10000, 50, 'Sutlik MCHJ'),
('Kolbasa', "Go'sht-mahsulotlari", 60000, 120, 'Tim'),
('Kampot', 'Ichimlik', 12000, 90, 'Bliss'),
('Qazi', "Go'sht-mahsulotlari", 180000, 30, 'Qoratosh'),
('Yogurt', 'Oziq-ovqat', 12000, 230, 'Musaffo'),
('Pishloq', 'Oziq-ovqat', 105000, 40, 'Matsarella'),
('Olma', 'Meva', 17000, 180, 'Qibray fruits MCHJ'),
('Suv', 'Ichimlik', 5000, 400, 'Hydrolife'),
('Kakos', 'Meva', 120000, 20, 'Palma');


-- Query 1
select * from products
order by price desc;

-- Query 2
select * from products
where quantity < 50;

-- Query 3
select * from products
where price > 100000;

-- Query 4
select category, sum(quantity) from products
group by category;