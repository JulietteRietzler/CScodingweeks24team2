import json
from MVP2.similarité import *
from MVP2.validité_nom import *
from MVP2.aeration import *

def donnees(fichier):
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
   d["moyenne longueur nom des fonctions"]= moyenne_longueur_nom_fonction(fichier)
   d["nom des variables"]=moyenne_longueur_variables(fichier)
   d["nom de variable trop court"]= critere_variable_pas_trop_court(fichier)
   d["pourcentage d'aeration"]=pourcentage_d_espaces(fichier)
   return(json.dumps(d,indent=4),d)

#print(donnees('EventCandidatA.rb'))
