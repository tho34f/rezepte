# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:09:20 2021

@author: thorb
"""

import Konstanten


def check_kategorie(gui):
    """ Gewählte Kategorie prüfen """
    kategorieName = gui.kategorieNameInput.get()
    for kategorie in Konstanten.kategorien:
        if kategorieName == kategorie:
            return True
    return False
