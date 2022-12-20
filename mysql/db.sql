-- Datenbank Sopra-LernApp

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema Sopra-LernApp
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Sopra-LernApp` ;

-- -----------------------------------------------------
-- Schema Sopra-LernApp
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Sopra-LernApp` DEFAULT CHARACTER SET utf8mb3 ;
USE `Sopra-LernApp` ;

-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Nachricht`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Nachricht` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Nachricht` (
  `nachricht_id` INT NOT NULL,
  `nachricht_text` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`nachricht_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

--
-- Dumping data for table `Nachricht`
--
LOCK TABLES `Sopra-LernApp`.`Nachricht` WRITE;
/*!40000 ALTER TABLE `Sopra-LernApp`.`Nachricht` DISABLE KEYS */;
INSERT INTO `Sopra-LernApp`.`Nachricht` VALUES ('1', 'Hallo, ich würde gerne Informatik lernen'), ('2', 'Ich würde gerne morgen lernen');
/*!40000 ALTER TABLE `Sopra-LernApp`.`Nachricht` ENABLE KEYS */;
UNLOCK TABLES;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Konversation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Konversation` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Konversation` (
  `konversation_id` INT NOT NULL,
  `anfragestatus` VARCHAR(45) NULL DEFAULT NULL,
  `nachricht_id` INT NOT NULL,
  PRIMARY KEY (`konversation_id`),
  INDEX `fk_Konversation_Nachricht1_idx` (`nachricht_id` ASC) VISIBLE,
  CONSTRAINT `fk_Konversation_Nachricht1`
    FOREIGN KEY (`nachricht_id`)
    REFERENCES `Sopra-LernApp`.`Nachricht` (`nachricht_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

--
-- Dumping data for table `Konversation`
--
LOCK TABLES `Sopra-LernApp`.`Konversation` WRITE;
/*!40000 ALTER TABLE `Sopra-LernApp`.`Konversation` DISABLE KEYS */;
INSERT INTO `Sopra-LernApp`.`Konversation` VALUES ('1', 'angenommen', '1'), (2, 'abgelehnt', '2');
/*!40000 ALTER TABLE `Sopra-LernApp`.`Konversation` ENABLE KEYS */;
UNLOCK TABLES;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Profil`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Profil` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Profil` (
  `profil_id` INT NOT NULL,
  `hochschule` VARCHAR(45) NULL DEFAULT NULL,
  `studiengang` VARCHAR(45) NULL DEFAULT NULL,
  `semester` INT NULL DEFAULT NULL,
  `lernfaecher` VARCHAR(45) NULL DEFAULT NULL,
  `selbsteinschaetzung` INT NULL DEFAULT NULL,
  PRIMARY KEY (`profil_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

--
-- Dumping data for table `Profil`
--
LOCK TABLES `Sopra-LernApp`.`Profil` WRITE;
/*!40000 ALTER TABLE `Sopra-LernApp`.`Profil` DISABLE KEYS */;
INSERT INTO `Sopra-LernApp`.`Profil` VALUES ('20', 'Uni Hohenheim', 'Wiwi', '1', 'BWL', '2'),
('30', 'HdM', 'WI', '2', 'Informatik', '2'), ('40', 'HdM', 'WI', '4', 'Informatik', '4');
/*!40000 ALTER TABLE `Sopra-LernApp`.`Profil` ENABLE KEYS */;
UNLOCK TABLES;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Chatteilnahme`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Chatteilnahme` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Chatteilnahme` (
  `chatteilnahme_id` INT NOT NULL,
  `profil_id` INT NOT NULL,
  `konversation_id` INT NOT NULL,
  PRIMARY KEY (`chatteilnahme_id`),
  INDEX `fk_Chatteilnahme_Profil1_idx` (`profil_id` ASC) VISIBLE,
  INDEX `fk_Chatteilnahme_Konversation1_idx` (`konversation_id` ASC) VISIBLE,
  CONSTRAINT `fk_Chatteilnahme_Konversation1`
    FOREIGN KEY (`konversation_id`)
    REFERENCES `Sopra-LernApp`.`Konversation` (`konversation_id`),
  CONSTRAINT `fk_Chatteilnahme_Profil1`
    FOREIGN KEY (`profil_id`)
    REFERENCES `Sopra-LernApp`.`Profil` (`profil_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Lerngruppe`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Lerngruppe` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Lerngruppe` (
  `lerngruppe_id` INT NOT NULL,
  `gruppenname` VARCHAR(45) NULL DEFAULT NULL,
  `teilnehmer` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`lerngruppe_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

--
-- Dumping data for table `Lerngruppe`
--
LOCK TABLES `Sopra-LernApp`.`Lerngruppe` WRITE;
/*!40000 ALTER TABLE `Sopra-LernApp`.`Lerngruppe` DISABLE KEYS */;
INSERT INTO `Sopra-LernApp`.`Lerngruppe` VALUES ('1', 'Informatik für Dummies', 'Peter Wright, Thomas Mueller');
/*!40000 ALTER TABLE `Sopra-LernApp`.`Lerngruppe` ENABLE KEYS */;
UNLOCK TABLES;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Gruppenteilnahme`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Gruppenteilnahme` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Gruppenteilnahme` (
  `gruppenteilnahme_id` INT NOT NULL,
  `status` VARCHAR(45) NULL DEFAULT NULL,
  `profil_id` INT NOT NULL,
  `lerngruppe_id` INT NOT NULL,
  PRIMARY KEY (`gruppenteilnahme_id`),
  INDEX `fk_Gruppenteilnehmer_Profil_idx` (`profil_id` ASC) VISIBLE,
  INDEX `fk_Gruppenteilnahme_Lerngruppe1_idx` (`lerngruppe_id` ASC) VISIBLE,
  CONSTRAINT `fk_Gruppenteilnahme_Lerngruppe1`
    FOREIGN KEY (`lerngruppe_id`)
    REFERENCES `Sopra-LernApp`.`Lerngruppe` (`lerngruppe_id`),
  CONSTRAINT `fk_Gruppenteilnehmer_Profil`
    FOREIGN KEY (`profil_id`)
    REFERENCES `Sopra-LernApp`.`Profil` (`profil_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Lerndaten`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Lerndaten` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Lerndaten` (
  `lerndaten_id` INT NOT NULL,
  `tageszeit` VARCHAR(45) NULL DEFAULT NULL,
  `tage` VARCHAR(45) NULL DEFAULT NULL,
  `frequenz` INT NULL DEFAULT NULL,
  `lernort` VARCHAR(45) NULL DEFAULT NULL,
  `lernart` VARCHAR(45) NULL DEFAULT NULL,
  `gruppengroesse_min` INT NULL DEFAULT NULL,
  `gruppengroesse_max` INT NULL DEFAULT NULL,
  `vorkenntnisse` VARCHAR(45) NULL DEFAULT NULL,
  `extrovertiertheit` VARCHAR(45) NULL DEFAULT NULL,
  `profil_id` INT NOT NULL,
  PRIMARY KEY (`lerndaten_id`),
  INDEX `fk_Lerndaten_Profil1_idx` (`profil_id` ASC) VISIBLE,
  CONSTRAINT `fk_Lerndaten_Profil1`
    FOREIGN KEY (`profil_id`)
    REFERENCES `Sopra-LernApp`.`Profil` (`profil_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

--
-- Dumping data for table `Lerndaten`
--
LOCK TABLES `Sopra-LernApp`.`Lerndaten` WRITE;
/*!40000 ALTER TABLE `Sopra-LernApp`.`Lerndaten` DISABLE KEYS */;
INSERT INTO `Sopra-LernApp`.`Lerndaten` VALUES ('1', 'morgens', 'Montag, Mittwoch', 2, 'zuhause', 'online', 2, 4, 'schlecht', 'mittel', '20'),
('2', 'mittags', 'Mittwoch, Freitag, Samstag', 3, 'Hochschule', 'offline', 2, 6, 'mittel', 'mittel', '30'),
('3', 'mittags', 'Montag, Freitag', 2, 'Hochschule', 'offline', 2, 6, 'gut', 'sehr', '40');
/*!40000 ALTER TABLE `Sopra-LernApp`.`Lerndaten` ENABLE KEYS */;
UNLOCK TABLES;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Lernfaecher`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Lernfaecher` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Lernfaecher` (
  `lernfach_id` INT NOT NULL,
  `lernfachname` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`lernfach_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Person` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Person` (
  `person_id` INT NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `vorname` VARCHAR(45) NULL DEFAULT NULL,
  `lebensjahre` INT NULL,
  `geschlecht` VARCHAR(45) NULL DEFAULT NULL,
  `lerngruppe` INT NULL DEFAULT NULL,
  `google_user_id` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `profil_id` INT NOT NULL,
  PRIMARY KEY (`person_id`),
  INDEX `fk_Person_Profil1_idx` (`profil_id` ASC) VISIBLE,
  CONSTRAINT `fk_Person_Profil1`
    FOREIGN KEY (`profil_id`)
    REFERENCES `Sopra-LernApp`.`Profil` (`profil_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

--
-- Dumping data for table `Person`
--
LOCK TABLES `Sopra-LernApp`.`Person` WRITE;
/*!40000 ALTER TABLE `Sopra-LernApp`.`Person` DISABLE KEYS */;
INSERT INTO `Sopra-LernApp`.`Person` VALUES ('1', 'Tyson', 'Mike', '50', 'männlich', '1', '1', 'ironmike@gmail.com', '20'),
('2', 'Wright', 'Peter', '52', 'männlich', '2', '2', 'snakebite@gmail.com', '30'),
('3', 'Mueller', 'Thomas', '32', 'männlich', '3', '3', 'miasanmia@gmail.com', '40');
/*!40000 ALTER TABLE `Sopra-LernApp`.`Person` ENABLE KEYS */;
UNLOCK TABLES;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Profil_Lernfaecher`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Profil_Lernfaecher` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Profil_Lernfaecher` (
  `profil_id` INT NOT NULL,
  `lernfach_id` INT NOT NULL,
  INDEX `fk_Profil_Lernfaecher_Profil1_idx` (`profil_id` ASC) VISIBLE,
  INDEX `fk_Profil_Lernfaecher_Lernfaecher1_idx` (`lernfach_id` ASC) VISIBLE,
  CONSTRAINT `fk_Profil_Lernfaecher_Lernfaecher1`
    FOREIGN KEY (`lernfach_id`)
    REFERENCES `Sopra-LernApp`.`Lernfaecher` (`lernfach_id`),
  CONSTRAINT `fk_Profil_Lernfaecher_Profil1`
    FOREIGN KEY (`profil_id`)
    REFERENCES `Sopra-LernApp`.`Profil` (`profil_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `Sopra-LernApp`.`Match`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Sopra-LernApp`.`Match` ;

CREATE TABLE IF NOT EXISTS `Sopra-LernApp`.`Match` (
  `match_id` INT NOT NULL,
  `suchende_person_id` INT NULL DEFAULT NULL,
  `quote` FLOAT NULL DEFAULT NULL,
  `lernfach` VARCHAR(45) NULL DEFAULT NULL,
  `match_profil_id` INT NOT NULL,
  PRIMARY KEY (`match_id`),
  INDEX `fk_match_Profil1_idx` (`match_profil_id` ASC) VISIBLE,
  CONSTRAINT `fk_match_Profil1`
    FOREIGN KEY (`match_profil_id`)
    REFERENCES `Sopra-LernApp`.`Profil` (`profil_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
