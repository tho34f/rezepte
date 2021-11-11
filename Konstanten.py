# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 07:20:18 2021

@author: thorb
"""

from pathlib import Path

# dropbox-konstanten
droboauth = 'kU34bXLSJfMAAAAAAAAAARLRIV8PFo_6IvKhSysNlTXO9mSDln6fUL-4eseEKmML'
favIcon = Path(__file__).with_name("thorben.ico")
rezeptIcon = Path(__file__).with_name("rezepte.jpg")

# Texte für Lables, Buttons etc.
openingLabel = "Herzlich willkommen bei dieser Anwendung. Diese bietet die Möglichkeit, ein Rezept aus der Dropbox downzuloaden.\n Bitte geben Sie eine Kategorie ein: \n"

categorieNotFound = "Die eingegebene Kategorie konnte nicht gefunden werden. Bitte eine andere Kategorie eingeben!"
searchRezept = "Bitte Geben Sie ein Rezept ein."
uploadRezept = "Bitte Geben Sie ein Rezept für den Upload ein."
