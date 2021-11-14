# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 07:01:38 2021

@author: thorb
"""
from tkinter import Label, LabelFrame, Entry, Menu
from PIL import ImageTk, Image
import Konstanten


class GUI:

    def __init__(self, master, title, kategorieChooseLabelText):
        self.master = master
        master.title(title)
        # BenötigteFotos
        master.iconbitmap(Konstanten.favIcon)
        self.my_image = ImageTk.PhotoImage(Image.open(Konstanten.rezeptIcon))
        self.my_label_image = Label(master, image=self.my_image)
        self.my_label_image.place(x=0, y=0, relwidth=1, relheight=1)
        # BenötigteFrames
        self.frameOpening = LabelFrame(master, text="Begrüßung", padx=10, pady=10)
        self.frameSelectionKategorie = LabelFrame(master, text="Kategorie wählen", padx=10, pady=10)
        self.frameSelectionRezepte = LabelFrame(master, text="Rezept Suche", padx=10, pady=10)
        self.frameUploadRezepte = LabelFrame(master, text="Rezept Upload", padx=10, pady=10)
        self.frameInformationFound = LabelFrame(master, text="Erfolgsmeldung Rezept-Download", padx=10, pady=10)
        self.frameInformationNotFound = LabelFrame(master, text="Fehlermeldung Rezept-Download", padx=10, pady=10)
        self.frameInformationUpload = LabelFrame(master, text="Erfolgsmeldung Rezept-Upload", padx=10, pady=10)
        self.frameInformationNotUpload = LabelFrame(master, text="Fehlermeldung Rezept-Upload", padx=10, pady=10)
        self.frameAccountInformation = LabelFrame(master, text="Account-Informationen", padx=10, pady=10)
        self.frameCreateKategorie = LabelFrame(master, text="Kategorie erstellen", padx=10, pady=10)
        # Ein Eingabefeld zur Eingabe einer Kategorie bzw. eines Rezeptnamens erstellen
        self.rezeptNameInput = Entry(self.frameSelectionRezepte, width=75, borderwidth=10)
        self.rezeptNameInputUpload = Entry(self.frameUploadRezepte, width=75, borderwidth=10)
        self.kategorieNameInput = Entry(self.frameSelectionKategorie, width=75, borderwidth=10)
        self.createKategorieNameInput = Entry(self.frameCreateKategorie, width=75, borderwidth=10)
        # Labels
        self.openingLabel = Label(self.frameOpening, text=Konstanten.openingLabel)
        self.selectionLabelKategorie = Label(self.frameSelectionKategorie, text=kategorieChooseLabelText)
        self.selectionLabelKategorieNotFound = Label(self.frameInformationNotFound, text=Konstanten.categorieNotFound)
        self.uploadLabelRezept = Label(self.frameUploadRezepte, text=Konstanten.uploadRezept)
        self.createLabelKategorie = Label(self.frameCreateKategorie, text=Konstanten.createNewKategorie)
        self.information_upload_label = Label(self.frameInformationUpload, text=Konstanten.uploadNotError)
        self.information_upload_Error_label = Label(self.frameInformationNotUpload, text=Konstanten.uploadError)
        self.information_upload_Error_Ending_label = Label(self.frameInformationNotUpload, text=Konstanten.uploadErrorEnding)
        # Buttons
        # Menü
        self.menu = Menu(master)
        self.filemenu = Menu(self.menu)
        master.config(menu=self.menu)
        self.menu.add_cascade(label="Datei", menu=self.filemenu)
