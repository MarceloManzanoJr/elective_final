-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: health_center
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int NOT NULL,
  `Staff_staff_id` int NOT NULL,
  `date_time_of_appointment` datetime NOT NULL,
  PRIMARY KEY (`appointment_id`),
  KEY `fk_Appointments_Patients1_idx` (`patient_id`),
  KEY `fk_Appointments_Staff1_idx` (`Staff_staff_id`),
  CONSTRAINT `fk_Appointments_Patients1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `fk_Appointments_Staff1` FOREIGN KEY (`Staff_staff_id`) REFERENCES `staff` (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (1,1,3,'2024-12-12 09:00:00'),(2,2,5,'2024-12-12 10:00:00'),(3,3,2,'2024-12-12 11:00:00'),(4,4,8,'2024-12-12 12:30:00'),(5,5,6,'2024-12-13 14:00:00'),(6,6,7,'2024-12-13 15:00:00'),(7,7,4,'2024-12-13 16:30:00'),(8,8,1,'2024-12-14 08:00:00'),(9,9,9,'2024-12-14 09:30:00'),(10,10,10,'2024-12-14 11:00:00'),(11,11,12,'2024-12-14 13:00:00'),(12,12,14,'2024-12-14 15:00:00'),(13,13,11,'2024-12-15 10:00:00'),(14,14,13,'2024-12-15 11:30:00'),(15,15,15,'2024-12-15 13:00:00'),(16,16,18,'2024-12-15 14:30:00'),(17,17,16,'2024-12-16 09:00:00'),(18,18,17,'2024-12-16 10:30:00'),(19,19,19,'2024-12-16 12:00:00'),(20,20,20,'2024-12-16 14:00:00'),(21,21,21,'2024-12-17 09:00:00'),(22,22,22,'2024-12-17 10:30:00'),(23,23,23,'2024-12-17 13:00:00'),(24,24,24,'2024-12-17 15:00:00'),(25,25,25,'2024-12-17 16:30:00');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medication`
--

DROP TABLE IF EXISTS `medication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medication` (
  `medication_id` int NOT NULL AUTO_INCREMENT,
  `medication_type_code` int NOT NULL,
  `medication_unit_cost` int DEFAULT NULL,
  `medication_name` varchar(255) NOT NULL,
  `medication_description` varchar(255) NOT NULL,
  PRIMARY KEY (`medication_id`),
  KEY `fk_Medication_medication_types_idx` (`medication_type_code`),
  CONSTRAINT `fk_Medication_medication_types` FOREIGN KEY (`medication_type_code`) REFERENCES `medication_types` (`medication_type_code`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medication`
--

LOCK TABLES `medication` WRITE;
/*!40000 ALTER TABLE `medication` DISABLE KEYS */;
INSERT INTO `medication` VALUES (1,1,50,'Amoxicillin','Used to treat bacterial infections'),(2,2,25,'Paracetamol','Relieves mild to moderate pain and reduces fever'),(3,3,30,'Ibuprofen','Reduces inflammation and pain'),(4,4,60,'Cetirizine','Relieves allergy symptoms'),(5,5,100,'Oseltamivir','Treats influenza virus infections'),(6,6,70,'Fluconazole','Antifungal for yeast infections'),(7,7,90,'Diazepam','Used for anxiety and muscle spasms'),(8,8,80,'Salbutamol','Treats asthma and bronchospasms'),(9,9,45,'Furosemide','Diuretic for high blood pressure and edema'),(10,10,200,'Warfarin','Prevents blood clot formation'),(11,11,150,'Sertraline','Antidepressant for anxiety and depression'),(12,12,65,'Prednisolone','Anti-inflammatory for various conditions'),(13,13,110,'Olanzapine','Antipsychotic for schizophrenia and bipolar disorder'),(14,14,55,'Ondansetron','Prevents nausea and vomiting'),(15,15,20,'Bisacodyl','Laxative for constipation relief'),(16,16,25,'Ranitidine','Reduces stomach acid production'),(17,17,40,'Chlorhexidine','Antiseptic for wound cleaning'),(18,18,150,'Levonorgestrel','Emergency contraceptive'),(19,19,500,'COVID-19 Vaccine','Stimulates immune response to prevent COVID-19'),(20,20,400,'Methotrexate','Immunosuppressant for autoimmune diseases'),(21,21,300,'Metformin','Controls blood sugar levels in diabetes'),(22,22,120,'Amlodipine','Reduces high blood pressure'),(23,23,90,'Atorvastatin','Lowers cholesterol levels'),(24,24,35,'Dextromethorphan','Suppresses cough'),(25,25,60,'Guaifenesin','Loosens mucus in the respiratory tract');
/*!40000 ALTER TABLE `medication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medication_types`
--

DROP TABLE IF EXISTS `medication_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medication_types` (
  `medication_type_code` int NOT NULL AUTO_INCREMENT,
  `medication_type_name` varchar(225) NOT NULL,
  `medication_type_description` varchar(225) NOT NULL,
  PRIMARY KEY (`medication_type_code`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medication_types`
--

LOCK TABLES `medication_types` WRITE;
/*!40000 ALTER TABLE `medication_types` DISABLE KEYS */;
INSERT INTO `medication_types` VALUES (1,'Antibiotic','Used to treat bacterial infections'),(2,'Analgesic','Pain reliever medication'),(3,'Antipyretic','Reduces fever'),(4,'Antihistamine','Relieves allergy symptoms'),(5,'Antiviral','Used to treat viral infections'),(6,'Antifungal','Treats fungal infections'),(7,'Sedative','Promotes calm or induces sleep'),(8,'Bronchodilator','Opens airways in respiratory conditions'),(9,'Diuretic','Promotes urine production'),(10,'Anticoagulant','Prevents blood clots'),(11,'Antidepressant','Treats depression'),(12,'Anti-inflammatory','Reduces inflammation'),(13,'Antipsychotic','Treats psychiatric conditions'),(14,'Antiemetic','Prevents nausea and vomiting'),(15,'Laxative','Relieves constipation'),(16,'Antacid','Neutralizes stomach acid'),(17,'Antiseptic','Prevents infection in wounds'),(18,'Contraceptive','Used for birth control'),(19,'Vaccine','Stimulates immune response'),(20,'Immunosuppressant','Suppresses immune system activity'),(21,'Antidiabetic','Controls blood sugar levels'),(22,'Antihypertensive','Lowers high blood pressure'),(23,'Cholesterol-lowering','Reduces cholesterol levels'),(24,'Cough Suppressant','Relieves cough symptoms'),(25,'Expectorant','Loosens mucus in the respiratory tract');
/*!40000 ALTER TABLE `medication_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `middle_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `date_of_birth` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'Jane','M','Doe','1990-01-01','Famale','123 Main Street'),(2,'Jane','Elizabeth','Smith','1990-11-22','Female','456 Oak Avenue'),(3,'Sophia','Grace','Anderson','1993-10-05','Male','707 Palm Road'),(4,'Emily','Rose','Brown','1995-07-04','Female','101 Maple Boulevard'),(5,'Michael','Thomas','Davis','1978-12-19','Male','202 Birch Drive'),(6,'Sarah','Anne','Miller','1988-05-11','Female','303 Cedar Court'),(7,'David','William','Wilson','1992-09-30','Male','404 Spruce Way'),(8,'Emma','Marie','Moore','1997-08-25','Female','505 Chestnut Street'),(9,'Christopher','Daniel','Taylor','1980-01-14','Male','606 Walnut Lane'),(10,'Sophia','Grace','Anderson','1993-10-05','Female','707 Palm Road'),(11,'Joshua','Edward','Thomas','1987-04-27','Male','808 Cypress Avenue'),(12,'Olivia','Claire','Jackson','1999-06-08','Female','909 Fir Street'),(13,'Matthew','Scott','White','1981-02-18','Male','1010 Magnolia Circle'),(14,'Isabella','Faith','Harris','1996-03-20','Female','1111 Redwood Drive'),(15,'Andrew','Paul','Martin','1989-07-12','Male','1212 Sycamore Way'),(16,'Mia','Hope','Thompson','2000-05-24','Female','1313 Aspen Avenue'),(17,'Daniel','George','Garcia','1975-08-03','Male','1414 Poplar Lane'),(18,'Charlotte','Lily','Martinez','1998-09-16','Female','1515 Holly Street'),(19,'James','Henry','Robinson','1984-12-07','Male','1616 Willow Drive'),(20,'Amelia','Rose','Clark','2001-04-09','Female','1717 Sequoia Boulevard'),(21,'Benjamin','Lucas','Rodriguez','1986-01-30','Male','1818 Elmwood Court'),(22,'Ava','Ivy','Lewis','1994-11-13','Female','1919 Pinewood Circle'),(23,'Ethan','Nathaniel','Lee','1979-02-25','Male','2020 Birchwood Lane'),(24,'Lily','Victoria','Walker','1983-06-29','Female','2121 Cedarwood Street'),(25,'Alexander','Ryan','Hall','1991-10-17','Male','2222 Ashwood Avenue'),(26,'John','A.','Doe','1990-01-01','Male','123 Elm Street'),(27,'John','A.','Doe','1990-01-01','Male','123 Elm Street'),(28,'John','A.','Doe','1990-01-01','Male','123 Elm Street'),(29,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(30,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(31,'John','Michael','Doe','1985-06-15 00:00:00','Male','123 Elm Street'),(32,'John','Michael','Doe','1985-06-15 00:00:00','Male','123 Elm Street'),(41,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(42,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(43,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(44,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(45,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(46,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(47,'Alice','','Brown','2000-01-01','Female','789 Maple Street'),(48,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(49,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(50,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(51,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(52,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(53,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(54,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(55,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(56,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(57,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(58,'Alice','','Brown','2000-01-01','Female','789 Maple Street'),(59,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(60,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(61,'John','Michael','Doe','1985-06-15','Male','123 Elm Street'),(62,'Jane','','Smith','1990-03-22','Female','456 Oak Avenue'),(63,'John','M','Doe','1990-01-01','Male','123 Main Street'),(64,'Sophia','Grace','Anderson','1993-10-05','Female','707 Palm Road'),(65,'Sophia','Grace','Anderson','1993-10-05','Female','707 Palm Road'),(66,'Sophia','Grace','Anderson','1993-10-05','Female','707 Palm Road'),(67,'Sophia','Grace','Anderson','1993-10-05','Male','707 Palm Road');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients_medecation`
--

DROP TABLE IF EXISTS `patients_medecation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients_medecation` (
  `patients_medication_id` int NOT NULL AUTO_INCREMENT,
  `Medication_medication_id` int NOT NULL,
  `Patients_patient_id` int NOT NULL,
  `date_time_administered` varchar(225) NOT NULL,
  `dosage` varchar(225) NOT NULL,
  `comments` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`patients_medication_id`),
  KEY `fk_Patients_Medecation_Medication1_idx` (`Medication_medication_id`),
  KEY `fk_Patients_Medecation_Patients1_idx` (`Patients_patient_id`),
  CONSTRAINT `fk_Patients_Medecation_Medication1` FOREIGN KEY (`Medication_medication_id`) REFERENCES `medication` (`medication_id`),
  CONSTRAINT `fk_Patients_Medecation_Patients1` FOREIGN KEY (`Patients_patient_id`) REFERENCES `patients` (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients_medecation`
--

LOCK TABLES `patients_medecation` WRITE;
/*!40000 ALTER TABLE `patients_medecation` DISABLE KEYS */;
INSERT INTO `patients_medecation` VALUES (1,1,1,'2024-01-01 08:30:00','500mg','Morning dose'),(2,2,2,'2024-01-01 12:00:00','250mg','After lunch'),(3,3,3,'2024-01-01 18:00:00','100mg','Evening dose'),(4,4,4,'2024-01-02 08:30:00','200mg','Pre-breakfast'),(5,5,5,'2024-01-02 12:30:00','300mg','Post-lunch'),(6,6,6,'2024-01-02 19:00:00','150mg','Night dose'),(7,7,7,'2024-01-03 09:00:00','600mg','Before meal'),(8,8,8,'2024-01-03 13:00:00','400mg','After meal'),(9,9,9,'2024-01-03 17:30:00','350mg','Pre-dinner'),(10,10,10,'2024-01-04 08:00:00','500mg','Daily dose'),(11,11,11,'2024-01-04 14:00:00','100mg','Midday'),(12,12,12,'2024-01-04 20:00:00','250mg','After dinner'),(13,13,13,'2024-01-05 07:30:00','200mg','Morning'),(14,14,14,'2024-01-05 13:30:00','300mg','Afternoon'),(15,15,15,'2024-01-05 19:30:00','450mg','Night'),(16,16,16,'2024-01-06 08:45:00','350mg','Morning routine'),(17,17,17,'2024-01-06 12:15:00','150mg','After lunch'),(18,18,18,'2024-01-06 18:15:00','500mg','Pre-sleep'),(19,19,19,'2024-01-07 09:45:00','600mg','Before workout'),(20,20,20,'2024-01-07 15:00:00','400mg','Evening medication'),(21,21,21,'2024-01-07 21:30:00','250mg','Bedtime dose'),(22,22,22,'2024-01-08 08:15:00','200mg','Breakfast supplement'),(23,23,23,'2024-01-08 14:30:00','300mg','Lunch supplement'),(24,24,24,'2024-01-08 20:45:00','500mg','Dinner supplement'),(25,25,25,'2024-01-09 07:00:00','450mg','Morning dose');
/*!40000 ALTER TABLE `patients_medecation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staff_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `middle_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) NOT NULL,
  `data_of_birth` varchar(45) NOT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `qualifications` varchar(45) NOT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'John','A.','Doe','1985-03-15','Male','MBBS'),(2,'Jane','B.','Smith','1990-07-22','Female','Nurse'),(3,'Mike','C.','Johnson','1982-01-08','Male','Pharmacist'),(4,'Emily','D.','Brown','1995-05-11','Female','Surgeon'),(5,'Chris','E.','Davis','1987-10-19','Male','Pediatrician'),(6,'Laura','F.','Miller','1993-09-27','Female','Dermatologist'),(7,'Daniel','G.','Wilson','1984-02-14','Male','Radiologist'),(8,'Sophia','H.','Moore','1989-06-06','Female','Nurse Practitioner'),(9,'David','I.','Taylor','1991-12-31','Male','Physiotherapist'),(10,'Olivia','J.','Anderson','1986-04-17','Female','Orthopedist'),(11,'Matthew','K.','Thomas','1992-11-25','Male','Psychologist'),(12,'Lily','L.','Jackson','1994-08-30','Female','Optometrist'),(13,'Ethan','M.','White','1983-03-20','Male','Cardiologist'),(14,'Emma','N.','Harris','1988-07-10','Female','Anesthesiologist'),(15,'James','O.','Martin','1985-12-05','Male','Pathologist'),(16,'Isabella','P.','Lee','1990-02-23','Female','Midwife'),(17,'Lucas','Q.','Perez','1987-01-15','Male','General Practitioner'),(18,'Mia','R.','Clark','1996-06-12','Female','Nutritionist'),(19,'Alexander','S.','Lewis','1981-08-03','Male','Neurologist'),(20,'Ava','T.','Young','1992-05-07','Female','Dentist'),(21,'Benjamin','U.','Hall','1984-09-01','Male','Gynecologist'),(22,'Chloe','V.','Walker','1993-03-10','Female','Occupational Therapist'),(23,'Noah','W.','Allen','1986-11-15','Male','Ophthalmologist'),(24,'Harper','X.','King','1991-12-28','Female','ENT Specialist'),(25,'William','Y.','Scott','1989-07-21','Male','Medical Assistant');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-14 14:05:39
