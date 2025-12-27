





#omnivorisme et regression sur l'omnivorisme
#df["score_omnivorisme"] = df[[c for c in df.columns if c.endswith("_bin")]].sum(axis=1)

#X = df[["sexe", "age", "plusde10000habitants"]]
#X = sm.add_constant(X)

#y = df["score_omnivorisme"]

#model = sm.OLS(y, X, missing="drop").fit()
#print(model.summary())





# regression par classe du clustering
#for c in df["classe"].unique():
#    sub = df[df["classe"] == c]
#    model = sm.OLS(
#        sub["score_omnivorisme"],
#        sm.add_constant(sub[["age_cat", "sexe", "agglo"]]),
#        missing="drop"
#    ).fit()
#    print(f"\nClasse {c}")
#    print(model.summary())