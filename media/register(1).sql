-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 08, 2023 at 12:26 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `orgname` varchar(50) DEFAULT NULL,
  `phnnum` bigint(10) DEFAULT NULL,
  `hno` varchar(50) DEFAULT NULL,
  `locality` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `uploadedfile` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`orgname`, `phnnum`, `hno`, `locality`, `district`, `state`, `email`, `password`, `uploadedfile`) VALUES
('9876543210', 12121212, 'hh', 'hhhj', 'hh', 'hhj', '123', '123', NULL),
('abcd', 2147483647, 'hnp', 'djj', 'dist', 'abc', 'abc', '123', NULL),
('maniteja', 2147483647, 'hn', 'Ganeshnagar', 'KNR', 'TS', 'maniteja123', '123', NULL),
('abc', 9876543210, 'hnp', 'djj', 'hhhj', 'TS', 'abc', '123', NULL),
('a', 0, 'a', 'a', 'a', 'a', 'a@gmail.com', 'a', 'no file'),
('a', 0, 'a', 'a', 'a', 'a', 'a', 'a', 'mediaSURPLUS FOOD MANAGEMENT documentation.docx'),
('a', 0, 'a', 'a', 'a', 'a', 'a', 'a', 'mediaSURPLUS FOOD MANAGEMENT documentation.docx'),
('a', 0, 'a', 'a', 'a', 'a', 'a', 'a', 'SURPLUS FOOD MANAGEMENT documentation.docx'),
('a', 0, 'a', 'a', 'a', 'a', 'a', 'a', 'projectadmin.html'),
('abc', 987654321, 'hno', 'a', 'a', 'a', 'abc', 'a', 'SURPLUS FOOD MANAGEMENT documentation.docx'),
('a', 0, 'a', 'a', 'a', 'a', 'a', 'a', 'SURPLUS FOOD MANAGEMENT documentation.docx');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
