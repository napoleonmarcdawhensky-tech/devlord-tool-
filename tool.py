from style import *
from modules import option1, option2, option3, option4
from colorama import Fore

while True:
    clear()
    banner()
    menu()

    choix = input(Fore.GREEN + "\nroot@matrix >> ")

    if choix == "1":
        option1.run()
    elif choix == "2":
        option2.run()
    elif choix == "3":
        option3.run()
    elif choix == "4":
        option4.run()
    elif choix == "0":
        print(Fore.GREEN + "\nDéconnexion du système...")
        break
    else:
        print(Fore.GREEN + "Commande inconnue")
        input("Entrée pour continuer...")
