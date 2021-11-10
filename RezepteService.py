# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:09:20 2021

@author: thorb
"""

kategorien = []


def fillKategorie(db):
    kategorien.clear()
    response = db.files_list_folder('')
    for file in response.entries:
        kategorien.append(file.name)


def check_kategorie(gui):
    """ Gewählte Kategorie prüfen """
    kategorieName = gui.kategorieNameInput.get()
    for kategorie in kategorien:
        if kategorieName == kategorie:
            return True
    return False
