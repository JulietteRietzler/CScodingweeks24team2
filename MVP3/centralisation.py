import json
from MVP3.similarité_méthode import *
from MVP3.récupération_méthodes import *
from MVP3.récupération_test import *

def resultats_comparaison(fichier,fichierTest):
  '''
  :param fichier: fichier à analyser
  :retourne: un fichier json
  '''
  d={}
  d["pourcentage de similarité des méthodes avec les fichiers"]=
  #d["pourcentage de similarité des noms de variable avec les fichiers"]=
  d["pourcentage de similarité des tests avec les fichiers"]=
  return(json.dumps(d,indent=4))
