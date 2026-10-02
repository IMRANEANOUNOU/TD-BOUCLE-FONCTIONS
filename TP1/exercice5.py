def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

x = int(input("Entrer un entier naturel : "))
if x < 0:
    print("La factorielle n'est définie ici que pour n >= 0.")
else:
    print(f"{x}! = {factorielle(x)}")
