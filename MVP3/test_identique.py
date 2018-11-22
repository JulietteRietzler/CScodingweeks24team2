import pytest
from MVP3.identique import *

def test_nombre_moyen_identique_methodes():
   assert type(nombre_moyen_identique_methodes('EventCandidatA.rb',('EventCandidatATrich.txt')))==float
