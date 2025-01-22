USE first_database;

CREATE TABLE IF NOT EXISTS books (
    id int NOT NULL AUTO_INCREMENT, 
    name varchar(255),
    PRIMARY KEY(id)
);

INSERT INTO books(name) VALUES('The hobbit');
INSERT INTO books(name) VALUES('Lord of the rings');
