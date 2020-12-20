-- Database
DROP DATABASE IF EXISTS dev;
CREATE DATABASE dev;

-- User
CREATE USER test WITH PASSWORD 'us3rt3st*';
GRANT ALL PRIVILEGES ON DATABASE "dev" to test;

-- Schema
CREATE SCHEMA clothes;

-- Tables
CREATE TABLE clothes."clothes" (
  "id" bigint PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "description" varchar(1000),
  "reference" varchar(100),
  "price" decimal NOT NULL,
  "old_price" decimal,
  "discount" integer,
  "url" varchar NOT NULL,
  "image" varchar NOT NULL,
  "store_id" bigint NOT NULL,
  "subcategory_id" bigint NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."colors" (
  "id" bigint PRIMARY KEY,
  "name" varchar(30)
);

CREATE TABLE clothes."sizes" (
  "id" bigint PRIMARY KEY,
  "name" varchar(10)
);

CREATE TABLE clothes."categories" (
  "id" bigint PRIMARY KEY,
  "name" varchar(55)
);

CREATE TABLE clothes."subcategories" (
  "id" bigint PRIMARY KEY,
  "name" varchar(55),
  "category_id" bigint
);

CREATE TABLE clothes."stores" (
  "id" bigint PRIMARY KEY,
  "name" varchar(50),
  "country_id" bigint,
  "created_at" timestamp NOT NULL
);

CREATE TABLE clothes."clothes_colors_sizes_map" (
  "clothe_id" bigint,
  "color_id" bigint,
  "size_id" bigint,
  "created_at" timestamp NOT NULL
  PRIMARY KEY ("clothe_id", "color_id", "size_id")
);

CREATE TABLE clothes."countries" (
  "id" bigint PRIMARY KEY,
  "name" varchar(55),
  "continent" varchar(20),
  "code" varchar(3),
  "currency" varchar(5),
  "created_at" timestamp NOT NULL
);

ALTER TABLE clothes."stores" ADD FOREIGN KEY ("country_id") REFERENCES clothes."countries" ("id");

ALTER TABLE clothes."clothes" ADD FOREIGN KEY ("store_id") REFERENCES clothes."stores" ("id");

ALTER TABLE clothes."subcategories" ADD FOREIGN KEY ("category_id") REFERENCES clothes."categories" ("id");

ALTER TABLE clothes."clothes_colors_sizes_map" ADD FOREIGN KEY ("size_id") REFERENCES clothes."sizes" ("id");

ALTER TABLE clothes."clothes_colors_sizes_map" ADD FOREIGN KEY ("color_id") REFERENCES clothes."colors" ("id");

ALTER TABLE clothes."clothes_colors_sizes_map" ADD FOREIGN KEY ("clothe_id") REFERENCES clothes."clothes" ("id");

ALTER TABLE clothes."clothes" ADD FOREIGN KEY ("subcategory_id") REFERENCES clothes."subcategories" ("id");

