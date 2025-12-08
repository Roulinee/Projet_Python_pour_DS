import numpy as np
import pandas as pd

np.random.seed(123)

df = pd.read_excel("/home/onyxia/work/Projet_Python_pour_DS/data/hadopi-2020-musique-data.xlsx")
obs = df.shape[0]
print(obs)

df_recode = df.assign(
    sexe = df["QSEXE"].map({"FEMME": 0, "HOMME": 1}),
    tranche_age = df["RAGE2"].map({"De15a24ans": 1, "De25a34ans1": 2, "De35a49ans1": 3, "De50a64ans1": 4, "De65aPlus": 5}),
    agglo = df["AGGLOIFOP2"].map({"MoinsDe100000Habitants": 0, "MoinsDe100000Habitants":1}),
    province = df["REG3"].map({"RegionIleDeFrance":0, "PROVINCE":1}),
    csp = df["PI4"].map({"INACTIFS":-1, "CSPMOINS":0, "CSPPLUS":1}),
    freq_utilisation_internet = df["RS1"].map({"Plusieurs fois par jour":1, "1 fois par jour ou presque":2, "3 à 5 fois par semaine":3, "1 à 2 fois par semaine":4, "2 à 3 fois par semaine":4, "1 fois par mois":4, "Moins souvent":4})
)

print(df_recode.describe())