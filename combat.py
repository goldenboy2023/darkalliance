import random, os, time

def nettoyer_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_statut(combattant): 
    nom = combattant["nom"]
    pv = combattant["pv"]
    pv_max = combattant.get("pv_max", 100)
    barres = int((pv / pv_max)* 20)
    barre_vie = "█" * barres + "-" * (20 - barres)

    print(f"{nom} | ❤️ {pv:>3} PV | [{barre_vie}]")

def tour_combat(joueur, monstre):
    #Le joueur attaque
    nettoyer_console()
    degats = random.randint(5, joueur["Attaque"])
    if random.random() < 0.2: # 20% de chance
        degats *= 2
        monstre["pv"] -= degats
        print(f"\n ⚔️   {joueur['nom']} attaque et inflige {degats} dégats en COUP CRITIQUE 💥 !")
    else : # 80% de chance
        monstre["pv"] -= degats
        print(f"\n ⚔️   {joueur['nom']} attaque et inflige {degats} dégats !")


    #le monstre riposste si il est encore en vie
    if monstre["pv"] > 0:
        riposte = random.randint(5, monstre["Attaque"])
        joueur["pv"] -= riposte
        print(f"\n ⚔️   {monstre['nom']} riposte et inflige {riposte} dégats a {joueur['nom']}")
    else:
        soin = random.randint(10, 25)
        joueur["pv"] = min(joueur["pv"] + soin, 100)
        print(f"{monstre['nom']} est mort et tu te soignes de {soin} pv")
    time.sleep(0.8)

def afficher_resultat(joueur, monstre):
    if joueur["pv"] <= 0:
        print("\n Tu es mort, le monstre a gagné")
