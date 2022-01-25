-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 23, 2021 at 01:41 PM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `listing`
--

CREATE DATABASE IF NOT EXISTS `listing` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `listing`;
-- --------------------------------------------------------

--
-- Table structure for table `listing`
--

DROP TABLE IF EXISTS `listing`;
CREATE TABLE IF NOT EXISTS `listing` (
  `ListingID` int(255) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `DateTime` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `Title` varchar(255) NOT NULL,
  `ProgrammingLanguage` varchar(255) NOT NULL,
  `ListingDescription` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL DEFAULT 'Open',
  `Price` decimal(5,2) NOT NULL,
  PRIMARY KEY (`ListingID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `listing` (`ListingID`, `Name`, `DateTime`, `Title`, `ProgrammingLanguage`, `ListingDescription`, `Status`, `Price`) VALUES
('1', NULL, '2021-04-06 07:21:15.79229', 'Cool Microservice', 'Java', 'Please help me do a cool microservice of your choice!', 'Open', '100.00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
