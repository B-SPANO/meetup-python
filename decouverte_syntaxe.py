# Rapide découverte de la syntaxe génerale de python a travers l'exemple de la suite de Syracuse.
# Lien suite de Syracuse: https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse


# Doc de Python:
# https://docs.python.org/fr/3/tutorial/introduction.html

# les Variables :
# Elles sont affectées grace a la syntaxe: nom_variable = valeur_affectée
# les chaines de caracteres sont a encapsuler dans des guillemets -> nom_variable = "valeur_affectée"
# dans le cas d'un entier ex: 2, il n'y as pas besoin de guillemets -> ma_variable = 2

# les Fonctions :
# Elles sont des bouts de code déja programmer et pouvant etre appeler pour realiser le role qui est leur est attribuer
# Elles sont appeler comme suis ->  nom_fonction() (les parentheses vide ici, servent a passer des valeurs, les arguments.)
# ex: print() qui affiche la valeur passé en parametres.

# Conditions:
# syntaxe indissociable de la programmation informatique, les structures conditionnelles permettent de comparer deux elements (ou plus)
# et d'effectuer certaines actions en retour.
# exemple de syntaxe: 

# if age > 18 :
#     print("majeur")
# else:
#     print("mineur")


# Boucles:
# Les boucles permettent de repeter un bout de code plusieurs fois, elles possedent
# une ou plusieurs valeurs indiquant leurs modalitées d'executions.
# Il existe 2 type de boucles principaux, for et while
# exemple de syntaxe:

# boucle for: (Faire pour)

# words = ['cat', 'window', 'defenestrate']
# for w in words:
    # print(w, len(w))  # len() est une fonction qui affiche longeur.

# cat 3
# window 6
# defenestrate 12

# boucle while: (faire tant que)

# while a < 2:
#     a - 1

# l'une des force de Python est sa facilité de lecture et d'ecriture
# c'est un langage de haut niveau, proche du langage naturel.
# Son formatage est directement dicter dans les bonnes pratique de Python
# permettant ainsi d'unifier la facon de coder en Python.
# les regles sont dans la PEP8 (Python Enhancement Proposal)
# https://www.python.org/dev/peps/pep-0008/


# Essayer de traduire ce pseudo-code en Python et de lancer le script.
# issue de https://www.math93.com/images/algobox/Syracuse_temps_vol_math93.html#42


# 1   VARIABLES (en Python pas besoin de déclarer les variables en amont)
# 2     u EST_DU_TYPE NOMBRE
# 3     i EST_DU_TYPE NOMBRE
# 4     n EST_DU_TYPE NOMBRE
# 5     m EST_DU_TYPE NOMBRE
# 6     l EST_DU_TYPE NOMBRE
# 7     j EST_DU_TYPE NOMBRE
# 8   DEBUT_ALGORITHME
# 9     AFFICHER "Donnez le nombre de suites de Syracuse à analyser."
# 10    AFFICHER "L'algorithme propose le calcul du temps de vol et de l'altitude maximale des suites de Syracuse"
# 11    TANT_QUE (l<2) FAIRE
# 12      DEBUT_TANT_QUE
# 13      LIRE l
# 14      FIN_TANT_QUE
# 15    POUR j ALLANT_DE 2 A l
# 16      DEBUT_POUR
# 17      n PREND_LA_VALEUR j
# 18      TANT_QUE (n!=1) FAIRE
# 19        DEBUT_TANT_QUE
# 20        SI (n%2==0) ALORS
# 21          DEBUT_SI
# 22          n PREND_LA_VALEUR n/2
# 23          FIN_SI
# 24          SINON
# 25            DEBUT_SINON
# 26            n PREND_LA_VALEUR 3*n+1
# 27            FIN_SINON
# 28        i PREND_LA_VALEUR i+1
# 29        SI (n>m) ALORS
# 30          DEBUT_SI
# 31          m PREND_LA_VALEUR n
# 32          FIN_SI
# 33        FIN_TANT_QUE
# 34      AFFICHER "Suite N = "
# 35      AFFICHER j
# 36      AFFICHER " : Temps vol = "
# 37      AFFICHER i
# 38      AFFICHER " / et Altitude max = "
# 39      AFFICHER m
# 40      m PREND_LA_VALEUR j+1
# 41      i PREND_LA_VALEUR 0
# 42      FIN_POUR
# 43  FIN_ALGORITHME