# Projet Python pour la Data science
Par _Morgane Ribeiro_ et _Juline Ley_, Décembre 2025

# Mesure de l'omnivorisme culturel 


## SOMMAIRE
* [Définition](#def)
* [Objectif](#obj)
* [Source des données](#source)
* [Présentation du dépôt](#pres)
* [Licence](#licence)

## Définitions <a class="anchor" id="def"></a>

L'omnivorisme culturel est une notion issue de la sociologie de la culture désignant la tendance d’un individu à consommer une large diversité de formes culturelles, au-delà des frontières traditionnelles entre genres, supports ou niveaux de légitimité culturelle.
Dans le contexte numérique, l’omnivorisme culturel renvoie à la diversification des pratiques culturelles en ligne (musique, films, séries, jeux, livres, podcasts, etc.) et à la capacité des individus à combiner plusieurs types de contenus et modes d’accès.

## Objectif <a class="anchor" id="obj"></a>

Ce projet vise à mesurer et caractériser l’omnivorisme culturel dans les pratiques numériques à partir de données d’enquêtes nationales, en construisant des indicateurs de diversité des consommations culturelles et en identifiant des profils d’usagers selon leurs pratiques.
L’objectif est d’analyser la structure des consommations culturelles numériques, d’en dégager des typologies d’individus (spécialistes vs omnivores) et d’étudier les liens entre diversité culturelle et caractéristiques sociodémographiques.

## Source des données <a class="anchor" id="source"></a>

Nous avons essentiellement utilisé deux base de données issues de l'Autorité de régulation de la communication audiovisuelle et numérique (Arcom). 

Elles ont toutes les deux été menées en 2019 et publiées en 2020 par l'Ifop 

- Pratiques d’écoute de musique en ligne - 2020 : https://www.data.gouv.fr/datasets/pratiques-decoute-de-musique-en-ligne-2020 (lien vers le site mettant à disposition les données)

La première base est issue d'une étude menée sur internet par l'Ifop en 2019. La dernière mise à jour date du 15 juin 2021

- Consommation des contenus culturels et sportifs numériques - Baromètre : https://www.data.gouv.fr/datasets/consommation-des-contenus-culturels-et-sportifs-numeriques-barometre

La seconde base de données est plus large et cible 9 contenus culturels et sportifs dématérialisés (musique, films, séries, photos, jeux vidéo, logiciels, livres numériques et audio, presse en ligne et retransmissions sportives en direct). Elle a été menée sur internet et par téléphone. La dernière mise à jour date du 3 avril 2025.

## Présentation du dépot <a class="anchor" id="pres"></a>

Le travail principal est présenté dans deux versions du fichier : ```main.ipynb```
- ```main.ipynb``` est un jupyter notebook contenant le code non exécuté et les commentaires.
- ```main(resultats).ipynb``` est un jupyter notebook contenant en plus du code et des commentaires, les résultats exécutés. Cette version est notre rendu final.

Le dossier ```data``` contient une copie locale des deux bases de données utilisées.

Le dossier ```scripts``` contient le fichier ```fonctions.py```, récapitulant toutes les fonctions que nous avons utilisées, par souci de lisibilité et de facilité de manipulation.

Le fichier ```requirements.txt``` est exécuté par pip afin d'installer tous les paquets nécessaires pour exécuter le code.

## Licence <a class="anchor" id="licence"></a>

Les deux bases de données sont disponibles en licence ouverte, c'est à dire que nous avons « le droit personnel, non exclusif et gratuit, de réutilisation de « l’Information » soumise à la présente licence, dans le monde entier et pour une durée illimitée, dans les libertés et les conditions exprimées ci-dessous.
Vous êtes libre de réutiliser « l’Information » :
- Reproduire, copier, publier et transmettre « l’Information » ;
- Diffuser et redistribuer « l’Information » ;
- Adapter, modifier, extraire et transformer à partir de « l’Information », notamment pour créer des « Informations dérivées » ;
- Exploiter « l’Information » à titre commercial, par exemple en la combinant avec d’autres « Informations », ou en l’incluant dans votre propre produit ou application.

Sous réserve de :
- Mentionner la paternité de « l’Information » : sa source (a minima le nom du « Producteur ») et la date de sa dernière mise à jour.

Le « Réutilisateur » peut notamment s’acquitter de cette condition en indiquant un ou des liens hypertextes (URL) renvoyant vers « l’Information » et assurant une mention effective de sa paternité.

Cette mention de paternité ne doit ni conférer un caractère officiel à la réutilisation de « l’Information », ni suggérer une quelconque reconnaissance ou caution par le « Producteur », ou par toute autre entité publique, du « Réutilisateur » ou de sa réutilisation. »

Source : https://www.etalab.gouv.fr/wp-content/uploads/2014/05/Licence_Ouverte.pdf 

