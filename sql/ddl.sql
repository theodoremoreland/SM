CREATE DATABASE IF NOT EXISTS `ecommerce`
    DEFAULT CHARACTER SET utf8 
    COLLATE utf8_general_ci
;

USE `ecommerce`;

-- Not sure if this needs a lookup table, depends on whether brands are 1-to-1 with products.
CREATE TABLE Brand (
    brand_id INT NOT NULL AUTO_INCREMENT,
    brand_name VARCHAR(100) NOT NULL,
    PRIMARY KEY (brand_id),
    UNIQUE (brand_name)
);

CREATE TABLE Category (
    category_id INT NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    category_description VARCHAR(2000),
    PRIMARY KEY (category_id),
    UNIQUE (category_name, category_description)
); 

CREATE TABLE Product (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    sku VARCHAR(50) NOT NULL,
    product_description VARCHAR(2000) NOT NULL,
    brand_id INT,
    PRIMARY KEY (product_id),
    FOREIGN KEY (brand_id) REFERENCES Brand(brand_id),
    UNIQUE (sku)
);

-- Lookup table for categories and subcategories of product (e.g. PVC Valves, Metal Valves, Flexible PVC Pipe etc.).
CREATE TABLE Product_Category (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    is_subcategory BOOLEAN NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (category_id) REFERENCES Category(category_id)
);

-- Can be used to store product attributes such as Pump Type, Size, Tubing Type etc.
CREATE TABLE Attribute (
    attribute_id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL,
    attribute_key VARCHAR(255), -- e.g. Pump Type, Size, etc.
    attribute_value VARCHAR(255), -- e.g. Ball Valve, 1/2 inch, etc.
    PRIMARY KEY (attribute_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Can be used to store references to images, videos, documents, etc (would not store the actual media).
CREATE TABLE Media (
    media_id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL,
    source VARCHAR(255) NOT NULL, -- e.g. url, file path, etc.
    source_type VARCHAR(50), -- e.g. url, file system, stream, etc.
    media_type VARCHAR(50), -- e.g. image, video, document, etc.
    PRIMARY KEY (media_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    UNIQUE (source)
);

CREATE TABLE Inventory (
    inventory_id INT NOT NULL AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (inventory_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);