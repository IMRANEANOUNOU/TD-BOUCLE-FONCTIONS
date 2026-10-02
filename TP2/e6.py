from random import randint

choix = ["pierre", "papier", "ciseaux"]
victoires = 0
defaites = 0
nuls = 0

while True:
    joueur = input("Pierre, papier ou ciseaux (stop pour arrêter) : ").lower()

    while joueur not in choix and joueur != "stop":
        joueur = input("Choix invalide. Réessayez : ").lower()

    if joueur == "stop":
        break

    ordinateur = choix[randint(0, 2)]
    print("Ordinateur :", ordinateur)

    if joueur == ordinateur:
        nuls = nuls + 1
    elif (joueur == "pierre" and ordinateur == "ciseaux") or (joueur == "papier" and ordinateur == "pierre") or (joueur == "ciseaux" and ordinateur == "papier"):
        victoires = victoires + 1
    else:
        defaites = defaites + 1

print(victoires, "victoires,", defaites, "défaites et", nuls, "matchs nuls")
