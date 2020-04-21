-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2020 at 08:06 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `amazon`
--

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `order_id` char(6) DEFAULT NULL,
  `product_id` char(6) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `product_detail` varchar(50) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `client_name` varchar(100) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `weight_kg` float DEFAULT NULL,
  `date_time` datetime DEFAULT NULL,
  `special_req` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`order_id`, `product_id`, `product_name`, `product_detail`, `quantity`, `address`, `client_name`, `phone_no`, `weight_kg`, `date_time`, `special_req`) VALUES
('200110', '888173', 'Sony PlayStation 4', 'Slim 1TB, White', 1, 'Hong Kong, Tuen Mun, Yau Oi Estate', 'Mr. Wong', '63829172', 3, '2020-02-18 14:22:15', 'Afternoon reception'),
('200110', '888174', 'Hydro Flask Standard Mouth Water Bottle', '', 2, 'Hong Kong, Mongkok, Pak Po Estate', 'Calvin', '94536657', 0.5, '2020-02-20 00:35:02', ''),
('200110', '888175', 'Shure SE215', 'Sound Isolating Earphones', 1, 'Hong Kong, Wong Tai Sin, Upper Wong Tai Sin Estate', 'Mrs. Ng', '62926601', 0.2, '2020-02-20 14:24:15', 'Weekend reception'),
('200111', '888176', 'Ryu Ga Gotoku 3 [Japan Import]', '', 4, 'Hong Kong, Yeun Long, Yoho Mall', 'Ms. Pang', '93715621', 0.2, '2020-02-21 19:37:59', ''),
('200111', '888177', 'Nintendo Switch', 'Neon Blue and Neon Red,Console', 1, 'Hong Kong, Tin Shui Wai, Tin Yat Estate', 'Mr. Chan', '91730789', 0.4, '2020-02-21 09:28:26', ''),
('200112', '888178', 'Apple iPad Mini', 'Wi-Fi,64GB,SpaceGray', 1, 'Hong Kong, Wong Tai Sin , Chuk Yuen North Estate', 'Mr Lai', '61241124', 0.5, '2020-02-22 15:35:24', 'Weekday reception');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
