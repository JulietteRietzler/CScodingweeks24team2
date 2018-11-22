import pytest
from MVP1.collecte_de_données import *
from MVP1.nb_comments import *
from MVP1.nb_fonctions import *
from MVP1.nb_tests import *
from MVP1.nb_asserts import *

def test_resultats():
    assert type(nombre_de_commentaires('EventCandidatATest.rb'))==int
    assert type(nb_de_fonctions('EventCandidatATest.rb'))==int
    assert type(nb_de_tests('EventCandidatATest.rb'))==int
    assert type(nb_moyen_de_asserts_par_test('EventCandidatATest.rb'))== float
    assert type(resultats('EventCandidatA.rb','EventCandidatATest.rb')[0])==str
    assert type(resultats('EventCandidatA.rb','EventCandidatATest.rb')[1])==dict


