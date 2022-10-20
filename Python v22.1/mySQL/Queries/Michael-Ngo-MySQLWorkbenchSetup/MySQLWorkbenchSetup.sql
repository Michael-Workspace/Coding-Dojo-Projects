SELECT * 
FROM names;

INSERT INTO `names`.`names` (`name`) VALUES ('Michael Ngo');

INSERT INTO `names`.`names` (`name`) 
VALUES 
	('Alexis Miller'),
    ('Tana Inzar'),
    ('Bilal Azil');

DELETE FROM `names`.`names` WHERE (`id` = '19');
