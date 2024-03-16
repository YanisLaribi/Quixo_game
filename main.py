"""Jeu Quixo

Ce programme permet de joueur au jeu Quixo.
"""
from api import débuter_partie, jouer_coup, lister_parties
from quixo import (
    analyser_commande,
    formater_jeu,
    formater_les_parties,
    récupérer_le_coup,
)

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = ""


if __name__ == "__main__":
    args = analyser_commande()
    if args.parties:
        parties = lister_parties(args.idul, SECRET)
        print(formater_les_parties(parties))
    else:
        id_partie, joueurs, plateau = débuter_partie(args.idul, SECRET)
        while True:
            # Afficher la partie
            print(formater_jeu(joueurs, plateau))
            # Demander au joueur de choisir son prochain coup
            origine, direction = récupérer_le_coup()
            # Envoyez le coup au serveur
            id_partie, joueurs, plateau = jouer_coup(
                id_partie,
                origine,
                direction,
                args.idul,
                SECRET,
            )
