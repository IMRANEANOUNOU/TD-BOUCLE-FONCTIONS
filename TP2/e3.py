# s = 0
# n = 0
# 
# while True:
#     x = input("Entrez un nombre ou stop : ")
#     if x == "stop":
#         break
#     x = int(x)
#     s = s + x
#     n = n + 1
# 
# if n > 0:
#     print("Moyenne :", s / n)
# else:
#     print("Aucun nombre saisi")

#modification pour la questions b
s = 0
n = 0

while True:
    x = input("Entrez un nombre entre 0 et 20 ou stop : ")
    if x == "stop":
        break
    x = int(x)

    while x < 0 or x > 20:
        x = int(input("Entrez un nombre entre 0 et 20 : "))

    s = s + x
    n = n + 1

if n > 0:
    print("Moyenne :", s / n)
else:
    print("Aucun nombre saisi")     
