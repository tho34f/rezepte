# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 08:24:14 2021

@author: thorb
"""
import getpass
from tkinter import Tk, Label, Button, END, filedialog
import GuiRezepte
import dropbox
import RezepteService
import Konstanten

db = dropbox.Dropbox(Konstanten.droboauth)
RezepteService.fillKategorie(db)

# Texte für Labels
kategorieChooseLabelText = Konstanten.kategorieChooseLabel
numberOfKategorien = RezepteService.kategorien.__len__()
for i in range(0, numberOfKategorien):
    name = RezepteService.kategorien.__getitem__(i)
    i = i + 1
    kategorieChooseLabelText = kategorieChooseLabelText + " " + str(i) + ") " + name
    if i % 5 == 0:
        kategorieChooseLabelText = kategorieChooseLabelText + "\n "

# Ein Fenster und Den Fenstertitle erstellen
fenster = Tk()
rezepte_gui = GuiRezepte.GUI(fenster, "Rezepte", kategorieChooseLabelText)
rezepte_gui.my_label_image.place(x=0, y=0, relwidth=1, relheight=1)

# Main-Frame anzeigen
rezepte_gui.frameOpening.pack(padx=10, pady=10)


def show_kategorie_input(case):
    RezepteService.showKategorieSelection(rezepte_gui)
    RezepteService.forgetFrameOne(rezepte_gui)
    if case == 1:
        confirmButtonSearchKategorieOne.grid(row=6, column=4, padx=25)
        confirmButtonSearchKategorieTwo.grid_forget()
    else:
        confirmButtonSearchKategorieOne.grid_forget()
        confirmButtonSearchKategorieTwo.grid(row=6, column=4, padx=25)


def show_rezept_input():
    """ Rezept-Eingabe anzeigen """
    kategorieName = rezepte_gui.kategorieNameInput.get()
    kategorieExists = RezepteService.check_kategorie(kategorieName)
    if kategorieExists:
        search = Konstanten.searchRezept
        RezepteService.fillRezepte(db, kategorieName)
        numberOfRezepte = RezepteService.rezepte.__len__()
        for i in range(0, numberOfRezepte):
            name = RezepteService.rezepte.__getitem__(i)
            i = i + 1
            search = search + " " + str(i) + ") " + name
            if i % 5 == 0:
                search = search + "\n "
        rezepte_gui.frameInformationNotFound.pack_forget()
        rezepte_gui.frameSelectionRezepte.pack(padx=10, pady=10)
        selectionLabelRezept = Label(rezepte_gui.frameSelectionRezepte, text=search)
        selectionLabelRezept.grid(row=5, column=0, columnspan=10, padx=100)
        rezepte_gui.rezeptNameInput.grid(row=6, column=0, columnspan=10, padx=100)
        confirmButtonRezept.grid(row=7, column=3, padx=25)
        newCategorieButton.grid(row=7, column=4, padx=25)
    else:
        rezepte_gui.frameInformationNotFound.pack(padx=10, pady=10)
        rezepte_gui.selectionLabelKategorieNotFound.grid(row=5, column=0, columnspan=10, padx=100)
        rezepte_gui.kategorieNameInput.delete(0, END)


def choose_new_categorie():
    """ Neue Kategorie auswählen """
    rezepte_gui.kategorieNameInput.delete(0, END)
    RezepteService.forgetFrameTwo(rezepte_gui)


def create_new_categorie():
    RezepteService.forgetFrameOne(rezepte_gui)
    rezepte_gui.frameSelectionKategorie.pack_forget()
    rezepte_gui.frameCreateKategorie.pack(padx=10, pady=10)
    rezepte_gui.createLabelKategorie.grid(row=2, column=0, columnspan=10, padx=100)
    rezepte_gui.createKategorieNameInput.grid(row=3, column=0, columnspan=10, padx=100)
    createCategorieButton.grid(row=4, column=0, columnspan=10, padx=100)


def create_categorie():
    kategorieName = rezepte_gui.createKategorieNameInput.get()
    db.files_create_folder('/' + kategorieName, autorename=False)
    RezepteService.fillKategorie(db)


def show_upload_input():
    """ Upload-Input anzeigen """
    kategorieName = rezepte_gui.kategorieNameInput.get()
    kategorieExists = RezepteService.check_kategorie(kategorieName)
    if kategorieExists:
        rezepte_gui.frameUploadRezepte.pack()
        rezepte_gui.uploadLabelRezept.grid(row=5, column=0, columnspan=10, padx=100)
        rezepte_gui.rezeptNameInputUpload.grid(row=6, column=0, columnspan=10, padx=100)
        confirmButtonRezeptUpload.grid(row=7, column=4, padx=25)
        chooseButtonRezeptUpload.grid(row=7, column=3, padx=25)
    else:
        rezepte_gui.frameInformationNotFound.pack(padx=10, pady=10)
        rezepte_gui.selectionLabelKategorieNotFound.grid(row=5, column=0, columnspan=10, padx=100)
        rezepte_gui.kategorieNameInput.delete(0, END)


def suche():
    """ Rezept suchen und download """
    kategorieName = rezepte_gui.kategorieNameInput.get()
    rezeptName = rezepte_gui.rezeptNameInput.get()
    dropboxPath = "/" + kategorieName + "/" + rezeptName
    downloadPath = "C:/Users/" + getpass.getuser() + "/Documents/" + rezeptName
    isFileExisting = exists_file(dropboxPath)
    information_find_label = Label(rezepte_gui.frameInformationFound, text="Die Datei " + rezeptName + " wurde erfolgreich heruntergeladen. \n Diese kann unter " + downloadPath + " gefunden werden.")
    information_not_find_label = Label(rezepte_gui.frameInformationNotFound, text="Die Datei " + rezeptName + " wurde nicht gefunden. \n Bitte geben Sie einen Dateinamen ein.")
    if isFileExisting:
        db.files_download_to_file(downloadPath, dropboxPath)
        rezepte_gui.rezeptNameInput.delete(0, END)
        rezepte_gui.frameInformationNotFound.pack_forget()
        rezepte_gui.frameInformationFound.pack(padx=10, pady=10)
        rezepte_gui.selectionLabelKategorieNotFound.grid_forget()
        information_not_find_label.grid_forget()
        information_find_label.grid(row=8, column=0, columnspan=10, padx=100)
    else:
        rezepte_gui.rezeptNameInput.delete(0, END)
        rezepte_gui.frameInformationFound.pack_forget()
        rezepte_gui.frameInformationNotFound.pack(padx=10, pady=10)
        information_find_label.grid_forget()
        information_not_find_label.grid(row=8, column=0, columnspan=10, padx=100)


def choose_rezept_upload():
    """ Rezept-Datei für upload auswählen"""
    sourceDir = filedialog.askopenfilename()
    rezepte_gui.rezeptNameInputUpload.insert(1, sourceDir)


def upload():
    """ upload einer rezept datei"""
    kategorieName = rezepte_gui.kategorieNameInput.get()
    rezeptName = rezepte_gui.rezeptNameInputUpload.get()
    if len(rezeptName) > 0:
        sourceDirsplitted = rezeptName.split("/")
        lastIndex = len(sourceDirsplitted)
        sourceEnding = sourceDirsplitted[lastIndex - 1].split(".")[1]
        if sourceEnding == "pdf":
            dropboxPath = "/" + kategorieName + "/" + sourceDirsplitted[lastIndex - 1]
            with open(rezeptName, 'rb') as f:
                db.files_upload(f.read(), dropboxPath)
            rezepte_gui.frameInformationUpload.pack(padx=10, pady=10)
            rezepte_gui.frameInformationNotUpload.pack_forget()
            rezepte_gui.information_upload_label.grid(row=8, column=0, columnspan=10, padx=100)
        else:
            rezepte_gui.frameInformationUpload.pack_forget()
            rezepte_gui.frameInformationNotUpload.pack(padx=10, pady=10)
            rezepte_gui.information_upload_Error_Ending_label.grid(row=8, column=0, columnspan=10, padx=100)
            rezepte_gui.information_upload_Error_label.grid_forget()
    else:
        rezepte_gui.frameInformationUpload.pack_forget()
        rezepte_gui.frameInformationNotUpload.pack(padx=10, pady=10)
        rezepte_gui.information_upload_Error_label.grid(row=8, column=0, columnspan=10, padx=100)
        rezepte_gui.information_upload_Error_Ending_label.grid_forget()
    rezepte_gui.rezeptNameInputUpload.delete(0, END)


# Funktion, die prüft, ob ein File in der Dropbox vorhanden ist
def exists_file(file_name):
    """ Prüft, ob Pfad existiert"""
    try:
        db.files_get_metadata(file_name)
        return True
    except Exception:
        return False


# Funktion, die die Account-Informationen ausgibt
def show_information():
    """ Zeigt Account Informationen """
    rezepte_gui.frameSelectionKategorie.pack_forget()
    RezepteService.forgetFrameTwo(rezepte_gui)
    rezepte_gui.frameUploadRezepte.pack_forget()
    rezepte_gui.frameAccountInformation.pack(padx=10, pady=10)
    account_information_label = Label(rezepte_gui.frameAccountInformation, text="Account infos: " + db.users_get_current_account().__getattribute__("name").__str__() + "\n" + db.users_get_current_account().__getattribute__("email").__str__())
    account_information_label.grid(row=9, column=0, columnspan=10, padx=100)


def shutdown():
    """ Schließt das Fenster """
    fenster.destroy()


# Ein Eingabefeld zur Eingabe einer Kategorie anzeigen
rezepte_gui.openingLabel.grid(row=0, column=0, columnspan=10, padx=100)

# Button für die Suche einer Kategorie
confirmButtonKategorie = Button(rezepte_gui.frameOpening, text="Suche Kategorie starten", command=lambda: show_kategorie_input(1))
confirmButtonKategorie .grid(row=4, column=3, padx=25)
confirmButtonSearchKategorieOne = Button(rezepte_gui.frameSelectionKategorie, text="Kategorie suchen", command=show_rezept_input)
confirmButtonSearchKategorieTwo = Button(rezepte_gui.frameSelectionKategorie, text="Kategorie suchen", command=show_upload_input)
confirmButtonRezept = Button(rezepte_gui.frameSelectionRezepte, text="Suche Rezept Starten", command=suche)
confirmButtonRezeptUpload = Button(rezepte_gui.frameUploadRezepte, text="Upload Rezept Starten", command=upload)
chooseButtonRezeptUpload = Button(rezepte_gui.frameUploadRezepte, text="Ein Rezept auswählen", command=choose_rezept_upload)
newCategorieButton = Button(rezepte_gui.frameSelectionRezepte, text="Neue Kategorie eingeben", command=choose_new_categorie)
# Button für die Account-Informationen
accountButton = Button(rezepte_gui.frameOpening, text="Account Informationen anzeigen", command=show_information)
accountButton.grid(row=4, column=4, padx=25)
# Button zum Datei-Upload
uploadButton = Button(rezepte_gui.frameOpening, text="Eine Datei uploaden", command=lambda: show_kategorie_input(2))
uploadButton.grid(row=4, column=5, padx=25)
# Button neue Kategorie erstellen
createNewCategorieButton = Button(rezepte_gui.frameOpening, text="Eine neue Kategorie erstellen", command=create_new_categorie)
createNewCategorieButton.grid(row=4, column=6, padx=25)
createCategorieButton = Button(rezepte_gui.frameCreateKategorie, text="Kategorie erstellen", command=create_categorie)

# Command für Menü hinzufügen
rezepte_gui.filemenu.add_command(label="Programm beenden", command=shutdown)

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.geometry("1920x1080")
fenster.mainloop()
