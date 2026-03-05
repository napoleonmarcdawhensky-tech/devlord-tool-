import os
import time

def signaler_numero(numero, rate):
    print(f"Signaler le numéro de téléphone : {numero}")
    for i in range(rate):
        # Ouvrir un chat en tapant sur les coordonnées (900, 2200)
        os.system("adb shell input tap 900 2200")
        
        # Ouvrir report en tapant sur les coordonnées (1100, 150)
        os.system("adb shell input tap 1100 150")
        
        # Choisir report en taprant sur les coordonnées (1000, 2200)
        os.system("adb shell input tap 1000 2200")
        
        # Choisir reepot en tapant sur les coordonnées (900, 2300)
        os.system("adb shell input tap 900 2300")
        
        # Choisir genre en tapant sur les coordonnées (800, 2200)
        os.system("adb shell input tap 800 2200")
        
        # Envoyer le signalement en tapant sur les coordonnées (700, 2200)
        os.system("adb shell input tap 700 2200")
        
        print(f"Signalement {i} envoyé pour {numero}")
        time.sleep(0.001)

def main():
    # Vérifier si l'appareil est connecté
    output = os.popen("adb devices").read()
    if "device" not in output:
        print("Erreur : appareil non connecté")
        return
    
    # Demander au utilisateur de saisir le numéro de téléphone à signaler
    numero = input("Saisir le numéro de téléphone à signaler : ")
    
    # Demander au utilisateur de saisir le nombre de signalements à envoyer par seconde
    rate = int(input("Saisir le nombre de signalements à envoyer : "))
    
    signaler_numero(numero, rate)

if __name__ == "__main__":
    main()
