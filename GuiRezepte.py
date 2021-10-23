# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:01:38 2021

@author: thorb
"""
from tkinter import Label, LabelFrame, Entry, Button, Menu, END
from PIL import ImageTk, Image
import Konstanten


class GUI:

    def __init__(self, master, title):
        self.master = master
        master.title(title)
        # BenötigteFotos
        master.iconbitmap(Konstanten.favIcon)
        self.my_image = ImageTk.PhotoImage(Image.open(Konstanten.rezeptIcon))
        self.my_label_image = Label(master, image=self.my_image)
        self.my_label_image.place(x=0, y=0, relwidth=1, relheight=1)
        # BenötigteFrames
        self.frameSelectionKategorie = LabelFrame(master, text="Kategorie wählen", padx=10, pady=10)
        self.frameSelectionRezepte = LabelFrame(master, text="Rezept Suche", padx=10, pady=10)
        self.frameUploadRezepte = LabelFrame(master, text="Rezept Upload", padx=10, pady=10)
        self.frameInformationFound = LabelFrame(master, text="Erfolgsmeldung", padx=10, pady=10)
        self.frameInformationNotFound = LabelFrame(master, text="Fehlermeldung", padx=10, pady=10)
        self.frameAccountInformation = LabelFrame(master, text="Account-Informationen", padx=10, pady=10)
        # Ein Eingabefeld zur Eingabe einer Kategorie bzw. eines Rezeptnamens erstellen
        self.rezeptNameInput = Entry(self.frameSelectionRezepte, width=75, borderwidth=10)
        self.kategorieNameInput = Entry(self.frameSelectionKategorie, width=75, borderwidth=10)
        # Labels
        self.selectionLabelKategorie = Label(self.frameSelectionKategorie, text=Konstanten.opiningLabel)
        self.selectionLabelKategorieNotFound = Label(self.frameInformationNotFound, text=Konstanten.categorieNotFound)
        self.selectionLabelRezept = Label(self.frameSelectionRezepte, text=Konstanten.searchRezept)
        self.uploadLabelRezept = Label(self.frameUploadRezepte, text=Konstanten.uploadRezept)
        # Buttons
        # Menü
        self.menu = Menu(master)
        self.filemenu = Menu(self.menu)
        master.config(menu=self.menu)
        self.menu.add_cascade(label="Datei", menu=self.filemenu)
