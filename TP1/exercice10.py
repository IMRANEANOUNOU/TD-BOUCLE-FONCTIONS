def factorielle(n) :
    if(n == 0):
        return 1
    else :
        return n*factorielle(n-1)


def approx(epsi):
    n = 0
    u = 1

    while 3 / factorielle(n) >= epsi:
        n += 1
        u += 1 / factorielle(n)

    return u

print(approx(0.001))
