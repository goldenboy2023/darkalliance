import random

def afficher_statut(combattant): 
    print(f"{combattant['nom']} a {combattant['pv']} PV")

def tour_combat(joueur, monstre):
    #Le joueur attaque
    degats = random.randint(5, joueur["Attaque"])
    monstre["pv"] -= degats
    print(f"\n{joueur['nom']} attaque et inflige {degats} dégats !")


    #le monstre riposste si il est encore en vie
    if monstre["pv"] > 0:
        riposte = random.randint(5, monstre["Attaque"])
        joueur["pv"] -= riposte
        print(f"\n{monstre['nom']} riposte et inflige {riposte} a {joueur['nom']}")
    else:
        print(f"{monstre['nom']} est mort")

def afficher_resultat(joueur, monstre):
    if joueur["pv"] <= 0:
        print("\n Tu es mort, le monstre a gagné")
    elif monstre["pv"] <= 0:
        print("\n Tu as vaincu le monstre")
