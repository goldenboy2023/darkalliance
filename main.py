from combat import afficher_statut, afficher_resultat, tour_combat
from personnages import joueur, monstre 

while joueur["pv"] > 0 and monstre["pv"] > 0:
    afficher_statut(joueur)
    afficher_statut(monstre)
    input("\nAppuei sur Entrée pour attaquer ...")
    tour_combat(joueur, monstre)

    afficher_resultat(joueur, monstre)