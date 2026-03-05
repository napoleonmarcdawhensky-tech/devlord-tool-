import os
import random
import time

def generer_num():
    return ''.join(random.choice('0123456789') for _ in range(10))

def envoyer_message(num):
    message = "Ceci est un message automatique"
    os.system(f"adb shell am broadcast -a android.intent.action.SEND -d 'sms:{num}' -e 'sms_body' '{message}'")

def main():
    # Demander au utilisateur de saisir le numéro de téléphone à cibler
    num = input("Saisir le numéro de téléphone à cibler : ")

    # Boucle pour envoyer des messages en masse
    for i in range(10000):
        # Envoyer le message ciblé au numéro précisé
        message = "Vous êtes ciblés !"
        os.system(f"adb shell am broadcast -a android.intent.action.SEND -d 'sms:{num}' -e 'sms_body' '{message}'")
        print(f"Message ciblé envoyé à {num}")

        # Ensuite, spamme avec les numéros générés
        num_genere = generer_num()
        envoyer_message(num_genere)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
