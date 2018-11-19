import pytest
from MVP2.similarité import *

def test_similarite():
   assert type(similarite("str1","str2"))==float
   assert 0<=similarite("str1","str2")<=1


def test_tableau_ressemblance():
   assert type(tableau_ressemblance(['tuv','xyz','abc']))==np.ndarray
   for i in range(len(['tuv','xyz','abc'])):
       for j in range(len(['tuv','xyz','abc'])):
           assert 0<=tableau_ressemblance(['tuv','xyz','abc'])[i][j]<=1


def test_ressemblance():
   assert 0<=ressemblance(np.array([[0.9,1],[0.5,0.08]]))<=1


def test_pourcentage_de_ressemblance_code():
   assert type(pourcentage_de_ressemblance_code('EventCandidatA.rb'))==float
   assert 0<=pourcentage_de_ressemblance_code('EventCandidatA.rb')<=1

