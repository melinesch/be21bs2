CREATE TABLE `identification` (
  `idUser` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `mail` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `motPasse` varchar(200) NOT NULL,
  `statut` int(2) NOT NULL DEFAULT 1,
  `newMdp` int(2) NOT NULL DEFAULT 2,
  `avatar` varchar(20) NOT NULL DEFAULT '1.png'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `identification`
--

INSERT INTO `identification` (`idUser`, `nom`, `prenom`, `mail`, `login`, `motPasse`, `statut`, `newMdp`, `avatar`) VALUES
(1, 'Blériot', 'Louis', 'louis.bleriot@enac.fr', 'a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 0, 0, '8.png'),
(2, 'Boucher', 'Hélène', 'helene.boucher@enac.fr', 'b', '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d', 1, 0, '3.png'),
(3, 'admin', 'admin', 'admin@enac.fr', 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 0, 0, '10.png'),
(9, 'Ader', 'Clément ', 'clement.ader@enac.fr', 'ader', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '2.png'),
(10, 'Aubrun', 'Émile', 'emile.aubrun@enac.fr', 'aubrun', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '4.png'),
(11, 'Carpentier', 'Roger', 'roger.carpentier@enac.fr', 'carpentier', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '6.png'),
(12, 'Farman', 'Henri', 'henri.farman@enac.fr', 'farman', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '8.png'),
(13, 'Daurat', 'Didier', 'didier.daurat@enac.fr', 'daurat', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '9.png'),
(14, 'Mermoz', 'Jean', 'jean.mermoz@enac.fr', 'mermoz', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '11.png'),
(15, 'Wright', 'Katharine', 'katharine.wright@enac.fr', 'wright', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '1.png'),
(16, 'Peltier', 'Therese', 'therese.peltier@enac.fr', 'peltier', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '3.png'),
(17, 'De Laroche', 'Raymonde', 'raymonde.delaroche@enac.fr', 'delaroche', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '1.png'),
(18, 'Johnson', 'Amy', 'amy.johnson@enac.fr', 'johnson', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '7.png'),
(19, 'Earhart', 'Amelia', 'amelia.earhart@enac.fr', 'earhart', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '11.png'),
(20, 'Tereshkova', 'Valentina', 'valentina.tereshkova@enac.fr', 'tereshkova', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1, 0, '1.png');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `identification`
--
ALTER TABLE `identification`
  ADD PRIMARY KEY (`idUser`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `identification`
--
ALTER TABLE `identification`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;
