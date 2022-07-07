CREATE DATABASE YoutubeVideoConverter;
USE YoutubeVideoConverter;

CREATE TABLE Midia(
idMidia INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(250) NOT NULL,
arquivo LONGBLOB NOT NULL
)ENGINE = InnoDB;

select * from Midia;