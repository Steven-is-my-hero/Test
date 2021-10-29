# Initialise un nombre aléatoire
from random import randrange

# Crée les variables 
answer = randrange(0, 100)
number = -1
attempts = 10


#lance une boucle qui ne s'arrêtera que si la réponse est trouvé
while answer != number:
    # Demande a l'utilisateur de saisir un nombre
    try:
        number = int(input("Enter a number between 1 and 100: "))

        attempts -=1
        print("number of remaining attempts:",attempts)

        if attempts ==0:
            print("Purple you noob the answer was",answer) #insulte le joueur si il ne trouve pas en 10 essaie
            break
        elif answer > number:
            print("Higher") # Dit si le nombre est plus petit ou plus grand 
        elif answer < number:
            print("lower")
        elif answer == number:
         print("Congratulation, i m proud of you, you are like a son/daughter to me, you grow so fast") #félicite le joueur si il trouve la réponse
        else:
            print("There is an error somewhere") #ne sert à rien mais on sait jamais
         
    except:
        print("I said a Number dummies") #ne ce lance que si le joueur rentre autre chose qu'un nombre