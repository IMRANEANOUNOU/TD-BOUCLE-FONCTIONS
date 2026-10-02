#que calcule ce programe ? -> il calcule l'accumilation de la somme de l'ancienne u avec l'actuelle indice k a la puissance 3 
#pour avoir le resultat direct ? -> supprimer print(u)
#si en remplace k par n ? -> en fait n maintenent est fixee non pas comme k de la dernier version 


n = input("Entrer un entier naturel : ");

n = eval(n)

u=0
for k in range(0,n+1):
    u = u+ k**3
    print(u)

print("Le resultat est : ",u)




