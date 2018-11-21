import pytest
from MVP2.collecte_de_données_MVP2 import *

def test_resultats():
    assert type(resultats('EventCandidatA.rb'))==str
