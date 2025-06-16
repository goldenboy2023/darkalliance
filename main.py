from combat import afficher_statut, afficher_resultat, tour_combat
from personnages import joueur, ennemis 
import random

score = 0
for monstre in ennemis:
    print(f"\n Un {monstre['nom']} approche !")

    while joueur["pv"] > 0 and monstre["pv"] > 0:
        print("\n🧙 Que veux-tu faire ?")
        print("1. Attaquer")
        print("2. Se soigner")
        print("3. Fuir")

        choix = input("> ")
        if choix == "1":
            tour_combat(joueur, monstre)

        elif choix == "2":
            soin = random.randint(10, 25)
            joueur["pv"] = min(joueur["pv"] + soin, 100)
            print(f"\n💊 Tu te soignes de {soin} PV !")

        elif choix == "3":
            print("\n🏃 Tu as fui le combat. Fin de la partie.")
            break

        else:
            print("❌ Choix invalide. Réessaye.")
            continue
        
        afficher_statut(joueur)
        afficher_statut(monstre)
        input("\nAppuei sur Entrée pour attaquer ...")
        tour_combat(joueur, monstre)

    print()

    afficher_resultat(joueur, monstre)

    if joueur["pv"] <= 0:
        print("\n💀 Tu es mort pendant la vague !")
        break
    else:
        print(f"✅ Tu as vaincu le {monstre['nom']} et tu continues à te battre !")
        score += 1


#Message de fin de partie
print("\n🎮 Fin de la partie")
print(f"🏅 Monstres vaincus : {score} / {len(ennemis)}")

if score == len(ennemis):
    print("🌟 Bravo ! Tu as survécu à toutes les vagues !")
else:
    print("💀 Tu as péri avant la fin… mais tu en as bien dézingué !")