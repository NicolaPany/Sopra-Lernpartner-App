
-- Datenbank Sopra-LernApp

CREATE DATABASE IF NOT EXISTS `Sopra-LernApp` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Sopra-LernApp`;

-- Tabelle erstellen 'Person'
-- -----------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `Person` (
  `id` INT NOT NULL ,
  `name` VARCHAR(45) NULL,
  `vorname` VARCHAR(45) NULL,
  `lebensjahre` INT NOT NULL,
  `geschlecht` VARCHAR(45) NULL,
  `semester` INT NULL,
  `studiengang` VARCHAR(45) NULL,
  `lerngruppe` INT NULL,
  `google_user_id` VARCHAR(45),
  `email` VARCHAR(45) NULL,
  `profil_id` INT NOT NULL,
  PRIMARY KEY (`id`, `profil_id`));
  
  
-- Person Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Person` (id, name, vorname, lebensjahre, geschlecht, semester, studiengang, lerngruppe, google_user_id, email, profil_id)  
VALUES('1', 'Tyson', 'Mike', '50', 'männlich', '1', 'Wiwi', '1', '1', 'ironmike@gmail.com', '1');
INSERT INTO `Person` (id, name, vorname, lebensjahre, geschlecht, semester, studiengang, lerngruppe, google_user_id, email, profil_id)  
VALUES('2', 'Wright', 'Peter', '52', 'männlich', '2', 'Wirtschaftsinformatik', '2', '2', 'snakebite@gmail.com', '2');
INSERT INTO `Person` (id, name, vorname, lebensjahre, geschlecht, semester, studiengang, lerngruppe, google_user_id, email, profil_id)  
VALUES('3', 'Mueller', 'Thomas', '32', 'männlich', '5', 'Verpackungstechnik', '3', '3', 'miasanmia@gmail.com', '3');