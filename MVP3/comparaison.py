from MVP3.récupération_test import *
from MVP3.récupération_méthodes import *
from MVP2.validité_nom import *
from MVP3.similarité_méthode import *



def comparaison_test(fichier,*autres_fichiers):
   '''
   :param fichier: fichier à analyser
   :param autres_fichiers: autres fichiers qui sont comparés au fichier à analyser
   :return: tuple avec le poucentage de similarité le plus élevé et l'incide du fichier qui correspond avec ce pourcentage
   '''
   liste_test=récupérationt(fichier)
   liste_similarite=[]
   for i in range (len(autres_fichiers)):
       liste_comparaison=récupérationt(autres_fichiers[i])
       for k in range (len(liste_test)):
           for j in range (len(liste_comparaison)):
               m= (liste_test[k],liste_comparaison[j])
               liste_similarite.append(m)
   max=max(liste_similarite)
   indice_max=[i for i, j in enumerate(liste_similarite) if j == max]
   return(max,indice_max)


def comparaison_methode(fichier,*autres_fichiers):
   '''
   :param fichier: fichier à analyser
   :param autres_fichiers: autres fichiers qui sont comparés au fichier à analyser
   :return: tuple avec le poucentage de similarité le plus élevé et l'incide du fichier qui correspond avec ce pourcentage
   '''
   liste_methode=récupérationm(fichier)
   liste_similarite=[]
   for i in range (len(autres_fichiers)):
       liste_comparaison=récupérationm(autres_fichiers[i])
       for k in range (len(liste_methode)):
           for j in range (len(liste_comparaison)):
               m=similarite_methode(liste_methode[k],liste_comparaison[j])
               liste_similarite.append(m)
   max=max(liste_similarite)
   indice_max=[i for i, j in enumerate(liste_similarite) if j == max]
   return(max,indice_max)

print(comparaison_methode('EventCandadatA.rb',('EventCandaidateATrich.rb')))

def comparaison_nom_methode(fichier,*autres_fichiers):
   '''
   :param fichier: fichier à analyser
   :param autres_fichiers: autres fichiers qui sont comparés au fichier à analyser
   :return: tuple avec le poucentage de similarité le plus élevé et l'incide du fichier qui correspond avec ce pourcentage
   '''
   liste_nom_methode=trouver_nom_fonction(fichier)+trouver_scopes(fichier)
   liste_similarite=[]
   for i in range (len(autres_fichiers)):
       liste_comparaison=trouver_nom_fonction(autres_fichiers[i])+trouver_scopes(autres_fichiers[i])
       for k in range (len(liste_nom_methode)):
           for j in range (len(liste_comparaison)):
               m=similarite_methode(liste_nom_methode[k],liste_comparaison[j])
               liste_similarite.append(m)
   max=max(liste_similarite)
   indice_max=[i for i, j in enumerate(liste_similarite) if j == max]
   return(max,indice_max)
