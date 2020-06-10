# -*- coding: utf-8 -*-
"""
Created : 10/06/2020
@author: Lucas Pialleport

Code du tri par insertion : change la méthode de tri pour la faire corresponde a celle étudié en cours
PS : Ce code a pour objectif de démontrer nos compétances avec le tri par sélection, mais il n'est pas nécésaire au foctionement du programe et n'y est pas utilisé
"""
from random import *
from Main import *

def get_Sorted_by_insert_Infos(annee: str):

    dico_annee = {}

    for i in range(len(table)):
        if table[i][annee] != ":": dico_annee[table[i]["geo\\time"]] = int(table[i][annee])

    list_annee = [(k, v) for k, v in dico_annee.items()]

    #Fonction de tri :

    def tri(t: list):
        """
        Trie le tableau t dans l'ordre croissant
        :param : t (list)
        :return : t (list, valeur modifier : dans l'ordre corissant)
        """

        def echange(table, indice1, indice2):
            """
            Sous fonction : Effectue un échange de valeurs entre deux variables.
            :param : indice1(list), indice2(list), table(list)
            :return : table(list, valeur modifier)
            """

            tableVal1 = table[indice1]
            tableVal2 = table[indice2]

            table[indice1] = tableVal2
            table[indice2] = tableVal1

        for debut_nonTriee in range(len(t)):

            indice_valMini = debut_nonTriee

            for i in range(debut_nonTriee, len(t)):


                if t[i][1] < t[indice_valMini][1]:
                    indice_valMini = i

            echange(t, debut_nonTriee, indice_valMini)

        return t

    def convert_list_to_dict(liste : list):
        """
        Sous fonction : Convertie une liste de tuple en dictionaire.
        :param : liste (list)
        :return : dico_sorted(dico, trier dans l'ordre croisant)
        """

        dico_sorted = {}
        for k, v in liste: dico_sorted[k] = v

        return dico_sorted

    return convert_list_to_dict(tri(list_annee))

year = str(randint(2007, 2018))
print("DEBUG ⇒ Année :",year , "→", get_Sorted_by_insert_Infos(year))
