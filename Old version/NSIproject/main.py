# -*- coding: utf-8 -*-
"""
Created : 06/05/2020
@author: alexandre wargnier / lucas pialleport
"""
import csv

file = open("Eurostat_Table_population.csv")
table = list(csv.DictReader(file, delimiter=';'))
file.close()

def getter(annee:str):

    dico_annee, dico_sorted = {}, {}

    for i in range(len(table)):

        if table[i][annee] != ":":
            dico_annee[table[i]["geo\\time"]] = int(table[i][annee])

    dico_sorted = dict(sorted(dico_annee.items(),key= lambda t: t[1]))

    return dico_sorted

def get_all_years(table:list):

    list_all_years = []

    for keys in table[1].keys():
        if keys not in list_all_years:
            list_all_years.append(keys)

    del list_all_years[0]

    return list_all_years

def TxtCreator(year):

    TXT = open(year + "_population.txt","w")
    TXT.write("Population au 1° janvier ")
    TXT.write(str(year))
    TXT.write("\nClassement par ordre croissant")
    TXT.write("\nSource : Eurostat ")
    TXT.write(str(year))
    TXT.write("\n\n")

    dico = getter(year)

    for keys in dico:

            TXT.write(str(keys))
            TXT.write(" : ")

            TXT.write(str(dico[keys]))
            TXT.write("\n")

def create_all_txt():

    for i in range (len(get_all_years(table))):
        TxtCreator(get_all_years(table)[i])


def HtmlCreator(year):

    HTML = open(year + "_population.html","w", encoding="UTF-8")
    CodeSource = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Mini projet - NSI</title>
    </head>
    <body>
        <h1>
            Population au 1er Janvier 2011
        </h1>
        <h2>    
            Classement par habitants
        </h2>
        <h3>
            Source : Eurostat 2011
        </h3>
        
        <h3>
  
    """
    HTML.write(CodeSource)

    dico = getter(year)

    for keys in dico:

            HTML.write(str(keys))
            HTML.write(" : ")

            HTML.write(str(dico[keys]))
            HTML.write("</br>")
            HTML.write("\n")

    HTML.write("</h3>")
    HTML.write("\n")

    HTML.write("</body>")
    HTML.write("\n")
    HTML.write("</html>")
    HTML.write("\n")

    HTML.close()

def create_all_html():

    for i in range (len(get_all_years(table))):
        HtmlCreator(get_all_years(table)[i])

create_all_txt()
create_all_html()
