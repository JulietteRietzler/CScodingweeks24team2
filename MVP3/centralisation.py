import json
from MVP3.identique import*
from MVP3.comparaison import *

def resultats_comparaison(fichier,fichier_test,autres_fichiers, autres_fichiers_test):
 '''
 :param fichier: fichier à analyser
 :param autres_fichier: fichiers qui sont comparés au fichier à analyser
 :retourne: un fichier json
 '''
 d={}
 d["pourcentage de similarité des méthodes avec les fichiers"]=comparaison_methode(fichier,autres_fichiers)[0]
 d["pourcentage de similarité des noms de variable avec les fichiers"]=comparaison_nom_methode(fichier,autres_fichiers)[0]
 d["pourcentage de similarité des tests avec les fichiers"]=comparaison_test(fichier_test,autres_fichiers_test)[0]
 d["nombre moyenne de noms de méthodes identiques avec les fichiers"]=nombre_moyen_identique_methodes(fichier,autres_fichiers)
 d["fichier le plus similaire"]=comparaison_methode(fichier,autres_fichiers)[1]
 d["fichier ayant les tests les plus similaires"]=comparaison_test(fichier_test,autres_fichiers_test)[1]
 if comparaison_methode(fichier,autres_fichiers)[0]>=0.6 or comparaison_test(fichier_test,autres_fichiers_test)[0]:
     d["fraude probable"]=True
 else:
     d["fraude probable"]=False
 return(json.dumps(d,indent=4),d)


