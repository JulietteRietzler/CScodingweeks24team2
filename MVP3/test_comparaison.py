import pytest
from MVP3.comparaison import *

fichier='EventCandidatA.rb'
autres_fichiers=['EventCandidatATrich.txt']
fichier_test='EventCandidatATest.rb'

def test_comparaisons():
   assert type(comparaison_test(fichier_test,autres_fichiers))==tuple
   assert type(comparaison_methode(fichier,autres_fichiers))==tuple
   assert type(comparaison_nom_methode(fichier,autres_fichiers))==tuple
   assert 0<comparaison_test(fichier_test,autres_fichiers)[0]<=1
   assert 0<comparaison_methode(fichier,autres_fichiers)[0]<=1
   assert 0<comparaison_nom_methode(fichier,autres_fichiers)[0]<=1
   assert type(comparaison_test(fichier_test,autres_fichiers)[1])==list
   assert type(comparaison_methode(fichier,autres_fichiers)[1])==list
   assert type(comparaison_nom_methode(fichier,autres_fichiers)[1])==list
