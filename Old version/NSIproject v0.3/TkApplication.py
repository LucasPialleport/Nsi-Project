# Importation =====================
from Main import *

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

import tkinter as tk
import tkinter.font as tkFont

# Initialisation =====================
window = Tk()
window.title("Démographie Européenne")
window.geometry("450x300")
window.resizable(0, 0)
window.configure(bg='#0B0C1B')
window.iconbitmap('icon.ico')
# ====================================


# Premier labelframe : "Création de fichier"
choix = tk.Frame(window, bg='#0B0C1B')
choix.configure(width=215, height=230)

# Renseigner une année à étudier #
YearChoice = Label(choix, text="Renseignez une année à étudier :")
YearChoice.place(x=19, y=25)  # POSITION DU TEXTE "Renseignez une année à étudier :"

# Menu déroulant
Annee = Combobox(choix, state='readonly')
Annee['values'] = get_all_years()
Annee.current(0)
Annee.place(x=35, y=65)

# Séléctionnez un format de sortie #
Format = Label(choix, text="Séléctionnez un format de sortie :")
Format.place(x=15, y=110)  # POSITION DU TEXTE "Séléctionnez un format de sortie :"

# Selection du type "HTML" / "TXT"
selected = IntVar()
HTML = Radiobutton(choix, text="HTML", value=1, variable=selected)
HTML.place(x=35, y=140)  # POSITION DU BOUTON HTML
TXT = Radiobutton(choix, text="TXT", value=2, variable=selected)
TXT.place(x=122.5, y=140)  # POSITION DU BOUTON TXT

# Bouton "Créer le fichier"
CreerFichier = Button(choix, text="Créer le fichier", command=choix)
CreerFichier.configure(width=20)
CreerFichier.place(x=40, y=175)

# placement de la frame choix
choix.place(x=5,y=60)

def choix():
    """
    Permet de prendre en compte le choix des RadioButton, et d'excuter la fonction correspondante
    Enter : none / exit : résultat de la fonction correspondante au choix de l'utilisateur
    """
    clicked = selected.get()
    if clicked == 1:
        return HtmlCreator(Annee.get())
    elif clicked == 2:
        return TxtCreator(Annee.get())

#====================================================

#=== Second labelframe : "Outils supplémentaires" ===
MoreTools = tk.Frame(window, bg='#0B0C1B')
MoreTools.configure(width=215, height=230)

# Bouton : "Créer tous les fichiers TXT"
CreateAllTXT = Button(MoreTools, text="Créer tous les fichiers TXT", command=create_all_txt)
CreateAllTXT.place(x=35, y=35)

# Bouton : "Créer tous les fichiers HTML"
CreateAllHTML = Button(MoreTools, text="Créer tous les fichiers HTML", command=create_all_html)
CreateAllHTML.place(x=29, y=65)

# Bouton : "Supprimer tous les fichiers TXT"
DeleteAllTXT = Button(MoreTools, text="Supprimer tous les fichiers TXT", command=delete_TXT)
DeleteAllTXT.place(x=22, y=115)

# Bouton : "Supprimer tous les fichiers HTML"
DeleteAllHTML = Button(MoreTools, text="Supprimer tous les fichiers HTML", command=delete_HTML)
DeleteAllHTML.place(x=16.5, y=145)

# Bouton : "Supprimer tous les fichiers HTML/TXT"
DeleteAll = Button(MoreTools, text="Supprimer tous les fichier", command=delete_all)
DeleteAll.place(x=37, y=175)

# Placement de la frame MoreTools
MoreTools.place(x=230, y=60)
#===============================

#=== Frame du menu : ===========

menu = tk.Frame(window, bg='#1A1B2E')
menu.configure(width=400, height=55)

# texte du menu
menu_label = tk.Label(menu, text="NSI Project", font=('Bahnschrift SemiBold', 20),fg='#EBDD52',bg='#1A1B2E')
menu_label.place(x=10, y=8)

# Placement de la frame MoreTools
menu.place(x=0, y=0)

#===============================

#=== boutton paramètre: ===========

image = PhotoImage('settings_icon.ico')
settings = tk.Button(window, width = 50, height=50, bg='#1A1B2E' , image=image)
settings.place(x=400, y=0)

#===============================
window.mainloop()  # Ouverture de la fenêtre
