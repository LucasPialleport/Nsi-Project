# -*- coding: utf-8 -*-
"""
Created : 06/05/2020
@author: Alexandre Wargnier / Lucas Pialleport

Code principale, "Main" permet d'éffectuer toutes les oppérations et calcules nécéssaire au fonctionement du programe
"""
import csv, os, shutil


file = open("Eurostat_Table_population.csv")
table = list(csv.DictReader(file, delimiter=';'))
file.close()


def getSortedInfos(annee: str):
    """
    Cette fonction permet de récupérer les informations du fichier CSV au travers d'une table.
    Sa sous-fonction permet de trier les données récupérées dans l'ordre décroissant selon la valeur.
    Elle retourne un dictionnaire.
    :param annee:
    :return tri(dico_annee):
    """
    dico_annee = {}
    for i in range(len(table)):
        if table[i][annee] != ":": dico_annee[table[i]["geo\\time"]] = int(table[i][annee])

    def tri(dico: dict):
        """
        La fonction "tri" est une sous-fonction, elle a pour but de trier les données
        dans un ordre décroissant d'un dictionnaire, selon les valeurs.
        Elle retourne un dictionnaire.
        :param dico:
        :return dico_sorted:
        """
        dico_sorted = dict(sorted(dico.items(), key=lambda t: t[1]))
        return dico_sorted
    return tri(dico_annee)

def get_all_years():
    """
    Cette fonction permet de récupérer toutes les clés de la table contenant les données du fichier CSV
    On récupère donc toutes les années présentent, en supprimant:
        - La première valeur : "geo\\time"
        - La seconde valeur : " " (c'est une valeur vide, sûrement une erreur dans le fichier CSV)
    Elle retourne une liste.
    :return list_all_years:
    """
    list_all_years = []
    for keys in table[1].keys():
        if keys not in list_all_years: list_all_years.append(keys)
    del list_all_years[-1]
    del list_all_years[0]
    return list_all_years

def TxtCreator(year):
    """
    TxtCreator est la fonction permettant de créer un fichier TXT, voici comment elle fonctionne :
        - Tout d'abord, elle essaie de créer un dossier "TXT" (nécessaire pour la suite), si il existe déjà, alors rien ne se passe.
        - Ensuite, elle crée un fichier au format txt dans le dossier existant ou créé : l'argument year + _population_txt.txt.
        - Pour finir, elle y écrit toutes les clés ainsi que leurs valeurs de getSortedInfos().
    Elle retourne la création d'un fichiers texte.
    :param year:
    """
    try:
        os.mkdir('TXT')
    except:
        pass

    TXT = open("TXT\\" + year + "_population_txt.txt", "w")
    TXT.write("Population au 1° janvier ")
    TXT.write(str(year))
    TXT.write("\nClassement par ordre croissant")
    TXT.write("\nSource : Eurostat ")
    TXT.write(str(year) + "\n\n")
    dico = getSortedInfos(year)
    for keys in dico:
        TXT.write(str(keys) + " : " + str(dico[keys]) + "\n")

def create_all_txt():
    """
    Cette fonction sert tout simplement de boucle,
    elle exécute la fonction TxtCreator() autant de fois que la fonction get_all_years() récupère d'années.
    Elle retourne la création de tous les fichiers texte.
    """
    for i in range(len(get_all_years())): TxtCreator(get_all_years()[i])

def HtmlCreator(year):
    """
    HtmlCreator est la fonction permettant de créer un fichier HTML, voici comment elle fonctionne :
        - Tout d'abord, elle essaie de créer un dossier "HTML" (nécessaire pour la suite), si il existe déjà, alors rien ne se passe.
        - Ensuite, elle crée un fichier au format html dans le dossier existant ou créé : l'argument year + _population_html.html.
        - De plus elle y écrit une base commune à tous les fichiers HTML (CodeSource)
          puis elle y ouvre la balise <ol> pour faire le listing de toutes les données
        - Elle écrit toutes les clés ainsi que leurs valeurs de getSortedInfos() dans des balises <li> qu'elle ferme juste après.
        - Pour finir, elle ferme les balises importantes qui ont étaient ouverts au préalable.
    Elle retourne la création d'un fichiers HTML.
    :param year:
    """
    try:
        os.mkdir('HTML')
    except:
        pass

    HTML = open("HTML\\" + year + "_population_html.html", "w", encoding="UTF-8")

    CodeSource = """
    <!DOCTYPE html>
    <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <title>, Mini projet - NSI,</title> 
            <link href="style.css" rel="stylesheet">
        </head>
        <body>
            <h1>Population au 1er Janvier :</h1>
            <h2>Classement par habitants</h2>
            <h3>Source : Eurostat</h3>
                <ol>    
                      
    """
    HTML.write(str(CodeSource))
    dico = getSortedInfos(year)
    HTML.write("\n")
    for keys in dico:
        HTML.write("\t\t\t\t\t" + "<li>" + str(keys) + " : " + str(dico[keys]) + "</li>\n")

    HTML.write("\t\t\t</ol>\n")
    HTML.write("\t\t</body>\n")
    HTML.write("\t</html>")
    HTML.close()

def create_all_html():
    """
    Cette fonction sert tout simplement de boucle,
    elle exécute la fonction HtmlCreator() autant de fois que la fonction get_all_years() récupère d'années.
    Elle retourne la création de tous les fichiers html.
    """
    for i in range(len(get_all_years())): HtmlCreator(get_all_years()[i])


#TKINTER - Suppression de fichiers
def delete_TXT():
    """
    Cette fonction supprime le fichier HTML.
    """
    try:
        shutil.rmtree('TXT')
    except:
        pass

def delete_HTML():
    """
    Cette fonction supprime le dossier HTML.
    """
    try:
        shutil.rmtree('HTML')
    except:
        pass

def delete_all():
    """
    Cette fonction supprime le dossier HTML & TXT
    """
    delete_TXT()
    delete_HTML()
