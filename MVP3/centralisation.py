import json
from import#à remplir

def resultats_comparaison(fichier,fichierTest):
  '''
  :param fichier: fichier à analyser
  :retourne: un fichier json
  '''
  d={}
  d["pourcentage de similarité des méthodes avec les fichiers"]=
  d["pourcentage de similarité des noms de variable avec les fichiers"]=
  d["pourcentage de similarité des tests avec les fichiers"]=
  return(json.dumps(d,indent=4))
