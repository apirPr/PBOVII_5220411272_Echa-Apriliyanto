USE `5220411272`;

CREATE TABLE
    perangkat_audio (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        merek VARCHAR(255) NOT NULL,
        harga INTEGER NOT NULL,
        jack_audio VARCHAR(255),
        wireless BOOLEAN
    );

CREATE TABLE
    in_ear_monitor (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        merek VARCHAR(255) NOT NULL,
        harga INTEGER NOT NULL,
        jack_audio VARCHAR(255),
        wireless BOOLEAN,
        driver VARCHAR(255),
        detachable BOOLEAN
    );

CREATE TABLE
    headphone (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        merek VARCHAR(255) NOT NULL,
        harga INTEGER NOT NULL,
        jack_audio VARCHAR(255),
        wireless BOOLEAN,
        jenis VARCHAR(255)
    );