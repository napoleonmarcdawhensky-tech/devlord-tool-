from colorama import Fore

def run():
    print(Fore.GREEN + "\n[ OPTION 1 ACTIVÉE ]")

    import sys
import threading
import time
import random

data = []

def accumulate_data():
    while True:
        data.append([random.randint(0, 100) for _ in range(50000)])
        time.sleep(0.05)

def heavy_computation():
    try:
        total = 0
        for i in range(len(data)):
            total += len(data[i])
        print("Total:", total)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Erreur:", exc_type, exc_obj)
        print("Numéro d'erreur:", exc_tb.tb_lineno)

def crash():
    raise Exception("CRASH")

def main():
    print("Entrez le numéro de téléphone :")
    num_tel = input()
    print("Vous avez entré :", num_tel)

    threading.Thread(target=accumulate_data).start()

    time.sleep(6)

    print("Déclenchement du traitement lourd...")
    heavy_computation()

    print("Déclenchement du crash...")
    try:
        crash()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Erreur:", exc_type, exc_obj)
        print("Numéro d'erreur:", exc_tb.tb_lineno)
        print("Crashed successfully !")

if __name__ == "__main__":
    main()



    input("\nAppuie sur Entrée pour retour...")
