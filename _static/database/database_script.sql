CREATE SCHEMA clothes;

-- Tables
CREATE TABLE clothes."clothes" (
  "id" bigint PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "description" varchar(1000),
  "reference" varchar(100) UNIQUE,
  "price" decimal NOT NULL,
  "old_price" decimal,
  "discount" integer,
  "url" varchar NOT NULL,
  "genre" varchar(1),
  "store_id" bigint NOT NULL,
  "subcategory_id" bigint NOT NULL,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."images" (
  "id" bigint PRIMARY KEY,
  "url" varchar(150),
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."colors" (
  "id" bigint PRIMARY KEY,
  "name" varchar(30),
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."sizes" (
  "id" bigint PRIMARY KEY,
  "name" varchar(10),
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."categories" (
  "id" bigint PRIMARY KEY,
  "name" varchar(55),
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."subcategories" (
  "id" bigint PRIMARY KEY,
  "name" varchar(55),
  "category_id" bigint,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."stores" (
  "id" bigint PRIMARY KEY,
  "name" varchar(50),
  "country_id" bigint,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

CREATE TABLE clothes."clothes_colors_sizes_map" (
  "clothe_id" bigint,
  "color_id" bigint,
  "size_id" bigint,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp,
  PRIMARY KEY ("clothe_id", "color_id", "size_id")
);

CREATE TABLE clothes."clothes_images_map" (
  "clothe_id" bigint,
  "image_id" bigint,
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp,
  PRIMARY KEY ("clothe_id", "image_id")
);

CREATE TABLE clothes."countries" (
  "id" bigint PRIMARY KEY,
  "name" varchar(55),
  "continent" varchar(20),
  "code" varchar(3),
  "currency" varchar(5),
  "created_at" timestamp NOT NULL,
  "updated_at" timestamp
);

ALTER TABLE clothes."stores" ADD FOREIGN KEY ("country_id") REFERENCES clothes."countries" ("id");

ALTER TABLE clothes."clothes" ADD FOREIGN KEY ("store_id") REFERENCES clothes."stores" ("id");

ALTER TABLE clothes."subcategories" ADD FOREIGN KEY ("category_id") REFERENCES clothes."categories" ("id");

ALTER TABLE clothes."clothes_colors_sizes_map" ADD FOREIGN KEY ("size_id") REFERENCES clothes."sizes" ("id");

ALTER TABLE clothes."clothes_colors_sizes_map" ADD FOREIGN KEY ("color_id") REFERENCES clothes."colors" ("id");

ALTER TABLE clothes."clothes_colors_sizes_map" ADD FOREIGN KEY ("clothe_id") REFERENCES clothes."clothes" ("id");

ALTER TABLE clothes."clothes_images_map" ADD FOREIGN KEY ("clothe_id") REFERENCES clothes."clothes" ("id");

ALTER TABLE clothes."clothes_images_map" ADD FOREIGN KEY ("image_id") REFERENCES clothes."images" ("id");

ALTER TABLE clothes."clothes" ADD FOREIGN KEY ("subcategory_id") REFERENCES clothes."subcategories" ("id");
