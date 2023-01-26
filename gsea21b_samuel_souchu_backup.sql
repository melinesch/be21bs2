-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 13 jan. 2023 à 19:09
-- Version du serveur : 10.9.2-MariaDB
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `gsea21b_samuel_souchu`
--

-- --------------------------------------------------------

--
-- Structure de la table `identification`
--

DROP TABLE IF EXISTS `identification`;
CREATE TABLE IF NOT EXISTS `identification` (
  `idUser` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `motPasse` varchar(100) NOT NULL,
  `statut` int(2) NOT NULL,
  `newMdp` int(2) NOT NULL DEFAULT 2,
  `avatar` varchar(20) NOT NULL,
  PRIMARY KEY (`idUser`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `identification`
--

INSERT INTO `identification` (`idUser`, `nom`, `prenom`, `mail`, `login`, `motPasse`, `statut`, `newMdp`, `avatar`) VALUES
(1, 'Blériot', 'Louis', 'louis.bleriot@enac.fr', 'a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 0, 0, '8.png'),
(2, 'Boucher', 'Hélène', 'helene.boucher@enac.fr', 'b', '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d', 1, 0, '3.png'),
(3, 'admin', 'admin', 'admin@enac.fr', 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 0, 2, '10.png'),
(9, 'Ader', 'Clément ', 'clement.ader@enac.fr', 'ader', 'f62ca90d76a18f31c57cf7be34dda1d5e41231bd166df5af54cd64923614591e', 1, 2, '2.png'),
(10, 'Aubrun', 'Émile', 'emile.aubrun@enac.fr', 'aubrun', '568408c44b9cf6e2c90098e120da77bd326d763f001d097885aab178550b80e8', 1, 2, '4.png'),
(11, 'Carpentier', 'Roger', 'roger.carpentier@enac.fr', 'carpentier', '4f2a4028e42489e00b2b83e54aeac205bd1fd481fb93080e97ca14c6269a17b0', 1, 2, '6.png'),
(12, 'Farman', 'Henri', 'henri.farman@enac.fr', 'farman', '8000865d041399d7959d33c1d8d2eb0164382ab2a17ee619ce3abaa2a8fbf7dd', 1, 2, '8.png'),
(13, 'Daurat', 'Didier', 'didier.daurat@enac.fr', 'daurat', '40f36784a9ed4697111f8025e6188b7fc7382968f7ea8a3aba30549378375cf8', 1, 2, '9.png'),
(14, 'Mermoz', 'Jean', 'jean.mermoz@enac.fr', 'mermoz', 'b1a6b90cec01fa40b7e24e100e4882e15ee6aacb3623635842369d1b82e09bec', 1, 2, '11.png'),
(21, 'r', 'r', 'r@r.r', 'r', '454349e422f05297191ead13e21d3db520e5abef52055e4964b82fb213f593a1', 1, 0, '6.png'),
(22, 'v', 'v', 'v@v.v', 'v', '4c94485e0c21ae6c41ce1dfe7b6bfaceea5ab68e40a2476f50208e526f506080', 1, 0, '15.png'),
(23, 'Deroche', 'Elise', 'elisederoche@enac.fr', 'deroche', '68ff2d3fe518d9d73266e033181a0f5debf1dfea0a245e3037d8fbaf51717c5b', 1, 2, '11.png');

-- --------------------------------------------------------

--
-- Structure de la table `vol`
--

DROP TABLE IF EXISTS `vol`;
CREATE TABLE IF NOT EXISTS `vol` (
  `idVol` int(255) NOT NULL AUTO_INCREMENT,
  `aeroclub` varchar(50) NOT NULL,
  `immat` varchar(50) NOT NULL,
  `depart` timestamp NOT NULL DEFAULT current_timestamp(),
  `arrivee` timestamp NOT NULL DEFAULT current_timestamp(),
  `tourpiste` int(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idVol`)
) ENGINE=InnoDB AUTO_INCREMENT=293 DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `vol`
--

INSERT INTO `vol` (`idVol`, `aeroclub`, `immat`, `depart`, `arrivee`, `tourpiste`) VALUES
(141, 'Chavenay_Bertin', 'F-HEJB', '2023-01-09 08:14:00', '2023-01-09 09:14:00', 1),
(142, 'Chavenay_Bertin', 'F-GABJ', '2023-01-09 08:30:00', '2023-01-09 09:30:00', 0),
(143, 'Chavenay_Bertin', 'F-GCUA', '2023-01-09 08:45:00', '2023-01-09 09:45:00', 1),
(144, 'Chavenay_Bertin', 'F-GBUR', '2023-01-09 09:00:00', '2023-01-09 10:00:00', 1),
(145, 'Chavenay_Bertin', 'F-HEJB', '2023-01-09 14:14:00', '2023-01-09 15:15:00', 1),
(146, 'Chavenay_Bertin', 'F-GABJ', '2023-01-09 14:30:00', '2023-01-09 15:30:00', 1),
(147, 'Chavenay_Bertin', 'F-GCUA', '2023-01-09 14:45:00', '2023-01-09 18:45:00', 0),
(148, 'Chavenay_Bertin', 'F-GBUR', '2023-01-09 15:00:00', '2023-01-09 17:30:00', 0),
(149, 'Chavenay_Bertin', 'F-HEJB', '2023-01-10 09:15:00', '2023-01-10 10:15:00', 1),
(150, 'Chavenay_Bertin', 'F-GABJ', '2023-01-10 09:30:00', '2023-01-10 10:30:00', 0),
(151, 'Chavenay_Bertin', 'F-GCUA', '2023-01-10 09:45:00', '2023-01-10 10:45:00', 0),
(152, 'Chavenay_Bertin', 'F-GBUR', '2023-01-10 08:00:00', '2023-01-10 09:00:00', 1),
(153, 'Chavenay_Bertin', 'F-HEJB', '2023-01-10 16:15:00', '2023-01-10 17:15:00', 1),
(154, 'Chavenay_Bertin', 'F-GABJ', '2023-01-10 16:30:00', '2023-01-10 17:30:00', 1),
(155, 'Chavenay_Bertin', 'F-GCUA', '2023-01-10 16:45:00', '2023-01-10 18:45:00', 0),
(156, 'Chavenay_Bertin', 'F-GBUR', '2023-01-10 17:00:00', '2023-01-10 17:45:00', 0),
(157, 'Chavenay_Bertin', 'F-HEJB', '2023-01-11 09:00:00', '2023-01-11 10:00:00', 1),
(158, 'Chavenay_Bertin', 'F-GABJ', '2023-01-11 14:15:00', '2023-01-11 15:15:00', 1),
(159, 'Chavenay_Bertin', 'F-GCUA', '2023-01-11 14:30:00', '2023-01-11 15:30:00', 1),
(160, 'Chavenay_Bertin', 'F-GBUR', '2023-01-11 14:45:00', '2023-01-11 17:45:00', 0),
(161, 'Chavenay_Bertin', 'F-HEJB', '2023-01-11 16:15:00', '2023-01-11 18:00:00', 0),
(162, 'Chavenay_Bertin', 'F-GABJ', '2023-01-11 16:30:00', '2023-01-11 17:00:00', 1),
(163, 'Chavenay_Bertin', 'F-GCUA', '2023-01-11 16:45:00', '2023-01-11 18:45:00', 0),
(164, 'Chavenay_Bertin', 'F-GBUR', '2023-01-11 17:00:00', '2023-01-11 18:00:00', 1),
(165, 'Chavenay_Bertin', 'F-HEJB', '2023-01-12 08:15:00', '2023-01-12 09:15:00', 1),
(166, 'Chavenay_Bertin', 'F-GABJ', '2023-01-12 08:30:00', '2023-01-12 09:30:00', 0),
(167, 'Chavenay_Bertin', 'F-GCUA', '2023-01-12 08:45:00', '2023-01-12 09:45:00', 1),
(168, 'Chavenay_Bertin', 'F-GBUR', '2023-01-12 09:00:00', '2023-01-12 10:00:00', 1),
(169, 'Chavenay_Bertin', 'F-HEJB', '2023-01-10 14:14:00', '2023-01-10 15:14:00', 1),
(170, 'Chavenay_Bertin', 'F-GABJ', '2023-01-12 14:30:00', '2023-01-12 16:30:00', 0),
(171, 'Chavenay_Bertin', 'F-GCUA', '2023-01-12 18:45:00', '2023-01-13 10:45:00', 0),
(172, 'Chavenay_Bertin', 'F-GBUR', '2023-01-12 17:00:00', '2023-01-12 19:30:00', 0),
(173, 'Chavenay_Bertin', 'F-HEJB', '2023-01-13 08:14:00', '2023-01-13 09:14:00', 1),
(174, 'Chavenay_Bertin', 'F-GABJ', '2023-01-13 08:30:00', '2023-01-13 09:30:00', 0),
(175, 'Chavenay_Bertin', 'F-GCUA', '2023-01-13 08:45:00', '2023-01-13 09:45:00', 1),
(176, 'Chavenay_Bertin', 'F-GBUR', '2023-01-13 09:00:00', '2023-01-13 10:00:00', 1),
(177, 'Chavenay_Bertin', 'F-HEJB', '2023-01-13 14:14:00', '2023-01-13 17:15:00', 0),
(178, 'Chavenay_Bertin', 'F-GABJ', '2023-01-13 14:30:00', '2023-01-13 15:30:00', 1),
(179, 'Chavenay_Bertin', 'F-GCUA', '2023-01-13 14:45:00', '2023-01-13 17:45:00', 0),
(180, 'Chavenay_Bertin', 'F-GBUR', '2023-01-13 14:00:00', '2023-01-13 16:30:00', 0),
(181, 'Chavenay_Bertin', 'F-HEJB', '2023-01-14 08:14:00', '2023-01-14 09:14:00', 1),
(182, 'Chavenay_Bertin', 'F-GABJ', '2023-01-14 08:30:00', '2023-01-14 09:30:00', 1),
(183, 'Chavenay_Bertin', 'F-GCUA', '2023-01-14 08:45:00', '2023-01-14 09:45:00', 0),
(184, 'Chavenay_Bertin', 'F-GBUR', '2023-01-14 09:00:00', '2023-01-14 14:00:00', 0),
(185, 'Chavenay_Bertin', 'F-HEJB', '2023-01-10 14:14:00', '2023-01-10 15:14:00', 1),
(186, 'Chavenay_Bertin', 'F-GABJ', '2023-01-14 14:30:00', '2023-01-14 15:30:00', 1),
(187, 'Chavenay_Bertin', 'F-GCUA', '2023-01-14 16:45:00', '2023-01-14 18:45:00', 0),
(188, 'Chavenay_Bertin', 'F-GBUR', '2023-01-14 17:00:00', '2023-01-15 09:30:00', 0),
(189, 'Chavenay_Bertin', 'F-HEJB', '2023-01-15 14:14:00', '2023-01-15 15:15:00', 0),
(190, 'Chavenay_Bertin', 'F-GABJ', '2023-01-15 14:30:00', '2023-01-15 15:30:00', 1),
(191, 'Chavenay_Bertin', 'F-GCUA', '2023-01-15 14:45:00', '2023-01-15 17:45:00', 0),
(192, 'Chavenay_Bertin', 'F-GBUR', '2023-01-15 16:14:00', '2023-01-15 17:14:00', 1),
(193, 'Chavenay_Bertin', 'F-HEJB', '2023-01-15 16:30:00', '2023-01-15 18:30:00', 0),
(194, 'Chavenay_Bertin', 'F-GABJ', '2023-01-15 18:45:00', '2023-01-16 09:15:00', 0),
(195, 'Chavenay_Bertin', 'F-GCUA', '2023-01-15 17:00:00', '2023-01-15 18:30:00', 0),
(196, 'Chavenay_Caudron', 'F-GNJA', '2023-01-09 10:15:00', '2023-01-09 11:15:00', 1),
(197, 'Chavenay_Caudron', 'F-GGXY', '2023-01-09 10:30:00', '2023-01-09 11:30:00', 0),
(198, 'Chavenay_Caudron', 'F-JBZE', '2023-01-09 10:45:00', '2023-01-09 11:45:00', 1),
(199, 'Chavenay_Caudron', 'F-GNJA', '2023-01-09 14:15:00', '2023-01-09 15:15:00', 1),
(200, 'Chavenay_Caudron', 'F-GGXY', '2023-01-09 14:30:00', '2023-01-09 15:30:00', 1),
(201, 'Chavenay_Caudron', 'F-JBZE', '2023-01-09 14:45:00', '2023-01-09 17:45:00', 0),
(202, 'Chavenay_Caudron', 'F-GNJA', '2023-01-10 09:15:00', '2023-01-10 10:15:00', 1),
(203, 'Chavenay_Caudron', 'F-GGXY', '2023-01-10 09:30:00', '2023-01-10 12:30:00', 0),
(204, 'Chavenay_Caudron', 'F-JBZE', '2023-01-10 09:45:00', '2023-01-10 12:45:00', 0),
(205, 'Chavenay_Caudron', 'F-GNJA', '2023-01-10 16:15:00', '2023-01-10 17:15:00', 1),
(206, 'Chavenay_Caudron', 'F-GGXY', '2023-01-10 16:30:00', '2023-01-10 17:30:00', 1),
(207, 'Chavenay_Caudron', 'F-JBZE', '2023-01-10 16:45:00', '2023-01-10 18:45:00', 0),
(208, 'Chavenay_Caudron', 'F-GNJA', '2023-01-11 11:00:00', '2023-01-11 12:00:00', 1),
(209, 'Chavenay_Caudron', 'F-GGXY', '2023-01-11 14:15:00', '2023-01-11 15:15:00', 1),
(210, 'Chavenay_Caudron', 'F-JBZE', '2023-01-11 14:30:00', '2023-01-11 15:30:00', 1),
(211, 'Chavenay_Caudron', 'F-GNJA', '2023-01-11 16:15:00', '2023-01-11 18:00:00', 0),
(212, 'Chavenay_Caudron', 'F-GGXY', '2023-01-11 16:30:00', '2023-01-11 16:30:00', 0),
(213, 'Chavenay_Caudron', 'F-JBZE', '2023-01-11 16:45:00', '2023-01-11 18:45:00', 0),
(214, 'Chavenay_Caudron', 'F-GNJA', '2023-01-12 08:15:00', '2023-01-12 09:15:00', 1),
(215, 'Chavenay_Caudron', 'F-GGXY', '2023-01-12 08:30:00', '2023-01-12 09:30:00', 0),
(216, 'Chavenay_Caudron', 'F-JBZE', '2023-01-12 08:45:00', '2023-01-12 10:45:00', 1),
(217, 'Chavenay_Caudron', 'F-GNJA', '2023-01-10 14:15:00', '2023-01-10 15:15:00', 1),
(218, 'Chavenay_Caudron', 'F-GGXY', '2023-01-12 14:30:00', '2023-01-12 15:30:00', 1),
(219, 'Chavenay_Caudron', 'F-JBZE', '2023-01-12 18:45:00', '2023-01-13 08:45:00', 0),
(220, 'Chavenay_Caudron', 'F-GNJA', '2023-01-13 10:15:00', '2023-01-13 11:15:00', 1),
(221, 'Chavenay_Caudron', 'F-GGXY', '2023-01-13 10:30:00', '2023-01-13 11:30:00', 0),
(222, 'Chavenay_Caudron', 'F-JBZE', '2023-01-13 10:45:00', '2023-01-13 11:45:00', 1),
(223, 'Chavenay_Caudron', 'F-GNJA', '2023-01-13 14:15:00', '2023-01-13 15:15:00', 1),
(224, 'Chavenay_Caudron', 'F-GGXY', '2023-01-13 14:30:00', '2023-01-13 15:30:00', 1),
(225, 'Chavenay_Caudron', 'F-JBZE', '2023-01-13 14:45:00', '2023-01-13 17:45:00', 0),
(226, 'Chavenay_Caudron', 'F-GNJA', '2023-01-14 08:15:00', '2023-01-14 09:15:00', 1),
(227, 'Chavenay_Caudron', 'F-GGXY', '2023-01-14 08:30:00', '2023-01-14 09:30:00', 1),
(228, 'Chavenay_Caudron', 'F-JBZE', '2023-01-14 08:45:00', '2023-01-14 10:45:00', 0),
(229, 'Chavenay_Caudron', 'F-GNJA', '2023-01-10 14:15:00', '2023-01-10 15:15:00', 1),
(230, 'Chavenay_Caudron', 'F-GGXY', '2023-01-14 14:30:00', '2023-01-14 15:30:00', 1),
(231, 'Chavenay_Caudron', 'F-JBZE', '2023-01-14 16:45:00', '2023-01-14 18:45:00', 0),
(232, 'Chavenay_Caudron', 'F-GNJA', '2023-01-15 14:15:00', '2023-01-15 15:15:00', 0),
(233, 'Chavenay_Caudron', 'F-GGXY', '2023-01-15 14:30:00', '2023-01-15 15:30:00', 1),
(234, 'Chavenay_Caudron', 'F-JBZE', '2023-01-15 14:45:00', '2023-01-15 17:45:00', 0),
(235, 'Chavenay_Caudron', 'F-GNJA', '2023-01-15 16:30:00', '2023-01-15 18:30:00', 0),
(236, 'Chavenay_Caudron', 'F-GGXY', '2023-01-15 18:45:00', '2023-01-16 08:15:00', 0),
(237, 'Chavenay_Caudron', 'F-JBZE', '2023-01-15 17:00:00', '2023-01-15 18:30:00', 0),
(238, 'Chavenay_Renault', 'F-BOFY', '2023-01-09 07:15:00', '2023-01-09 09:15:00', 0),
(239, 'Chavenay_Renault', 'F-BXRY', '2023-01-09 07:30:00', '2023-01-09 08:30:00', 1),
(240, 'Chavenay_Renault', 'F-GSBN', '2023-01-09 07:45:00', '2023-01-09 09:45:00', 0),
(241, 'Chavenay_Renault', 'F-GNNY', '2023-01-09 09:00:00', '2023-01-09 12:00:00', 0),
(242, 'Chavenay_Renault', 'F-BOFY', '2023-01-09 14:15:00', '2023-01-09 15:15:00', 1),
(243, 'Chavenay_Renault', 'F-BXRY', '2023-01-09 14:30:00', '2023-01-09 15:30:00', 1),
(244, 'Chavenay_Renault', 'F-GSBN', '2023-01-09 14:45:00', '2023-01-09 18:45:00', 0),
(245, 'Chavenay_Renault', 'F-GNNY', '2023-01-09 15:00:00', '2023-01-09 17:00:00', 1),
(246, 'Chavenay_Renault', 'F-BOFY', '2023-01-10 09:15:00', '2023-01-10 11:15:00', 0),
(247, 'Chavenay_Renault', 'F-BXRY', '2023-01-10 09:30:00', '2023-01-10 10:30:00', 1),
(248, 'Chavenay_Renault', 'F-GSBN', '2023-01-10 09:45:00', '2023-01-10 10:45:00', 1),
(249, 'Chavenay_Renault', 'F-GNNY', '2023-01-10 07:00:00', '2023-01-10 09:00:00', 0),
(250, 'Chavenay_Renault', 'F-BOFY', '2023-01-10 15:15:00', '2023-01-10 16:15:00', 1),
(251, 'Chavenay_Renault', 'F-BXRY', '2023-01-10 15:30:00', '2023-01-10 17:30:00', 0),
(252, 'Chavenay_Renault', 'F-GSBN', '2023-01-10 16:45:00', '2023-01-10 18:45:00', 0),
(253, 'Chavenay_Renault', 'F-GNNY', '2023-01-10 17:00:00', '2023-01-10 17:45:00', 0),
(254, 'Chavenay_Renault', 'F-BOFY', '2023-01-11 09:00:00', '2023-01-11 10:00:00', 1),
(255, 'Chavenay_Renault', 'F-BXRY', '2023-01-11 14:15:00', '2023-01-11 15:15:00', 1),
(256, 'Chavenay_Renault', 'F-GSBN', '2023-01-11 14:30:00', '2023-01-11 15:30:00', 1),
(257, 'Chavenay_Renault', 'F-GNNY', '2023-01-11 14:45:00', '2023-01-11 17:45:00', 0),
(258, 'Chavenay_Renault', 'F-BOFY', '2023-01-11 16:15:00', '2023-01-11 18:00:00', 0),
(259, 'Chavenay_Renault', 'F-BXRY', '2023-01-11 15:30:00', '2023-01-11 16:00:00', 1),
(260, 'Chavenay_Renault', 'F-GSBN', '2023-01-11 16:45:00', '2023-01-11 18:45:00', 0),
(261, 'Chavenay_Renault', 'F-GNNY', '2023-01-11 17:00:00', '2023-01-11 18:00:00', 1),
(262, 'Chavenay_Renault', 'F-BOFY', '2023-01-12 07:15:00', '2023-01-12 09:15:00', 1),
(263, 'Chavenay_Renault', 'F-BXRY', '2023-01-12 07:30:00', '2023-01-12 09:30:00', 0),
(264, 'Chavenay_Renault', 'F-GSBN', '2023-01-12 07:45:00', '2023-01-12 09:45:00', 1),
(265, 'Chavenay_Renault', 'F-GNNY', '2023-01-12 09:00:00', '2023-01-12 10:00:00', 1),
(266, 'Chavenay_Renault', 'F-BOFY', '2023-01-10 14:15:00', '2023-01-10 15:15:00', 1),
(267, 'Chavenay_Renault', 'F-BXRY', '2023-01-12 14:30:00', '2023-01-12 16:30:00', 0),
(268, 'Chavenay_Renault', 'F-GSBN', '2023-01-12 18:45:00', '2023-01-13 08:30:00', 0),
(269, 'Chavenay_Renault', 'F-GNNY', '2023-01-12 17:00:00', '2023-01-13 08:30:00', 0),
(270, 'Chavenay_Renault', 'F-BOFY', '2023-01-13 07:15:00', '2023-01-13 08:15:00', 1),
(271, 'Chavenay_Renault', 'F-BXRY', '2023-01-13 07:30:00', '2023-01-13 09:30:00', 0),
(272, 'Chavenay_Renault', 'F-GSBN', '2023-01-13 07:45:00', '2023-01-13 08:45:00', 1),
(273, 'Chavenay_Renault', 'F-GNNY', '2023-01-13 09:00:00', '2023-01-13 10:00:00', 1),
(274, 'Chavenay_Renault', 'F-BOFY', '2023-01-13 14:15:00', '2023-01-13 16:15:00', 0),
(275, 'Chavenay_Renault', 'F-BXRY', '2023-01-13 14:30:00', '2023-01-13 15:30:00', 1),
(276, 'Chavenay_Renault', 'F-GSBN', '2023-01-13 14:45:00', '2023-01-13 17:45:00', 0),
(277, 'Chavenay_Renault', 'F-GNNY', '2023-01-13 14:00:00', '2023-01-13 16:30:00', 0),
(278, 'Chavenay_Renault', 'F-BOFY', '2023-01-14 07:15:00', '2023-01-14 08:15:00', 1),
(279, 'Chavenay_Renault', 'F-BXRY', '2023-01-14 07:30:00', '2023-01-14 08:30:00', 1),
(280, 'Chavenay_Renault', 'F-GSBN', '2023-01-14 07:45:00', '2023-01-14 09:45:00', 0),
(281, 'Chavenay_Renault', 'F-GNNY', '2023-01-14 09:00:00', '2023-01-14 14:00:00', 0),
(282, 'Chavenay_Renault', 'F-BOFY', '2023-01-10 14:15:00', '2023-01-10 15:15:00', 1),
(283, 'Chavenay_Renault', 'F-BXRY', '2023-01-14 14:30:00', '2023-01-14 15:30:00', 1),
(284, 'Chavenay_Renault', 'F-GSBN', '2023-01-14 16:45:00', '2023-01-14 17:45:00', 0),
(285, 'Chavenay_Renault', 'F-GNNY', '2023-01-14 17:00:00', '2023-01-15 08:30:00', 0),
(286, 'Chavenay_Renault', 'F-BOFY', '2023-01-15 14:15:00', '2023-01-15 15:15:00', 0),
(287, 'Chavenay_Renault', 'F-BXRY', '2023-01-15 14:30:00', '2023-01-15 15:30:00', 1),
(288, 'Chavenay_Renault', 'F-GSBN', '2023-01-15 14:45:00', '2023-01-15 16:45:00', 0),
(289, 'Chavenay_Renault', 'F-GNNY', '2023-01-15 16:15:00', '2023-01-15 17:15:00', 1),
(290, 'Chavenay_Renault', 'F-BOFY', '2023-01-15 16:30:00', '2023-01-15 18:30:00', 0),
(291, 'Chavenay_Renault', 'F-BXRY', '2023-01-15 18:45:00', '2023-01-16 09:15:00', 0),
(292, 'Chavenay_Renault', 'F-GSBN', '2023-01-15 17:00:00', '2023-01-15 18:00:00', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
