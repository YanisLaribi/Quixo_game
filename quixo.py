"""Module Quixo

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_légende - Formater la représentation graphique de la légende.
    * formater_plateau - Formater la représentation graphique du plateau.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
    * récupérer_le_coup - Demander le prochain coup à jouer au joueur.
"""
import argparse


def analyser_commande():
    """Génère un interpréteur de commande.
    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
            Cet objet aura l'attribut «idul» représentant l'idul du joueur
            et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_légende(joueurs):
    """Formater la représentation graphique de la légende.

    Args:
        joueurs (list): Liste des joueurs.

    Returns:
        str: Chaîne de caractères représentant la légende.
    """
    légende = "Légende: "
    for i, joueur in enumerate(joueurs):
        if i == 0:
            légende += "X=" + joueur + ', '

        elif i == 1:
            légende += "O=" + joueur

    return légende


def formater_plateau(plateau):
    """Formater la représentation graphique du plateau.

    Args:
        plateau (list): Liste représentant l'état du plateau.

    Returns:
        str: Chaîne de caractères représentant le plateau.
    """

    plateau_formaté = "   -------------------\n"
    plateau_list = plateau['plateau']

    for i, rangée in enumerate(plateau_list, start=1):
        plateau_formaté += f"{i + 1} | "
        for cellule in rangée:
            plateau_formaté += f"{cellule} | "
            plateau_formaté = plateau_formaté[:-2] + "|\n"

            if i < len(plateau_list):
               plateau_formaté += "  |---|---|---|---|---|\n"

    plateau_formaté += "--|---|---|---|---|---\n"
    plateau_formaté += "  | 1   2   3   4   5\n"


def formater_jeu(joueurs, plateau):
    """Formater la représentation graphique d'un jeu.

    Dois faire usage des fonctions formater_légende et formater_plateau.

    Args:
        joueurs (list): Liste des joueurs.
        plateau (list): Liste représentant l'état du plateau.

    Returns:
        str: Chaîne de caractères représentant le jeu.
    """
    pass


def formater_les_parties(parties):
    """Formater la liste des dernières parties.

    L'ordre doit rester exactement le même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    pass


def récupérer_le_coup():
    """Demander le prochain coup à jouer au joueur.

    Returns:
        tuple: Tuple de 2 éléments composé de l'origine du bloc à déplacer et de sa direction.
            L'origine est une liste de 2 entiers [x, y].
            La direction est une chaîne de caractères.

    Examples:
        Donnez la position d'origine du bloc (x,y) :
        Quelle direction voulez-vous insérer? ('haut', 'bas', 'gauche', 'droite') :
    """
    pass
