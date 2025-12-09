import requests
import pandas as pd
import numpy as np

# -------------------------------
# Téléchargement du fichier
# -------------------------------
url = "https://www.data.gouv.fr/api/1/datasets/r/85d1feb0-76cc-4e84-96f4-169971db952e"

response = requests.get(url)

if response.status_code == 200:
    with open("data_arcom.ods", "wb") as file:
        file.write(response.content)
    print("Téléchargement réussi !")
else:
    print("Erreur :", response.status_code)

# -------------------------------
# Lecture en df
# -------------------------------
df_arcom = pd.read_excel("data_arcom.ods", engine="odf")
print(df_arcom.head())
obs = df_arcom.shape[0]
print(f"Nombre d'observations : {obs}")

# -------------------------------
# Sélection des variables
# -------------------------------
variables = [
    "SEXE", "QSEXE", "RAGE2", "XRAGE", "AGGLOIFOP2", "REG", "REG3", "REG13", "PI4", "STATUT",
    "FOYER", "RS1",
    # Q1_1 à Q1_11
    "Q1_1", "Q1_2", "Q1_3", "Q1_4", "Q1_5", "Q1_6", "Q1_7", "Q1_8", "Q1_9", "Q1_10", "Q1_11",
    # Q2_r1 à Q2_r11
    "Q2_r1", "Q2_r2", "Q2_r3", "Q2_r4", "Q2_r5", "Q2_r6", "Q2_r7", "Q2_r8", "Q2_r9", "Q2_r10",
    "Q2_r11", "Q3", "Q4",
    # Q5_1 à Q5_13
    "Q5_1", "Q5_2", "Q5_3", "Q5_4", "Q5_5", "Q5_6", "Q5_7", "Q5_8", "Q5_9", "Q5_10", "Q5_11",
    "Q5_12", "Q5_13",
    # Q6_r1 à Q6_r7
    "Q6_r1", "Q6_r2", "Q6_r3", "Q6_r4", "Q6_r5", "Q6_r6", "Q6_r7",
    "Q7",
    # Q18_1 à Q18_9
    "Q18_1", "Q18_2", "Q18_3", "Q18_4", "Q18_5", "Q18_6", "Q18_7", "Q18_8", "Q18_9",
    "Q22ALEA1", "Q22ALEA2"
]

df = df_arcom[variables]

# -------------------------------
# Nettoyage des valeurs nulles ou manquantes
# -------------------------------
df.replace({"#NUL!": np.nan, "": np.nan, " ": np.nan}, inplace=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # retirer les espaces au début et à la fin des string pour le recodage au cas où

# -------------------------------
# Recodage des variables sociodémo
# -------------------------------

# Sexe
sexe_map = {"FEMME": 0, "HOMME": 1}
df["sexe"] = df["QSEXE"].map(sexe_map)

# Tranche d'âge
age_map = {
    "De15a24ans": 1,
    "De25a34ans1": 2,
    "De35a49ans1": 3,
    "De50a64ans1": 4,
    "De65aPlus": 5,
}
df["age_cat"] = df["RAGE2"].map(age_map)

# Agglomération
agglo_map = {
    "MoinsDe100000Habitants": 0,
    "PlusDe100000Habitants": 1
}
df["agglo"] = df["AGGLOIFOP2"].map(agglo_map)



# -------------------------------
# Recodage de Q1, Q5, Q6, Q18 en var binaires, 0 si la personne répond non, garde la modalité sinon (ex : genre de musique)
# -------------------------------
multi_cols = [c for c in df.columns if c.startswith(("Q1_", "Q5_", "Q6_", "Q18_"))]

for col in multi_cols:
    df[col + "_bin"] = df[col].notna().astype(int)

# -------------------------------
# 6. Recodage des variables Q2_r1 à Q2_r9
# -------------------------------
freq_map_q2 = {
    "Uniquement de façon légale": 4,
    "Généralement de façon légale même s'il peut m'arriver de le faire de manière illégale": 3,
    "Autant de manière légale qu'illégale": 2,
    "Généralement de façon illégale même s'il peut m'arriver de le faire de manière légale": 1,
    "Uniquement de manière illégale": 0
}

for col in [f"Q2_r{i}" for i in range(1, 10)]:  # Q2_r10 et Q2_r11 restent NaN
    df[col + "_num"] = df[col].map(freq_map_q2)

# -------------------------------
# 7. Q22ALEA1 / Q22ALEA2 — fusion propre
# -------------------------------
df["Q22_clean"] = df[["Q22ALEA1", "Q22ALEA2"]].apply(
    lambda row: ", ".join(row.dropna().astype(str)) if row.notna().any() else np.nan,
    axis=1
)

# -------------------------------
# Verif donnees manquantes
# -------------------------------
print("\nValeurs manquantes par colonne :")
print(df.isna().sum().to_string())

print("\nPourcentage de valeurs manquantes :")
print((df.isna().mean() * 100).to_string())

# -------------------------------
# Statistiques descriptives
# -------------------------------
print("\n--- Variables numériques ---")
print(df.describe(include="number").T)

print("\n--- Variables catégorielles ---")
categorical_cols = df.select_dtypes(include="object").columns.tolist()
for col in categorical_cols:
    print(f"\nVariable : {col}")
    counts = df[col].value_counts(dropna=False)
    percentages = df[col].value_counts(normalize=True, dropna=False) * 100
    print(pd.concat([counts, percentages], axis=1, keys=["count", "percent"]))


