
n = int(input("Entrer un entier : "))
x = int(input("Entrer un reel : "))
res = 0
for i in range(n+1):
    res = res+ i*(x**i)
    print(res)

print(f"resultat est : {res}")
