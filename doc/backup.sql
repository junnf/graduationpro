-- MySQL dump 10.14  Distrib 5.5.46-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: course
-- ------------------------------------------------------
-- Server version	5.5.46-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class` (
  `class_id` int(7) NOT NULL,
  `class_name` varchar(30) NOT NULL,
  `teacher_name` varchar(15) NOT NULL,
  `other` varchar(100) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1110001,'operating system','liping','lianxifangshiTelEmailQQ'),(1110002,'Alg','liping','lianximailQQ');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class_table`
--

DROP TABLE IF EXISTS `class_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class_table` (
  `course_id` int(7) NOT NULL,
  `week_num` int(1) NOT NULL,
  `week_day` int(1) NOT NULL,
  `time` int(1) NOT NULL,
  `location` varchar(50) NOT NULL,
  `class_id` int(7) NOT NULL,
  PRIMARY KEY (`course_id`,`week_num`,`week_day`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_table`
--

LOCK TABLES `class_table` WRITE;
/*!40000 ALTER TABLE `class_table` DISABLE KEYS */;
INSERT INTO `class_table` VALUES (1110001,1,1,2,'West 12 N201',1110001),(1110001,1,1,3,'West 12 N202',1110002),(1110001,1,3,1,'West 12 N201',1110001),(1110001,1,3,4,'West 12 N202',1110002);
/*!40000 ALTER TABLE `class_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_dep`
--

DROP TABLE IF EXISTS `user_dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_dep` (
  `dep_num` int(5) NOT NULL,
  `name` varchar(20) NOT NULL,
  `passwd` varchar(50) DEFAULT NULL,
  `sexuality` int(1) DEFAULT NULL,
  PRIMARY KEY (`dep_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_dep`
--

LOCK TABLES `user_dep` WRITE;
/*!40000 ALTER TABLE `user_dep` DISABLE KEYS */;
INSERT INTO `user_dep` VALUES (11101,'admin_a','ljn7168396123',1);
/*!40000 ALTER TABLE `user_dep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_student`
--

DROP TABLE IF EXISTS `user_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_student` (
  `uid` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `sexuality` int(1) NOT NULL,
  `course_id` int(7) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_student`
--

LOCK TABLES `user_student` WRITE;
/*!40000 ALTER TABLE `user_student` DISABLE KEYS */;
INSERT INTO `user_student` VALUES (201215121,'junningliu','ljn7168396',1,1110001);
/*!40000 ALTER TABLE `user_student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-18 22:56:32
