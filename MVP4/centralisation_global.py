from MVP1.collecte_de_données import *
from MVP2.collecte_de_données_MVP2 import *
from MVP3.centralisation import *


def resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test):
    '''
    :param fichier: fichier du candidat
    :param fichier_test: fichier contenant les tests du candidats
    :param autres_fichiers: liste contenant les autres fichiers de la base de données
    :param autres_fichiers_test: liste contenant les autres fichiers de test de la base de données
    :return: les différents résultats des 3 premiers MVP
    '''
    d=resultats(fichier,fichier_test)[1]
    d.update(donnees(fichier)[1])
    d.update(resultats_comparaison(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1])
    return(json.dumps(d,indent=4),d)

print(resultat_final('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb']))
