import requests
import pandas as pd
import numpy as np
import os


def telecharger(url, nom, dossier="/home/onyxia/work/Projet_Python_pour_DS/data"):
    """"
    Importe le fichier de données sur le site
    url (str) : url du fichier que l'on souhaite télécharger
    nom (str) : nom du fichier qui apparaîtra  
    dossier (str) : chemin du dossier où le fichier sera téléchargé
    """
    response = requests.get(url)
    chemin_fichier = os.path.join(dossier, nom)
    if response.status_code == 200:
        with open(chemin_fichier, "wb") as file:
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


def ponderation_freq(series, weights):
    return (series
            .groupby(series)
            .apply(lambda x: weights.loc[x.index].sum())
            / weights.sum()) * 100


def recodage_barometre():
    df_barometre_cleaned = df_barometre_brut[variables_barometre]

    df_barometre_cleaned.replace({"#NUL!": np.nan, "": np.nan, " ": np.nan}, inplace=True)
    df_barometre_cleaned = df_barometre_cleaned.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # retirer les espaces au début et à la fin des string pour le recodage au cas où

    df_barometre_recode = pd.DataFrame([])

    # Sexe
    sexe_map = {"Une femme": 1, "Un homme": 0}
    df_barometre_recode["sexe"] = df_barometre_cleaned["SEXE"].map(sexe_map)

    df_barometre_recode["age"]=df_barometre_cleaned["AGE"]

    agglo_map = {"MoinsDe100000Habitants":0, "PlusDe100000Habitants":1}
    df_barometre_recode["plusde10000habitants"] = df_barometre_cleaned["AGGLOIFOP2"].map(agglo_map)


    df_barometre_recode["commune_centreville"] = np.where(
        df_barometre_cleaned["TYPCOM"] == "VilleCentre", 1, 0)

    df_barometre_recode["commune_rural"] = np.where(
        df_barometre_cleaned["TYPCOM"] == "Rural", 1, 0)

    df_barometre_recode["commune_banlieue_sup"] = np.where(
        df_barometre_cleaned["TYPCOM"] == "BanlieueNVSup", 1, 0)

    df_barometre_recode["commune_banlieue_modeste"] = np.where(
        df_barometre_cleaned["TYPCOM"] == "BanlieueNVModeste", 1, 0)

    df_barometre_recode["commune_banlieue_inter"] = np.where(
        df_barometre_cleaned["TYPCOM"] == "BanlieueNVInterm", 1, 0)

    df_barometre_recode["commune_isolee"] = np.where(
        df_barometre_cleaned["TYPCOM"] == "VilleIsolee", 1, 0)


    df_barometre_recode["taille_commune"] = df_barometre_cleaned["TAILCOM"]

    departements_dict = {
        "AIN": "01", "AISNE": "02", "ALLIER": "03", "ALPESDEHAUTESPROVENCE": "04",
        "HAUTESALPES": "05", "ALPESMARITIMES": "06", "ARDECHE": "07", "ARDENNES": "08",
        "ARIEGE": "09", "AUBE": "10", "AUDE": "11", "AVEYRON": "12", "BOUCHESDURHONE": "13",
        "CALVADOS": "14", "CANTAL": "15", "CHARENTE": "16", "CHARENTEMARITIME": "17",
        "CHER": "18", "CORREZE": "19", "CORSES": "2A", "COTEOR": "21", "COTEDARMOR": "22",
        "CREUSE": "23", "DORDOGNE": "24", "DOUBS": "25", "DROME": "26", "EURE": "27",
        "EUREETLOIRE": "28", "FINISTERE": "29", "GARD": "30", "HAUTEGARONNE": "31",
        "GERS": "32", "GIRONDE": "33", "HERAULT": "34", "ILLEETVILAINE": "35",
        "INDRE": "36", "INDREETLOIRE": "37", "ISERE": "38", "JURA": "39", "LANDES": "40",
        "LOIRTCHER": "41", "LOIRE": "42", "HAUTELOIRE": "43", "LOIREATLANTIQUE": "44",
        "LOIRET": "45", "LOT": "46", "LOTETGARONNE": "47", "LOZERE": "48", "MAINEETLOIRE": "49",
        "MANCHE": "50", "MARNE": "51", "HAUTEMARNE": "52", "MAYENNE": "53", "MEURTHEETMOSELLE": "54",
        "MEUSE": "55", "MORBIHAN": "56", "MOSELLE": "57", "NIEVRE": "58", "NORD": "59",
        "OISE": "60", "ORNE": "61", "PASDECALAIS": "62", "PUYDEDOME": "63",
        "PYRENNEESATLANTIQUES": "64", "HAUTESPYRENNEES": "65", "PYRENNEESORIENTALES": "66",
        "BASRHIN": "67", "HAUTRHIN": "68", "RHONE": "69", "HAUTESAONE": "70",
        "SAONEETLOIRE": "71", "SARTHE": "72", "SAVOIE": "73", "HAUTESAVOIE": "74",
        "PARIS": "75", "SEINEMARITIME": "76", "SEINEETMARNE": "77", "YVELINES": "78",
        "DEUXSEVRES": "79", "SOMME": "80", "TARN": "81", "TARNETGARONNE": "82",
        "VAR": "83", "VAUCLUSE": "84", "VENDEE": "85", "VIENNE": "86", "HAUTEVIENNE": "87",
        "VOSGES": "88", "YONNE": "89", "BELFORT": "90", "ESSONNE": "91",
        "HAUTSDESEINE": "92", "SEINESAINTDENIS": "93", "VALDEMARNE": "94", "VALDOISE": "95"
    }

    df_barometre_recode["dpt"] = df_barometre_cleaned["DPT"].map(departements_dict)

    province_map = {"RegionIleDeFrance":0, "PROVINCE":1}
    df_barometre_recode["province"] = df_barometre_cleaned["REG3"].map(province_map)

    df_barometre_recode["region"] = df_barometre_cleaned["REG13"]

    df_barometre_recode["situation_actuelle"] = df_barometre_cleaned["SITI"]

    df_barometre_recode["profession"] = df_barometre_cleaned["PPIA"]

    df_barometre_recode["csp"] = df_barometre_cleaned["RECPPIA"]

    df_barometre_recode["csp_plus"] = np.where(
        df_barometre_cleaned["PI4"] == "CSPPLUS", 1, 0)

    df_barometre_recode["csp_moins"] = np.where(
        df_barometre_cleaned["PI4"] == "CSPMOINS", 1, 0)

    df_barometre_recode["csp_inactifs"] = np.where(
        df_barometre_cleaned["PI4"] == "INACTIFS", 1, 0)

    df_barometre_recode["csp_inactifs_plus"] = np.where(
        df_barometre_cleaned["RECPPIA"] == "RetraitesCSPPlus", 1, 0)

    df_barometre_recode["csp_inactifs_moins"] = np.where(
        df_barometre_cleaned["RECPPIA"] == "RetraitesCSPMoins", 1, 0)


    df_barometre_recode["foyer"] = df_barometre_cleaned["FOYER"]

    df_barometre_recode[["conso_demat_mus", "conso_demat_films", "conso_demat_series", "conso_demat_photos", "conso_demat_jv", "conso_demat_livres", "conso_demat_logi", "conso_demat_presse", "conso_demat_retrans"]] = df_barometre_cleaned[["Q1_1", "Q1_2", "Q1_3", "Q1_4", "Q1_5", "Q1_6", "Q1_7", "Q1_8", "Q1_9"]]
    df_barometre_recode[["conso_demat_mus", "conso_demat_films", "conso_demat_series", "conso_demat_photos", "conso_demat_jv", "conso_demat_livres", "conso_demat_logi", "conso_demat_presse", "conso_demat_retrans"]] = df_barometre_recode[["conso_demat_mus", "conso_demat_films", "conso_demat_series", "conso_demat_photos", "conso_demat_jv", "conso_demat_livres", "conso_demat_logi", "conso_demat_presse", "conso_demat_retrans"]].applymap(lambda x: 1 if isinstance(x, str) and x.strip() != "" else 0)

    freq_map = {"Moins souvent": "Rare", "1 à 3 fois par mois": "Occasionnel", "1 à 5 fois par semaine": "Regulier", "Tous les jours ou presque": "Intensif"}
    df_barometre_recode[["freq_demat_mus", "freq_demat_films", "freq_demat_series", "freq_demat_photos", "freq_demat_jv", "freq_demat_livres", "freq_demat_logi", "freq_demat_presse", "freq_demat_retrans"]] = df_barometre_cleaned[["Q2_r1", "Q2_r2", "Q2_r3", "Q2_r4", "Q2_r5", "Q2_r6", "Q2_r7", "Q2_r8", "Q2_r9"]]

    for p in pratiques:
        df_barometre_recode[f"freq_demat_{p}"] = df_barometre_recode[f"freq_demat_{p}"].map(freq_map)

    df_barometre_recode["legal_culture"] = df_barometre_cleaned["Q4"]

    df_barometre_recode["poids"] = df_barometre_cleaned["POIDS"]

    df_barometre_recode["conso_legale"] = np.where(
        df_barometre_cleaned["Q4"] == "Uniquement de manière légale", 1, 0)

    df_barometre_recode["conso_illegale"] = np.where(
        df_barometre_cleaned["Q4"] == "Uniquement de manière illégale", 1, 0)

    mix_legal = [
        "Généralement de manière légale même s’il peut m’arriver de le faire de manière illégale",
        "Autant de manière légale qu’illégale",
        "Généralement de manière illégale même s’il peut m’arriver de le faire de manière légale"
    ]

    df_barometre_recode["conso_legale_et_illegale"] = (
        df_barometre_cleaned["Q4"].isin(mix_legal)
    ).astype(int)



    print(df_barometre_recode.head())