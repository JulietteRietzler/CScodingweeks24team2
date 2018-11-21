import json
from MVP2.similarité import *
#from MVP2.validité_nom import *
def resultats(fichier):
   '''
   :param fichier: fichier à analyser et à parser
   :retourne: un fichier json avec le pourcentage de ressemblance dans le fichier, si il y a un risque de duplication et
   si les nom de variable ou de fonctions sont adéquats.
   '''
   d={}
   d["pourcentage de ressemblance"]=pourcentage_de_ressemblance_code(fichier)
   #Après plusieurs test, on a estimer que si le pourcentage de ressemblance est supérieur à 60%, il y a risque de duplication.
   if pourcentage_de_ressemblance_code(fichier)>0.6:
       d["duplication probable"]=True
   else:
       d["duplication probable"]=False
   #d["nom des fonctions"]=
   #d["nom des variables"]=
   return(json.dumps(d,indent=4))

print(resultats('EventCandidatA.rb'))
