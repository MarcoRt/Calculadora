-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: escuela
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso` (
  `CursoID` int NOT NULL,
  `ProfesorID` int NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Nivel` int NOT NULL,
  PRIMARY KEY (`CursoID`),
  KEY `ProfesorID` (`ProfesorID`),
  CONSTRAINT `curso_ibfk_1` FOREIGN KEY (`ProfesorID`) REFERENCES `profesor` (`ProfesorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso`
--

LOCK TABLES `curso` WRITE;
/*!40000 ALTER TABLE `curso` DISABLE KEYS */;
INSERT INTO `curso` VALUES (101,1,'Calculo',1),(102,2,'Algebra Lineal',2),(103,3,'Calculo Avanzado',3),(201,4,'Historia de Mexico',1),(202,5,'Filosofia y Logica',1),(301,6,'Introduccion a la Psicologia',1),(302,7,'Nutricion',2);
/*!40000 ALTER TABLE `curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `DeptoID` int NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Director` varchar(50) NOT NULL,
  `Descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`DeptoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
INSERT INTO `departamento` VALUES (1,'Ingenieria','Miguel Velazquez','Departamento encargado del area de ingenieria'),(2,'Ciencias Sociales','Mateo Sousa','Departamento encargado del area de ciencias sociales'),(3,'Ciencias de la Salud','Mercedes Romero','Departamento encargado del area de ciencias de la salud');
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesor`
--

DROP TABLE IF EXISTS `profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesor` (
  `ProfesorID` int NOT NULL,
  `DeptoID` int NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Telefono` int NOT NULL,
  PRIMARY KEY (`ProfesorID`),
  KEY `DeptoID` (`DeptoID`),
  CONSTRAINT `profesor_ibfk_1` FOREIGN KEY (`DeptoID`) REFERENCES `departamento` (`DeptoID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesor`
--

LOCK TABLES `profesor` WRITE;
/*!40000 ALTER TABLE `profesor` DISABLE KEYS */;
INSERT INTO `profesor` VALUES (1,1,'Ildefonso Castillo','LEANDRO VALLE NO. 370 S/N, IRAPUATO CENTRO, 36500',55849615),(2,1,'Rafael Donoso','AV SAN PEDRO NO. 100 Int. F, SAN LUIS POTOSI CENTRO, 78000',55742653),(3,1,'Toribio Pizarro','BRAVO NO. 726, CENTRO, 91700',55423618),(4,2,'Efraín Costa','PARQUE NOROESTE NO. 718, EJIDAL, 81283',55684832),(5,2,'Ariadna Lerma','ORTIZ RUBIO NO. 300 NO. F, TECATE CENTRO, 21400',55421463),(6,3,'Esmeralda Chaparro','REPUBLICA NO 40 LOCAL 507, PLAZA TAPATIA, 443107',55854523),(7,3,'Priscila Bayón','CALLE 56 508 ALTOS, MERIDA CENTRO, 97000',55874569);
/*!40000 ALTER TABLE `profesor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-03 17:24:13
