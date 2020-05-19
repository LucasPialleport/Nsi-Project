from tkinter import *
from tkinter.ttk import *
import tkinter as tk

from Main import *

def settings_window():
    settings = Tk()

    settings.title("Paramètre de l'application")
    settings.geometry("450x320")
    settings.configure(bg="#26273B")
    settings.resizable(0, 0)
    settings.iconbitmap('Ressources\\icon.ico')

    settings.mainloop()

