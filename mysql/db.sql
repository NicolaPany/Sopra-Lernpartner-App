
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
  

-- Tabelle erstellen 'Lerndaten'
-- -----------------------------------------------------------------------  
CREATE TABLE IF NOT EXISTS `Lerndaten` (
  `lerndaten_id` INT NOT NULL ,
  `tageszeit` VARCHAR(45) NULL,
  `tage` VARCHAR(45) NULL,
  `frequenz` INT NULL,
  `lernort` VARCHAR(45) NULL,
  `lernart` VARCHAR(45) NULL,
  `gruppengroesse_min` INT NULL,
  `gruppengroesse_max` INT NULL,
  `vorkenntnisse` VARCHAR(45) NULL,
  `extrovertiertheit` VARCHAR(45) NULL,
  `profil_id` INT NOT NULL,
  PRIMARY KEY (`lerndaten_id`));
  
  
-- Tabelle erstellen 'Lerngruppe'
-- -----------------------------------------------------------------------  
CREATE TABLE IF NOT EXISTS `Lerngruppe` (
  `lerngruppe_id` INT NOT NULL ,
  `gruppenname` VARCHAR(45) NULL,
  `teilnehmer` VARCHAR(45) NULL,
  PRIMARY KEY (`lerngruppe_id`));
  

-- Tabelle erstellen 'Konversation'
-- -----------------------------------------------------------------------  
CREATE TABLE IF NOT EXISTS `Konversation` (
  `konversation_id` INT NOT NULL ,
  `anfragestatus` VARCHAR(45) NULL,
  PRIMARY KEY (`konversation_id`));
  
  
  -- Tabelle erstellen 'Nachricht'
-- -----------------------------------------------------------------------  
CREATE TABLE IF NOT EXISTS `Nachricht` (
  `nachricht_id` INT NOT NULL ,
  `nachricht_text` VARCHAR(300) NULL,
  `person_id` INT NOT NULL,
  `konversation_id` INT NOT NULL ,
  PRIMARY KEY (`nachricht_id`));
  
  
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
VALUES('30', 'HdM', 'WI', '2', 'Informatik', '2', '2');
INSERT INTO `Profil` (profil_id, hochschule, studiengang, semester, lernfaecher, selbsteinschaetzung, person_id)  
VALUES('40', 'HdM', 'WI', '4', 'Informatik', '4', '3');




-- Lerndaten Entitäten erstellen
-- ---------------------------------------------------------------------------------------------------------------------------
INSERT INTO `Lerndaten` (lerndaten_id, tageszeit, tage, frequenz, lernort, lernart, gruppengroesse_min, gruppengroesse_max, vorkenntnisse, extrovertiertheit, profil_id)  
VALUES('1', 'morgens', 'Montag, Mittwoch', '2', 'zuhause', 'online', '2', '4', 'schlecht', 'mittel', '20');
INSERT INTO `Lerndaten` (lerndaten_id, tageszeit, tage, frequenz, lernort, lernart, gruppengroesse_min, gruppengroesse_max, vorkenntnisse, extrovertiertheit, profil_id)  
VALUES('2', 'mittags', 'Mittwoch, Freitag, Samstag', '3', 'Hochschule', 'offline', '2', '6', 'mittel', 'mittel', '30');
INSERT INTO `Lerndaten` (lerndaten_id, tageszeit, tage, frequenz, lernort, lernart, gruppengroesse_min, gruppengroesse_max, vorkenntnisse, extrovertiertheit, profil_id)  
VALUES('3', 'mittags', 'Montag, Freitag', '2', 'Hochschule', 'offline', '2', '6', 'gut', 'sehr', '40');




-- Lerngruppen Entitäten erstellen
-- --------------------------------------------------------------------------------
INSERT INTO `Lerngruppe` (lerngruppe_id, gruppenname, teilnehmer)  
VALUES('1', 'Informatik für Dummies', 'Peter Wright, Thomas Mueller');



-- Konversation Entitäten erstellen
-- --------------------------------------------------------------------------------
INSERT INTO `Konversation` (konversation_id, anfragestatus)  
VALUES('1', 'akzeptiert');



-- Nachricht Entitäten erstellen
-- --------------------------------------------------------------------------------
INSERT INTO `Nachricht` (nachricht_id, nachricht_text, person_id, konversation_id)  
VALUES('1', 'Hallo, ich würde gerne Informatik lernen', '2', '1');
