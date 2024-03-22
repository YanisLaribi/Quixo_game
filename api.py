"""Module d'API du jeu Quixo

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * lister_parties - Récupérer la liste des parties reçus du serveur.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * récupérer_partie - Retrouver l'état d'une partie spécifique.
    * jouer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""
import requests

URL = "https://pax.ulaval.ca/quixo/api/h24/"


def lister_parties(idul, secret):
    """Lister les parties

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        list: Liste des parties reçues du serveur,
             après avoir décodé le json de sa réponse.
    """
    rep = requests.get(URL + "parties/", auth = (idul, secret))
    
    if rep.status_code == 200:
       list = rep.json()
       parties = list.get('parties')
       return(parties)
    
    elif rep.status_code == 401:

       raise PermissionError(rep.json()["message"])

    elif rep.status_code == 406:

       raise RuntimeError(rep.json()["message"])
    
    else : 
        raise ConnectionError
    

def débuter_partie(idul, secret):
    """Débuter une partie

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple de 3 éléments constitué de l'identifiant de la partie en cours,
            de la liste des joueurs et de l'état du plateau.
    """
    rep = requests.post(URL + "partie/", auth = (idul, secret))

    if rep.status_code == 200:
        tupl = rep.json()

        identifiant = tupl.get('id')
        liste_joueur = tupl.get('état').get('joueurs')
        état_du_plateau = tupl.get('état')

        return identifiant, liste_joueur, état_du_plateau
    
    elif rep.status_code == 401:
       raise PermissionError(rep.json()["message"])

    elif rep.status_code == 406:
       raise RuntimeError(rep.json()["message"])
    
    else : 
        raise ConnectionError


def récupérer_partie(id_partie, idul, secret):
    """Récupérer une partie

    Args:
        id_partie (str): identifiant de la partie à récupérer
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple de 4 éléments constitué de l'identifiant de la partie en cours,
            de la liste des joueurs, de l'état du plateau et du vainqueur.
    """
    url = f"https://pax.ulaval.ca/quixo/api/h24/partie/{id_partie}"
    rep = requests.get(url, auth = (idul, secret))

    if rep.status_code == 200:

        tupl = rep.json()

        identifiant = tupl.get('id')
        liste_joueur = tupl.get('état').get('joueurs')
        état_du_plateau = tupl.get('état')
        vainqueur = tupl.get('gagnant')

        return identifiant, liste_joueur, état_du_plateau, vainqueur
    
    elif rep.status_code == 401:
       raise PermissionError(rep.json()["message"])

    elif rep.status_code == 406:
       raise RuntimeError(rep.json()["message"])
    
    else : 
        raise ConnectionError


def jouer_coup(id_partie, origine, direction, idul, secret):
    """Jouer un coup

    Args:
        id_partie (str): Identifiant de la partie.
        origine (list): La position [x, y] du bloc à déplacer.
        direction (str): La direction du déplacement du bloc.:
            'haut': Déplacement d'un bloc du bas pour l'insérer en haut.
            'bas': Déplacement d'un bloc du haut pour l'insérer en bas.
            'gauche': Déplacement d'un bloc de droite pour l'insérer à gauche,
            'droite': Déplacement d'un bloc de gauche pour l'insérer à droite,
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        StopIteration: Erreur levée lorsqu'il y a un gagnant dans la réponse du serveur.
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        tuple: Tuple de 3 éléments constitué de l'identifiant de la partie en cours,
            de la liste des joueurs et de l'état du plateau.
    """
    rep = requests.put(URL + "jouer/", auth = (idul, secret))
    if rep.status_code == 200:
        partie_data = rep.json()
        partie_id = partie_data.get('id')
        joueurs = partie_data.get('état').get('joueurs')
        plateau = partie_data.get('état').get('plateau')
        return partie_id, joueurs, plateau
    
    elif rep.status_code == 200 and rep.json().get('gagnant'):
        raise StopIteration(f"{rep.json().get('gagnant')}")
    
    elif rep.status_code == 401:
       raise PermissionError(rep.json()["message"])

    elif rep.status_code == 406:
       raise RuntimeError(rep.json()["message"])
    
    else : 
        raise ConnectionError
    
