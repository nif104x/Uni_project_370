-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: skillswap
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`username`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`username`) REFERENCES `person` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat` (
  `chat_id` int NOT NULL AUTO_INCREMENT,
  `conversation_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sender_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `message_text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`chat_id`),
  KEY `conversation_id` (`conversation_id`),
  KEY `sender_id` (`sender_id`),
  CONSTRAINT `chat_ibfk_1` FOREIGN KEY (`conversation_id`) REFERENCES `conversation` (`conversation_id`),
  CONSTRAINT `chat_ibfk_2` FOREIGN KEY (`sender_id`) REFERENCES `person` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `connection`
--

DROP TABLE IF EXISTS `connection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `connection` (
  `requester_username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `receiver_username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `status` enum('pending','accepted','blocked') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT 'pending',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`requester_username`,`receiver_username`),
  KEY `receiver_username` (`receiver_username`),
  CONSTRAINT `connection_ibfk_1` FOREIGN KEY (`requester_username`) REFERENCES `user` (`username`),
  CONSTRAINT `connection_ibfk_2` FOREIGN KEY (`receiver_username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connection`
--

LOCK TABLES `connection` WRITE;
/*!40000 ALTER TABLE `connection` DISABLE KEYS */;
INSERT INTO `connection` VALUES ('chef_marcus','marketing_gal','pending','2023-10-15 02:00:00'),('data_wiz','python_pro','accepted','2023-10-05 03:15:00'),('guitar_hero','ux_sarah','accepted','2023-10-02 05:30:00'),('js_newbie','python_pro','pending','2023-10-16 13:10:00'),('marketing_gal','js_newbie','accepted','2023-10-12 10:45:00'),('photo_phi','yoga_guru','pending','2023-10-17 06:00:00'),('python_pro','ux_sarah','accepted','2023-10-01 04:00:00'),('yoga_guru','fitness_fan','accepted','2023-10-10 08:20:00');
/*!40000 ALTER TABLE `connection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conversation`
--

DROP TABLE IF EXISTS `conversation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversation` (
  `conversation_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_one` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_two` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`conversation_id`),
  UNIQUE KEY `user_one` (`user_one`,`user_two`),
  KEY `user_two` (`user_two`),
  CONSTRAINT `conversation_ibfk_1` FOREIGN KEY (`user_one`) REFERENCES `person` (`username`),
  CONSTRAINT `conversation_ibfk_2` FOREIGN KEY (`user_two`) REFERENCES `person` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversation`
--

LOCK TABLES `conversation` WRITE;
/*!40000 ALTER TABLE `conversation` DISABLE KEYS */;
/*!40000 ALTER TABLE `conversation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES ('chef_marcus','hash_pass_3'),('data_wiz','hash_pass_6'),('fitness_fan','hash_pass_5'),('guitar_hero','hash_pass_2'),('js_newbie','hash_pass_10'),('marketing_gal','hash_pass_8'),('photo_phi','hash_pass_7'),('python_pro','hash_pass_1'),('ux_sarah','hash_pass_4'),('yoga_guru','hash_pass_9');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `review_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `reviewer_username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `reviewee_username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `review_text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `rating` float DEFAULT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`,`session_id`),
  KEY `session_id` (`session_id`),
  KEY `reviewer_username` (`reviewer_username`),
  KEY `reviewee_username` (`reviewee_username`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `session` (`session_id`),
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`reviewer_username`) REFERENCES `user` (`username`),
  CONSTRAINT `review_ibfk_3` FOREIGN KEY (`reviewee_username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session` (
  `session_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `teacher_username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `student_username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `skill_id` int DEFAULT NULL,
  `credit_used` int DEFAULT '5',
  `schedule_time` datetime DEFAULT NULL,
  `status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT 'pending',
  `link` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`session_id`),
  KEY `teacher_username` (`teacher_username`),
  KEY `student_username` (`student_username`),
  KEY `skill_id` (`skill_id`),
  CONSTRAINT `session_ibfk_1` FOREIGN KEY (`teacher_username`) REFERENCES `user` (`username`),
  CONSTRAINT `session_ibfk_2` FOREIGN KEY (`student_username`) REFERENCES `user` (`username`),
  CONSTRAINT `session_ibfk_3` FOREIGN KEY (`skill_id`) REFERENCES `skill` (`skill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_list`
--

DROP TABLE IF EXISTS `session_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session_list` (
  `session_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_time` datetime DEFAULT NULL,
  `session_status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`session_id`,`user_username`),
  KEY `user_username` (`user_username`),
  CONSTRAINT `session_list_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `session` (`session_id`),
  CONSTRAINT `session_list_ibfk_2` FOREIGN KEY (`user_username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_list`
--

LOCK TABLES `session_list` WRITE;
/*!40000 ALTER TABLE `session_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill` (
  `skill_id` int NOT NULL AUTO_INCREMENT,
  `skill_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`skill_id`),
  UNIQUE KEY `skill_name` (`skill_name`),
  FULLTEXT KEY `skill_name_2` (`skill_name`,`description`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill`
--

LOCK TABLES `skill` WRITE;
/*!40000 ALTER TABLE `skill` DISABLE KEYS */;
INSERT INTO `skill` VALUES (1,'Python Programming','Backend development and automation scripting.'),(2,'Acoustic Guitar','Learn chords, strumming patterns, and music theory.'),(3,'Italian Cooking','Authentic pasta, pizza, and sauce techniques.'),(4,'UI/UX Design','Interface design using Figma and Adobe XD.'),(5,'HIIT Workout','High intensity interval training for fitness.'),(6,'PowerBI','Data visualization and business intelligence.'),(7,'Photography','Composition, lighting, and digital editing.'),(8,'SEO Marketing','Search engine optimization and growth hacking.'),(9,'Yoga & Meditation','Physical postures and mental mindfulness.'),(10,'Spanish Language','Basic to advanced conversational Spanish.');
/*!40000 ALTER TABLE `skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `bio` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `average_rating` float DEFAULT '0',
  `total_credits` int DEFAULT '50',
  `experience_level` int DEFAULT '1',
  `join_date` date DEFAULT NULL,
  `status` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`username`),
  UNIQUE KEY `email` (`email`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`username`) REFERENCES `person` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('chef_marcus','Marcus V.','marcus@cook.com','Master of Italian cuisine. Looking for help with Social Media Marketing.',4.5,55,3,'2023-03-05',1),('data_wiz','Jordan Smith','j.smith@data.com','Data Scientist. Teaching PowerBI. Looking for French conversation practice.',5,90,5,'2023-05-01',1),('fitness_fan','Chloe Adams','chloe@fit.net','Certified Trainer. Teaching HIIT workouts. Wanting to learn Photography.',4.2,30,2,'2023-04-12',1),('guitar_hero','Liam Chen','liam@music.io','Professional musician. Teaching Acoustic Guitar for UI Design tips.',4.7,40,4,'2023-02-10',1),('js_newbie','Sam Wilson','sam@learn.io','Just starting my tech journey. Willing to teach English for JS help.',0,50,1,'2023-08-12',1),('marketing_gal','Elena Rodriguez','elena@growth.co','Marketing Strategist. Swap SEO growth hacks for Javascript basics.',4.4,50,3,'2023-06-10',1),('photo_phi','Philip Ng','phil@lens.com','Travel Photographer. Teaching Lightroom. Wanting to learn Basic Yoga.',4.6,45,3,'2023-05-15',1),('python_pro','Alex Rivera','alex@dev.com','Senior Dev. I can teach Python & SQL. Want to learn Spanish.',4.9,75,5,'2023-01-15',1),('ux_sarah','Sarah Jenkins','sarah@design.me','UI/UX Designer. I swap Figma tutorials for Backend logic help.',4.8,60,4,'2023-03-20',1),('yoga_guru','Maya Patil','maya@zen.com','Yoga Instructor. Teaching mindfulness. Interested in learning Video Editing.',4.9,65,4,'2023-07-01',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_skills`
--

DROP TABLE IF EXISTS `user_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_skills` (
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `skill_id` int NOT NULL,
  `skill_type` enum('TEACH','LEARN') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `proficiency_level` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`username`,`skill_id`,`skill_type`),
  KEY `skill_id` (`skill_id`),
  CONSTRAINT `user_skills_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE,
  CONSTRAINT `user_skills_ibfk_2` FOREIGN KEY (`skill_id`) REFERENCES `skill` (`skill_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_skills`
--

LOCK TABLES `user_skills` WRITE;
/*!40000 ALTER TABLE `user_skills` DISABLE KEYS */;
INSERT INTO `user_skills` VALUES ('data_wiz',6,'TEACH','Expert'),('data_wiz',10,'LEARN','Beginner'),('fitness_fan',5,'TEACH','Intermediate'),('fitness_fan',7,'LEARN','Beginner'),('guitar_hero',2,'TEACH','Expert'),('guitar_hero',4,'LEARN','Intermediate'),('python_pro',1,'TEACH','Expert'),('python_pro',10,'LEARN','Beginner'),('ux_sarah',1,'LEARN','Intermediate'),('ux_sarah',4,'TEACH','Expert');
/*!40000 ALTER TABLE `user_skills` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-23  7:05:57
