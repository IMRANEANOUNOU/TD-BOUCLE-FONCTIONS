# n = int(input("donner moi les nombre des notes : "))
# s = 0
# for i in range(n):
#     m = int(input(f"note {i+1} : "))
#     if(m>=0 and m<=20):
#         s = s + m
#     else :
#         print("invalide input !")
#         break
# 
# print(f"Le moyenne est : {s/n}")
#     
n = int(input("Donner le nombre de notes : "))
somme = 0

if n <= 0:
    print("Le nombre de notes doit etre positif.")
else:
    notes_valides = True
    for i in range(n):
        note = float(input(f"Note {i + 1} : "))
        if 0 <= note <= 20:
            somme += note
        else:
            print("Entrée invalide ! Une note doit être entre 0 et 20.")
            notes_valides = False
            break

    if notes_valides:
        print("La moyenne est :", somme / n)
