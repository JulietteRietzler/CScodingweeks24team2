from MVP4.note import *
from MVP3.centralisation import *

def niveau_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test):
    '''
    :param fichier: fichier du candidat
    :param fichier_test: fichier contenant les tests du candidats
    :param autres_fichiers: liste contenant les autres fichiers de la base de données
    :param autres_fichiers_test: liste contenant les autres fichiers de test de la base de données
    :return: le niveau estimé du candidat
    '''
    niveau=''
    if note_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test)>=16:
        niveau='tres bon'
    elif 14<=note_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test)<16:
        niveau='bon'
    elif 12<=note_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test)<14:
        niveau='assez bon'
    elif 10<=note_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test)<12:
        niveau='passable'
    else:
        niveau='mauvais'
    if resultats_comparaison(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1]["fraude probable"]==True:
        return(niveau+'\n Attention, il y a probablement une fraude!')
    else:
        return(niveau)
