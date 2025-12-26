def telecharger(url, nom):
    """"Importe le fichier de données sur le site
    url (str) : url du fichier que l'on souhaite télécharger
    nom (str) : nom du fichier qui apparaîtra  """
    response = requests.get(url)
    if response.status_code == 200:
    with open(nom, "wb") as file:
        file.write(response.content)
    print("Téléchargement réussi !")
else:
    print("Erreur :", response.status_code)

