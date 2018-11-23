from MVP4.centralisation_global import *
from MVP4.evaluation import *

def produit(fichier, fichier_test, autres_fichiers, autres_fichiers_test):
    '''
    :param fichier: fichier du candidat
    :param fichier_test: fichier contenant les tests du candidats
    :param autres_fichiers: liste contenant les autres fichiers de la base de données
    :param autres_fichiers_test: liste contenant les autres fichiers de test de la base de données
    :return: le produit final: l'ensemble des métriques et le niveau estimé du candidat
    '''
    return(resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[0],note_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test),niveau_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test))

def affichage(fichier, fichier_test, autres_fichiers, autres_fichiers_test):
    '''
    :param fichier: fichier du candidat
    :param fichier_test: fichier contenant les tests du candidats
    :param autres_fichiers: liste contenant les autres fichiers de la base de données
    :param autres_fichiers_test: liste contenant les autres fichiers de test de la base de données
    :return: un fichier json contenat toutes les informations
    '''
    d=resultats(fichier,fichier_test)[1]
    d.update(donnees(fichier)[1])
    d.update(resultats_comparaison(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1])
    d["note du candidat"]=note_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test)
    d["niveau du candidat"]=niveau_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test)
    return(json.dumps(d,indent=4))

print(affichage('EventCandidatA.rb','EventCandidatATest.rb', ['event_candidate_b.rb','event_candidate_c.rb'],['event_candidate_b_test.rb','event_candidate_c_test.rb']))
