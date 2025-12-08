import numpy as np
import pandas as pd

np.random.seed(123)

df = pd.read_excel("/home/onyxia/work/Projet_Python_pour_DS/data/hadopi-2020-musique-data.ods", engine="odf")
obs = df.shape[0]
print(obs)

df_recode = df.assign(sexe = df["QSEXE"].map({"Femme": 0, "Homme": 1}))
df_recode = df.assign(tranche_age = df["RAGE2"].map({"De15a24ans": 1, "De25a34ans1": 2, "De35a49ans1": 3, "De50a64ans1": 4, "De65aPlus": 5}))
