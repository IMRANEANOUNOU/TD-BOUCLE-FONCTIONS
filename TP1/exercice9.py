from random import *
def game() :
    n = randint(0,1000)
    print(n)
    user_input = int(input("Entrer un nombre entre 1 et 1000 : "))
    max_essai = 1
    while n!=user_input and max_essai <=8 :
        if user_input > n:
            print("Le nombre rechercher est plus petit")
        else :
            print("Le nombre rechercher est plus grand")
        max_essai=max_essai+1
        user_input = int(input("nouvel essai : "))

    if(user_input == n):
        print("Bravo ! Vous avez trouve la bonne reponse")
        print(f"nombre d'essais : {max_essai}")
    else :
        print("Vous avez perdu , le nombre est : ",n)

game()
