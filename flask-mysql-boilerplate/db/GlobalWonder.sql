-- Show Database
SHOW DATABASES;

-- Create database
CREATE DATABASE Globalwonder;
USE Globalwonder;

CREATE TABLE IF NOT EXISTS airlines (
    airline_id INTEGER,
    name VARCHAR(50) NOT NULL ,
    num_accidents INTEGER NOT NULL ,
    rating DOUBLE,
    PRIMARY KEY (airline_id)
);

CREATE TABLE IF NOT EXISTS airports(
    code VARCHAR(3),
    city VARCHAR(50),
    primary key (code)
);


CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER,
    first_name VARCHAR(100),
    last_name VARCHAR(150),
    date_of_birth DATE,
    primary key (customer_id)
);


CREATE TABLE IF NOT EXISTS hotels(
    street_num INTEGER,
    street varchar(50),
    name varchar(50),
    ranking double,
    primary key (street_num, street, name)
);

ALTER TABLE hotels ADD INDEX street_num_index (street_num);
ALTER TABLE hotels ADD INDEX street_index (street);
ALTER TABLE hotels ADD INDEX name_index (name);



CREATE TABLE IF NOT EXISTS rent_car_company(
    company_name VARCHAR(50),
    rating DOUBLE,
    PRIMARY KEY (company_name)
);


CREATE TABLE IF NOT EXISTS attractions(
    attraction_id INTEGER,
    type VARCHAR(50),
    description TEXT,
    kid_friendly BOOLEAN NOT NULL,
    needs_booking BOOLEAN NOT NULL,
    price DOUBLE NOT NULL,
    primary key (attraction_id)
);


CREATE TABLE IF NOT EXISTS flights(
   flight_id INTEGER,
   price DOUBLE NOT NULL ,
   departure_time TIME,
   arrival_time TIME,
   layover BOOLEAN,
   class VARCHAR(10),
   airline_id INTEGER,
   departure_airport VARCHAR(3),
   arrive_airport VARCHAR(3),
   primary key (flight_id),
   foreign key (airline_id) references airlines(airline_id) ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (departure_airport) references airports(code) ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (arrive_airport) references airports(code) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS book_flights(
   flight_id INTEGER,
   customer_id INTEGER,
   primary key (flight_id,customer_id),
   foreign key (flight_id)  references flights(flight_id) ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (customer_id) references customers(customer_id)  ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS book_hotels(
   street_num INTEGER,
   street varchar(50),
   name varchar(50),
   customer_id INTEGER,
   primary key (street_num,street,name,customer_id),
   foreign key (street_num) references hotels(street_num)  ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (street) references hotels(street)  ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (name) references hotels(name)  ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (customer_id) references customers(customer_id)  ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS flight_menu(
   flight_id INTEGER,
   drinks VARCHAR(100),
   dessert VARCHAR(100),
   main_course VARCHAR(100),
   primary key (flight_id, drinks, dessert, main_course) ,
   foreign key (flight_id) references flights(flight_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS airport_lounges(
   code VARCHAR(3),
   lounge_type VARCHAR(15),
   primary key (code, lounge_type),
   foreign key (code) references airports(code)  ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS customer_phones(
   phone_num VARCHAR(20),
   customer_id INTEGER,
   primary key (phone_num),
   foreign key (customer_id) references customers(customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS customer_emails(
   email_address VARCHAR(100),
   customer_id INTEGER,
   primary key (email_address),
   foreign key (customer_id) references customers(customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS rooms(
    street_num INTEGER,
    street varchar(50),
    name varchar(50),
    room_num INTEGER,
    price INTEGER,
    type VARCHAR(30),
    availability BOOLEAN,
    capacity INTEGER,
    primary key (street_num,street,name,room_num),
    foreign key (street_num) references hotels(street_num)  ON DELETE CASCADE ON UPDATE CASCADE,
    foreign key (street) references hotels(street) ON DELETE CASCADE ON UPDATE CASCADE,
    foreign key (name) references hotels(name) ON DELETE CASCADE ON UPDATE CASCADE
);


    CREATE TABLE IF NOT EXISTS cars(
       company_name VARCHAR(50),
       license_plate VARCHAR(15),
       model VARCHAR(50),
       available BOOLEAN,
       capacity INTEGER,
       primary key (company_name, license_plate),
       foreign key (company_name) references rent_car_company(company_name)
    );


CREATE TABLE IF NOT EXISTS attractionHotel(
   street_num INTEGER,
   street varchar(50),
   name varchar(50),
   attraction_id INTEGER,
   primary key (street_num, street, name, attraction_id),
   foreign key (street_num) references hotels(street_num) ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (street) references hotels(street) ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (name) references hotels(name) ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (attraction_id) references attractions(attraction_id)  ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS rent_car(
   company_name VARCHAR(50),
   customer_id INTEGER,
   primary key (company_name, customer_id),
   foreign key (company_name) references rent_car_company(company_name) ON DELETE CASCADE ON UPDATE CASCADE,
   foreign key (customer_id) references customers(customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);
