# -*- coding: utf-8 -*-
"""
Created : 06/05/2020
@author: Alexandre Wargnier / Lucas Pialleport
"""
import csv, os, shutil


file = open("Eurostat_Table_population.csv")
table = list(csv.DictReader(file, delimiter=';'))
file.close()


def getSortedInfos(annee: str):

    dico_annee = {}

    for i in range(len(table)):
        if table[i][annee] != ":": dico_annee[table[i]["geo\\time"]] = int(table[i][annee])

    def tri(dico: dict):

        dico_sorted = dict(sorted(dico.items(), key=lambda t: t[1]))
        return dico_sorted

    return tri(dico_annee)


def get_all_years():

    list_all_years = []

    for keys in table[1].keys():
        if keys not in list_all_years: list_all_years.append(keys)

    del list_all_years[-1]
    del list_all_years[0]
    return list_all_years


def TxtCreator(year):

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
    for i in range(len(get_all_years())): TxtCreator(get_all_years()[i])


def HtmlCreator(year):

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
        HTML.write("\t\t\t\t\t\t" + "<li>" + str(keys) + " : " + str(dico[keys]) + "</li>\n")


    HTML.write("\t\t\t</ol>\n")
    HTML.write("\t\t</body>\n")
    HTML.write("\t</html>")

    HTML.close()

def create_all_html():
    for i in range(len(get_all_years())): HtmlCreator(get_all_years()[i])

#supression de fichier
def delete_TXT():
    try:
        shutil.rmtree('TXT')
    except:
        pass

def delete_HTML():
    try:
        shutil.rmtree('HTML')
    except:
        pass

def delete_all():
    delete_TXT()
    delete_HTML()

#-----------------------


