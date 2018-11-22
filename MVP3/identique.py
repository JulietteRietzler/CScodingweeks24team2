from MVP3.similarité_méthode import *
from MVP2.validité_nom import *

def nombre_moyen_identique_methodes(fichier,*autres_fichiers):
   '''
   :param fichier: fichier à analyser
   :param autres_fichiers: autres fichiers qui sont comparés au fichier à analyser
   :return: nombre moyen de noms identiques pour les tests du fichiers à analyser et les tests des autres fichiers
   '''
   liste_nom=trouver_nom_fonction(fichier)+trouver_scopes(fichier)
   n=len(liste_nom)
   liste_moyenne=[]
   for i in range (len(autres_fichiers)):
       m=0
       liste_autre_nom=trouver_nom_fonction(autres_fichiers[i])+trouver_scopes(autres_fichiers[i])
       for k in range(n):
           for j in range(len(liste_autre_nom)):
               if identique(str(liste_nom[k]),str(liste_autre_nom[j])):
                   m+=1
       m=m/n
       liste_moyenne.append(m)
   moyenne=sum(liste_moyenne[i] for i in range(len(liste_moyenne)))/len(liste_moyenne)
   return(moyenne)

#print(nombre_moyen_identique_methodes('EventCandidatA.rb',('EventCandidatATrich.txt')))
