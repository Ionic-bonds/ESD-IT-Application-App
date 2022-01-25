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
CREATE DATABASE IF NOT EXISTS `developer` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `developer`;

-- --------------------------------------------------------

--
-- Table structure for table `developers`
--

DROP TABLE IF EXISTS `developer`;
CREATE TABLE IF NOT EXISTS `developer` (
  `Name` varchar(64) NOT NULL,
  `Phone` varchar(11) NOT NULL,
  `Address` varchar(64) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `book`
--

INSERT INTO `developer` (`Name`, `Phone`, `Address`) VALUES
('Beff Bezos', '+6599999999', 'Blk 999 LOL #99-99 S(999999)'),
('Grill Gates', '+6512345678', 'Blk 123 Test Rd #123 S(123456)'),
('Dlon Musk', '+6587654321', 'Blk 321 Demo Rd #321 S(654321)');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
