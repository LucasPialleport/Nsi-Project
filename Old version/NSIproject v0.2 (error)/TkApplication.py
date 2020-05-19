from tkinter import ttk

from main import *
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.font as tkFont

# Initialisation ------------
window = Tk()
window.title("Démographie Européenne")
window.geometry("450x300")
window.resizable(0, 0)
# ---------------------------

# Main ----------------------

choix = Labelframe(window, text="Création de fichier")
choix.place(x=5, y=5)
choix.configure(width=215, height=290)
Label(choix)


# Bouton "Créer le fichier"
def ButtonClickedSuccessful():
    messagebox.showinfo("La fabrique de fichier", "Le fichier a été créé avec succès !")


CreerFichier = Button(window, text="Créer le fichier", command=ButtonClickedSuccessful)
CreerFichier.configure(width=20)
CreerFichier.place(x=49, y=200)  # POSITION DU BOUTON "Créer le fichier"

# Selection du type "HTML" / "TXT"
HTML = Radiobutton(window, text="HTML", value=1)
HTML.place(x=50, y=150)  # POSITION DU BOUTON HTML
TXT = Radiobutton(window, text="TXT", value=2)
TXT.place(x=135, y=150)  # POSITION DU BOUTON TXT

# Texte
Format = Label(window, text="Séléctionnez un format de sortie :")
Format.place(x=25, y=120)  # POSITION DU TEXTE "Séléctionnez un format de sortie :"

YearChoice = Label(window, text="Renseignez une année à étudier :")
YearChoice.place(x=25, y=40)  # POSITION DU TEXTE "Renseignez une année à étudier :"


# L'année choisie
Annee = Combobox(window)
Annee['values'] = (2007,2008,2009,2010,2011,2012,2013,2014,2015,2018)
Annee.current(0)
Annee.place(x=49, y=70)
#
#
#

# Outils supplémentaires

MoreTools = Labelframe(window, text="Outils supplémentaires")
MoreTools.place(x=230, y=5)
MoreTools.configure(width=215, height=290)
Label(MoreTools)


# Bouton
def CreateAllButtonSuccessful():
    messagebox.showinfo("La fabrique de fichier", "Toutes les fichiers de cette année ont étaient créés avec succès !")


CreateAllTXT = Button(window, text="Créer tous les fichiers TXT", command=create_all_txt)
CreateAllTXT.configure(command=CreateAllButtonSuccessful)
CreateAllTXT.place(x=266, y=68)

CreateAllHTML = Button(window, text="Créer tous les fichiers HTML", command=create_all_html)
CreateAllHTML.configure(command=CreateAllButtonSuccessful)
CreateAllHTML.place(x=260, y=100)
# ---------------------------
window.mainloop()
