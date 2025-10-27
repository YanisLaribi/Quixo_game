# Quixo – Jeu interactif en ligne (Projet universitaire python)

<img src="https://pax.ulaval.ca/static/GLO-1901/images/quixo.jpg" style="display: block; margin-left: auto; margin-right: auto;" alt="Quixo" width="50%" height="auto">

Quixo est une application Python qui permet de jouer au jeu de stratégie Quixo sur la ligne de commande, avec une implémentation basée sur des appels API, une gestion du plateau et des parties, ainsi que des outils pour automatiser les tests et la manipulation du jeu. Ce projet combine l’interaction directe via le terminal et l’intégration avec un serveur distant.

## Fonctionnalités

- Création et gestion de parties Quixo via une API tierce.
- Interface en ligne de commande permettant :
    - Démarrer une partie.
    - Jouer un coup et suivre la progression du jeu.
    - Lister et consulter les parties existantes.
    - Afficher le plateau et la légende du jeu en temps réel.
- Modules pour formater et gérer les éléments du jeu (plateau, parties, coups).
- Suite de tests automatisés pour valider le fonctionnement des principaux modules.
- Documentation dans le code pour faciliter la prise en main et l’extension.

## Structure du projet

- `main.py` : Point d'entrée principal, gère l’interaction avec l’utilisateur et orchestre le déroulement du jeu Quixo.
- `api.py` : Module d’interfaçage avec le serveur ; permet de lister, créer, récupérer et modifier des parties par appels REST sécurisés.
- `quixo.py` : Fonctions utilitaires pour la structure et la représentation graphique du jeu, l’analyse des commandes, la gestion des joueurs et du plateau.
- `tests.py` : Tests unitaires sur les fonctions clés de formatage et de manipulation du jeu Quixo.
- `file.gitignore` : Liste des fichiers à ignorer pour la gestion des versions.
