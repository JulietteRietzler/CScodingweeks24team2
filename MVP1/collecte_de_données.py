import json
from MVP1.nb_comments import *
from MVP1.nb_fonctions import *
from MVP1.nb_tests import *
from MVP1.nb_asserts import *

def resultats(fichier,fichierTest):
   '''
   :param fichier: fichier à analyser et à parser
   :retourne: un fichier json avec le nombre de fonctions définies, de tests, de commentaires et le rapport entre le nombre de fonctions définies et le nombre de tests
   '''
   d={}
   d["nombre_de_fonctions"]=nb_de_fonctions(fichier)
   d["nombre_de_tests"]=nb_de_tests(fichierTest)
   d["rapport nombre de fonctions et nombre de tests"]=nb_de_tests(fichierTest)/nb_de_fonctions(fichier)
   d["nombre moyen d'asserts par test"]= nb_moyen_de_asserts_par_test(fichierTest)
   d["nombre_de_commentaires"]=nombre_de_commentaires(fichier)+nombre_de_commentaires(fichierTest)
   d["rapport nombre de fonctions et nombre de commentaires"]=nombre_de_commentaires(fichier)/nb_de_fonctions(fichier)
   return(json.dumps(d,indent=4),d)




#print(resultats("EventCandidatA.rb","EventCandidatATest.rb"))
