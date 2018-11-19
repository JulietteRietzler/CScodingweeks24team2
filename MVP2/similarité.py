from difflib import SequenceMatcher
import numpy as np
from MVP2.decoupage_code import *

def similarite(str1, str2):
   '''
   :param str1,str2: deux chaînes de caractères à comparer
   :return: la ressemblance entre les deux chaînes de caractères type float  entre 0 et 1
   '''
   return SequenceMatcher(None, str1, str2).ratio()


def tableau_ressemblance(liste):
   '''
   :param list: liste de chaine de caractère
   :return: la similarité entre les éléments de la liste dans un tableau
   '''
   n=len(liste)
   tableau=np.zeros((n,n))
   for i in range(n):
       for j in  range(i,n):
           tableau[i][j]= similarite(liste[i],liste[j])
   return(tableau)

def ressemblance(tableau):
   '''
   :param tableau: tableau_ressemblance avec chiffre entre 0 et 1
   :return: le pourcentage de ressemblance d'une partie du code
   '''
   n=len(tableau)
   m=0
   if n!=0:
      for i in range(n):
         for j in range(n):
               m+=tableau[i][j]
      m=m/n**2
      return(m)
   else:
      print('erreur')

print(ressemblance(np.array([[0.9,1],[0.5,0.08]])))

def pourcentage_de_ressemblance_code(fichier):
   decoupage=decoupage_du_code(fichier)
   tableau_debut=tableau_ressemblance(decoupage[0])
   tableau_if=tableau_ressemblance(decoupage[1])
   tableau_for=tableau_ressemblance(decoupage[2])
   tableau_while=tableau_ressemblance(decoupage[3])
   tableau_until=tableau_ressemblance(decoupage[4])
   pourcentage= ressemblance(tableau_debut)+ressemblance(tableau_if)+ressemblance(tableau_for)+ressemblance(tableau_while)+ressemblance(tableau_until)
   return(pourcentage/5)

print(pourcentage_de_ressemblance_code('EventCandidatA.rb'))
