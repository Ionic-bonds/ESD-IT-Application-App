-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
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
-- Database: `developer`
--
CREATE DATABASE IF NOT EXISTS `interest` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `interest`;

-- --------------------------------------------------------

--
-- Table structure for table `developers`
--

DROP TABLE IF EXISTS `interest`;
CREATE TABLE IF NOT EXISTS `interest` (
  `IntID` int(255) NOT NULL AUTO_INCREMENT,
  `Title` varchar(64) NOT NULL,
  `Name` varchar(64) NOT NULL,
  `ListingID` int(255) NOT NULL,
  `Status` varchar(255) NOT NULL DEFAULT 'Open',
  PRIMARY KEY (`IntID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT /*;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
