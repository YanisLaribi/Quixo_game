"""Tests Quixo

Ce module contient des tests unitaires pour le projet Quixo.
"""
from quixo import formater_plateau, formater_jeu, formater_légende


def test_formater_légende():
    joueurs = ["josmi42", "automate"]

    attendu = (
        "Légende: X=josmi42, O=automate\n"
    )

    résultat = formater_légende(joueurs)

    assert résultat == attendu, "Échec du test de formater_légende"


def test_formater_plateau_pour_une_nouvelle_partie():
    plateau = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
    ]

    attendu = (
        "   -------------------\n"
        "1 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "2 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "3 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "4 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "5 |   |   |   |   |   |\n"
        "--|---|---|---|---|---\n"
        "  | 1   2   3   4   5\n"
    )

    résultat = formater_plateau(plateau)

    assert résultat == attendu, "Échec du test de formater_plateau pour une nouvelle partie"


def test_formater_jeu_pour_une_nouvelle_partie():
    joueurs = ["josmi42", "automate"]
    plateau = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
    ]

    attendu = (
        "Légende: X=josmi42, O=automate\n"
        "   -------------------\n"
        "1 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "2 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "3 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "4 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "5 |   |   |   |   |   |\n"
        "--|---|---|---|---|---\n"
        "  | 1   2   3   4   5\n"
    )

    résultat = formater_jeu(joueurs, plateau)

    assert résultat == attendu, "Échec du test de formater_jeu pour une nouvelle partie"


def test_formater_jeu_pour_une_partie_avancée():
    joueurs = ["josmi42", "automate"]
    plateau = [
        [" ", " ", "X", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "O"],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
    ]

    attendu = (
        "Légende: X=josmi42, O=automate\n"
        "   -------------------\n"
        "1 |   |   | X |   |   |\n"
        "  |---|---|---|---|---|\n"
        "2 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "3 |   |   |   |   | O |\n"
        "  |---|---|---|---|---|\n"
        "4 |   |   |   |   |   |\n"
        "  |---|---|---|---|---|\n"
        "5 |   |   |   |   |   |\n"
        "--|---|---|---|---|---\n"
        "  | 1   2   3   4   5\n"
    )

    résultat = formater_jeu(joueurs, plateau)

    assert résultat == attendu, "Échec du test de formater_jeu pour une partie avancée"



if __name__ == "__main__":
    test_formater_légende()
    print("Test de formater_légende pour une nouvelle partie réussi")
    test_formater_plateau_pour_une_nouvelle_partie()
    print("Test de formater_plateau pour une nouvelle partie réussi")
    test_formater_jeu_pour_une_nouvelle_partie()
    print("Test de formater_jeu pour une nouvelle partie réussi")
    test_formater_jeu_pour_une_partie_avancée()
    print("Test de formater_jeu pour une partie avancée réussi")
