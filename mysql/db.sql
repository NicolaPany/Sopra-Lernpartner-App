
-- Datenbank Sopra-LernApp

CREATE DATABASE IF NOT EXISTS `Sopra-LernApp` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Sopra-LernApp`;

-- Tabelle erstellen 'Person'
-- -----------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `Person` (
  `person_id` INT NOT NULL ,
  `name` VARCHAR(45) NULL,
  `vorname` VARCHAR(45) NULL,
  `lebensjahre` INT NOT NULL,
  `geschlecht` VARCHAR(45) NULL,
  `lerngruppe` INT NULL,
  `google_user_id` VARCHAR(45),
  `email` VARCHAR(45) NULL,
  `profil_id` INT NOT NULL,
  PRIMARY KEY (`person_id`));
  
-- Tabelle erstellen 'Profil'
-- -----------------------------------------------------------------------  
CREATE TABLE IF NOT EXISTS `Profil` (
  `profil_id` INT NOT NULL ,
  `hochschule` VARCHAR(45) NULL,
  `studiengang` VARCHAR(45) NULL,
  `semester` INT NULL,
  `lernfaecher` VARCHAR(45) NULL,
  `selbsteinschaetzung` INT NULL,
  `person_id` INT NOT NULL,
  PRIMARY KEY (`profil_id`));
  
  
-- Person Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Person` (person_id, name, vorname, lebensjahre, geschlecht, lerngruppe, google_user_id, email, profil_id)  
VALUES('1', 'Tyson', 'Mike', '50', 'männlich', '1', '1', 'ironmike@gmail.com', '20');
INSERT INTO `Person` (person_id, name, vorname, lebensjahre, geschlecht, lerngruppe, google_user_id, email, profil_id)  
VALUES('2', 'Wright', 'Peter', '52', 'männlich', '2', '2', 'snakebite@gmail.com', '30');
INSERT INTO `Person` (person_id, name, vorname, lebensjahre, geschlecht, lerngruppe, google_user_id, email, profil_id)  
VALUES('3', 'Mueller', 'Thomas', '32', 'männlich', '3', '3', 'miasanmia@gmail.com', '40');




-- Profil Entitäten erstellen
-- --------------------------------------------------------------------------------
INSERT INTO `Profil` (profil_id, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, person_id)  
VALUES('20', 'Uni Hohenheim', 'Wiwi', '1', 'BWL', '2', '1');
INSERT INTO `Profil` (profil_id, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, person_id)  
VALUES('30', 'HdM', 'WI', '2', 'Informatik', '4', '2');
