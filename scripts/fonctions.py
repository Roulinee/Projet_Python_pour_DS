import requests
import pandas as pd
import numpy as np


def telecharger(url, nom):
    """"
    Importe le fichier de données sur le site
    url (str) : url du fichier que l'on souhaite télécharger
    nom (str) : nom du fichier qui apparaîtra  
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(nom, "wb") as file:
            file.write(response.content)
        print("Téléchargement réussi !")
    else:
        print("Erreur :", response.status_code)


def analyser(df):
    """
    Résume le data frame en entrée
    df (DataFrame) : data frame à résumer
    """
    n_obs, n_var = df.shape

    n_num = df.select_dtypes(include="number").shape[1]
    n_txt = df.select_dtypes(include="object").shape[1]

    n_missing = df.isna().sum().sum()
    pct_missing = round(100 * n_missing / (n_obs * n_var), 2)

    n_var_missing = (df.isna().sum() > 0).sum()
    n_const = (df.nunique(dropna=False) <= 1).sum()

    phrase = (
        f"La base de données contient {n_obs} observations et {n_var} variables. "
        f"Elle comprend {n_num} variables numériques, {n_txt} variables de type texte, "
        f"On observe {n_missing} valeurs manquantes, soit {pct_missing}% de l’ensemble des cellules, "
        f"réparties sur {n_var_missing} variables. "
        f"Enfin, {n_const} variables sont constantes."
    )

    return phrase
