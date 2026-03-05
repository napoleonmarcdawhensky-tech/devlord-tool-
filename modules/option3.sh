#!/bin/bash

# Vérifier si l'appareil est connecté
if ! adb devices | grep -q "device"; then
  echo "Erreur : appareil non connecté"
  exit 1
fi

# Demander au utilisateur de saisir le numéro de téléphone à signaler
echo "Saisir le numéro de téléphone à signaler : "
read num

# Demander au utilisateur de saisir le nombre de signalements à envoyer par seconde
echo "Saisir le nombre de signalements à envoyer par seconde : "
read rate

# Boucle pour envoyer les signalements
for ((i=0; i<$rate; i++)); do
  # Ouvrir un chat en tapant sur les coordonnées (900, 2200)
  adb shell input tap 900 2200
  
  # Ouvrir le menu en tapant sur les coordonnées (1000, 150)
  adb shell input tap 1000 150
  
  # Faire glisser l'écran vers le bas pour afficher l'option "Signaler"
  adb shell input swipe 500 1000 500 500
  
  # Taper sur l'option "Signaler"
  adb shell input tap 500 800
  
  # Choisir l'option "Compte"
  adb shell input tap 500 1200
  
  # Choisir l'option "Comportement abusif"
  adb shell input tap 500 1400
  
  # Entrer le numéro de téléphone à signaler
  adb shell input text "$num"
  
  # Afficher le numéro de téléphone ciblé
  echo "Numéro de téléphone ciblé : $num"
  
  # Envoyer le signalement en tapant sur les coordonnées (700, 2200)
  adb shell input tap 700 2200
  
  # Afficher le numéro de signalement
  echo "Signalement $i envoyé pour $num"
  
  # Attendre un peu avant de répéter
  sleep 0.001
done
