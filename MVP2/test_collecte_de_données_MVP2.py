import pytest
from MVP2.collecte_de_données_MVP2 import *

def test_donnees():
    assert type(donnees('EventCandidatA.rb')[0])==str
    assert type(donnees('EventCandidatA.rb')[1])==dict
