from tkinter import *
from tkinter.ttk import *
import tkinter as tk

from Main import *
from TkSettings import *

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

# Main ===============================

# Frame du menu NSI Project
menu = tk.Frame(window, bg=ColorMenu)
menu.configure(width=450, height=55)
menu.place(x=0, y=0)

        # Texte du menu NSI Project
menu_label = tk.Label(menu, text="NSI Project", font=('Bahnschrift SemiBold', 20), fg='#EBDD52', bg=ColorMenu)
menu_label.place(x=10, y=9)

        # Bouton Settings
Settings_img = tk.PhotoImage(file="Ressources\\settings_img.png")

Settings_button = tk.Button(menu)
Settings_button.config(image=Settings_img, borderwidth=0, highlightthickness=0)

Settings_button.place(x=400, y=12)


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

CreerFichier = tk.Button(choix, text="Créer le fichier", bg="#232F4E", fg=Colortext, bd=0)
CreerFichier.configure(width=20, command=choix)
CreerFichier.place(x=40, y=175)  # POSITION DU BOUTON "Créer le fichier"

choix.place(x=5, y=65)

# Bouton "Créer le fichier"
def choix():
    clicked = selected.get()
    if clicked == 1:
        return HtmlCreator(Annee.get())
    elif clicked == 2:
        return TxtCreator(Annee.get())



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

window.mainloop()  # Ouverture de la fenêtre
