from random import randint

nombre = randint(1, 100)
essais = 10

while essais > 0:
    choix = int(input("Tentez de deviner un nombre entre 1 et 100 (essais restants: " + str(essais) + "): "))

    if choix == nombre:
        print("Bravo, vous avez trouvé le nombre !")
        break
    elif choix < nombre:
        print("Raté, le nombre à trouver est plus grand")
    else:
        print("Raté, le nombre à trouver est plus petit")

    essais = essais - 1

if essais == 0:
    print("Vous avez perdu, le nombre à trouver était", nombre)
