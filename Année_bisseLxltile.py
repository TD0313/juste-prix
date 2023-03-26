from random import randint

just_price = randint(1,1000)

running = True

while running :

    user_price = int(input("Insérer un prix :"))

    if user_price == just_price :
        prix("Trouvé")
        running = False

    elif user_price > just_price:
        print ("Trop grand")

    elif user_price < just_price :
        print ("Trop petit")

print ("Fin du jeu !")