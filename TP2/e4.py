def racine_cubique(n):
    if n < 0:
        return -racine_cubique(-n)

    i = 0
    while (i + 1) ** 3 <= n:
        i = i + 1
    return i

def est_cube(n):
    return racine_cubique(n) ** 3 == n

print(racine_cubique(-29))
print(est_cube(-27))
print(est_cube(-4))
