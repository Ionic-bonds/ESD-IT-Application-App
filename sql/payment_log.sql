-- Host: 127.0.0.1:3306
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `payment_log`
--
CREATE DATABASE IF NOT EXISTS `payment_log` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `payment_log`;

-- --------------------------------------------------------

--
-- Table structure for table `payment_log`
--

DROP TABLE IF EXISTS `payment_log`;
CREATE TABLE IF NOT EXISTS `payment_log` (
  `payment_log_id` int(11) NOT NULL AUTO_INCREMENT,
  `developer_name` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `price` varchar(10) NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;