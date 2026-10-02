def terme(n):
    u = 1

    for k in range(n):
        u = u / (u + 1)

    return u

print(terme(0)) 




# Un = 1/n+1
