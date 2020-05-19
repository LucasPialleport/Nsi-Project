# -*- coding: utf-8 -*-
"""
Created : 14/05/2020
@author: Alexandre Wargnier / Lucas Pialleport

Code tkinter : permet l'affichage de l'interface graphique et assure la connexion de celle-ci à "Main"
"""
import webbrowser, os

from tkinter import *
from tkinter.ttk import *
import tkinter as tk

from Main import *

# Initialisation =====================

    # Centrer la fenetre
def center_window(width, height):

    # get screen width et height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    # calcule position x et y
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

window = Tk()
window.title("Démographie Européenne")
center_window(450,320)
window.configure(bg="#26273B")
window.resizable(0, 0)
window.iconbitmap('Ressources\\icon.ico')

    # Colors
Colortext = "#6AFFF3"
ColorBackground = "#26273B"
ColorMenu = "#141526"

# /Initialisation ====================

#Fenètre About =======================

def open_About():

    window.withdraw()#cache la fenetre principale

    def center_About(width, height):
        # get screen width et height
        screen_width = About.winfo_screenwidth()
        screen_height = About.winfo_screenheight()
        # calcule position x et y
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        About.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def return_to_home():
        window.deiconify() #montre la fenetre principale
        About.withdraw() #cache le about

    def show_source_code():
        """Ouvre une fenêtre navigateur, menant au code source sur Git Hub"""
        webbrowser.open('https://github.com/LucasPialleport/Nsi-Project')

    def show_license():
        """Ouvre le notepad, contenat la license"""
        os.startfile("Ressources\\LICENSE.txt")

    About = Tk()
    About.title("Paramètre de l'application")
    center_About(400,220)
    About.configure(bg=ColorBackground)
    About.resizable(0, 0)
    About.iconbitmap('Ressources\\icon.ico')

    # Frame du menu About
    menu_About = tk.Frame(About, bg=ColorMenu)
    menu_About.configure(width=450, height=53)
    menu_About.place(x=0, y=0)

    # Texte du menu About
    menu_label = tk.Label(menu_About, text="Paramètres", font=('Bahnschrift SemiBold', 20), fg='#EBDD52', bg=ColorMenu)
    menu_label.place(x=10, y=6)

    #boutton home
    home_img = tk.PhotoImage(file="Ressources\\About.png")
    home_button = tk.Button(About,text="↳Retour",font=('Bahnschrift SemiBold', 18), fg='#EBDD52', command=return_to_home, width=10, height=1, bg=ColorMenu)
    home_button.config(borderwidth=0, highlightthickness=0)
    home_button.place(x=263, y=4)

    # Bouton : "Afficher le code source"
    source_code_button = tk.Button(About, text="Afficher le code source", command=show_source_code, bg="#232F4E", fg=Colortext, bd=0)
    source_code_button.place(x=140, y=70)

    # Bouton : "LICENSE"
    license_button = tk.Button(About, text="Afficher la license", command=show_license, bg="#232F4E", fg=Colortext, bd=0)
    license_button.place(x=155, y=100)

    # Bouton : "Débogage"
    debug_button = tk.Button(About, text="Créer un fichier de débogage", command=create_debug, bg="#232F4E", fg=Colortext, bd=0)
    debug_button.place(x=125, y=130)

    # Bouton : "Supprimer fichier de débogage"
    Delete_debug = tk.Button(About, text="Supprimer tous les fichiers de débogage", command=delete_debug, bg="#232F4E", fg=Colortext, bd=0)
    Delete_debug.place(x=95, y=160)

    #affichage crédit:
    credit = tk.Label(About, text="Dévellopé par : Pialleport Lucas & Wargnier Alexandre",font=('Bahnschrift SemiBold', 11), bg=ColorBackground, fg='#EBDD52')
    credit.place(x=17, y=190)  # POSITION DU TEXTE "Séléctionnez un format de sortie :"

    #affichage fenètre about
    About.mainloop()

# \fenètre About ===============================================

# Main =========================================================

# Frame du menu NSI Project
menu = tk.Frame(window, bg=ColorMenu)
menu.configure(width=450, height=55)
menu.place(x=0, y=0)

# Texte du menu NSI Project
menu_label = tk.Label(menu, text="NSI Project", font=('Bahnschrift SemiBold', 20), fg='#EBDD52', bg=ColorMenu)
menu_label.place(x=10, y=9)

# Bouton About
About_img = tk.PhotoImage(file="Ressources\\About.png")

About_button = tk.Button(menu, command=open_About)
About_button.config(image=About_img, borderwidth=0, highlightthickness=0)
About_button.place(x=400, y=12)

# Premier labelframe : "Création de fichier"
choix = tk.LabelFrame(window, text="Création de fichier", bg="#26273B", bd=1, fg=Colortext)
choix.configure(width=215, height=250)

# Renseigner une année à étudier #
YearChoice = tk.Label(choix, text="Renseignez une année à étudier :", bg="#26273B", fg=Colortext)
YearChoice.place(x=19, y=25)  # POSITION DU TEXTE "Renseignez une année à étudier :"

# Menu déroulant
Annee = Combobox(choix, state='readonly')
Annee['values'] = get_all_years()
Annee.current(0)
Annee.place(x=35, y=65)

# Séléctionnez un format de sortie #
Format = tk.Label(choix, text="Séléctionnez un format de sortie :", bg="#26273B", fg=Colortext)
Format.place(x=15, y=110)  # POSITION DU TEXTE "Séléctionnez un format de sortie :"

# Selection du type "HTML" / "TXT"
selected = IntVar()
HTML = tk.Radiobutton(choix, text="HTML", value=1, variable=selected, bg="#26273B", fg="#FFB834")
HTML.place(x=35, y=140)  # POSITION DU BOUTON HTML
TXT = tk.Radiobutton(choix, text="TXT", value=2, variable=selected, bg="#26273B", fg="#FFB834")
TXT.place(x=122.5, y=140)  # POSITION DU BOUTON TXT

def ChoixFormat():
    clicked = selected.get()
    if clicked == 1:
        return HtmlCreator(Annee.get())
    elif clicked == 2:
        return TxtCreator(Annee.get())


CreerFichier = tk.Button(choix, text="Créer le fichier", bg="#232F4E", fg=Colortext, bd=0)
CreerFichier.configure(width=20, command=ChoixFormat)
CreerFichier.place(x=40, y=175)

choix.place(x=5, y=65)


# Second labelframe : "Outils supplémentaires"
MoreTools = tk.LabelFrame(window, text="Outils supplémentaires", bg="#26273B", bd=1, fg=Colortext)
MoreTools.configure(width=215, height=250)

# Bouton : "Créer tous les fichiers TXT"
CreateAllTXT = tk.Button(MoreTools, text="Créer tous les fichiers TXT", command=create_all_txt, bg="#232F4E", fg=Colortext, bd=0)
CreateAllTXT.place(x=35, y=35)

# Bouton : "Créer tous les fichiers HTML"
CreateAllHTML = tk.Button(MoreTools, text="Créer tous les fichiers HTML", command=create_all_html, bg="#232F4E", fg=Colortext, bd=0)
CreateAllHTML.place(x=29, y=65)

# Bouton : "Supprimer tous les fichiers TXT"
DeleteAllTXT = tk.Button(MoreTools, text="Supprimer tous les fichiers TXT", command=delete_TXT, bg="#232F4E", fg=Colortext, bd=0)
DeleteAllTXT.place(x=22, y=125)

# Bouton : "Supprimer tous les fichiers HTML"
DeleteAllHTML = tk.Button(MoreTools, text="Supprimer tous les fichiers HTML", command=delete_HTML, bg="#232F4E", fg=Colortext, bd=0)
DeleteAllHTML.place(x=16.5, y=155)

# Bouton : "Supprimer tous les fichiers HTML/TXT"
DeleteAll = tk.Button(MoreTools, text="Supprimer tous les fichier", command=delete_all, bg="#232F4E", fg=Colortext, bd=0)
DeleteAll.place(x=37, y=185)

MoreTools.place(x=230, y=65)
# /Main ===============================

# Affichage de la fenêtre principale
window.mainloop()
