# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:09:20 2021

@author: thorb
"""

kategorien = []
rezepte = []


def fillKategorie(db):
    kategorien.clear()
    response = db.files_list_folder('')
    for file in response.entries:
        kategorien.append(file.name)


def fillRezepte(db, kategorieName):
    rezepte.clear()
    response = db.files_list_folder('/' + kategorieName)
    for file in response.entries:
        rezepte.append(file.name)


def showKategorieSelection(gui):
    gui.frameSelectionKategorie.pack(padx=10, pady=10)
    gui.kategorieNameInput.grid(row=2, column=0, columnspan=10, padx=100)
    gui.selectionLabelKategorie.grid(row=0, column=0, columnspan=10, padx=100)


def forgetFrameOne(gui):
    gui.frameAccountInformation.pack_forget()
    gui.frameUploadRezepte.pack_forget()
    gui.frameInformationNotFound.pack_forget()
    gui.frameCreateKategorie.pack_forget()


def forgetFrameTwo(gui):
    gui.frameSelectionRezepte.pack_forget()
    gui.frameInformationNotFound.pack_forget()
    gui.frameInformationFound.pack_forget()
    gui.frameCreateKategorie.pack_forget()


def check_kategorie(kategorieName):
    """ Gewählte Kategorie prüfen """
    for kategorie in kategorien:
        if kategorieName == kategorie:
            return True
    return False
