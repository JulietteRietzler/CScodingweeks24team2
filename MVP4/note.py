from MVP4.centralisation_global import *

def note_assert_par_test(evaluation):
   nb_assert_par_test = evaluation["nombre moyen d'asserts par test"]
   if nb_assert_par_test >= 3 :
       return 3
   return (nb_assert_par_test - 1) * 3/2

def note_long_nom_fonction(evaluation):
   longueur_moyenne_nom_fonctions = evaluation["moyenne longueur nom des fonctions"]
   if longueur_moyenne_nom_fonctions >= 15 :
       return 1.5
   return longueur_moyenne_nom_fonctions * 0.1

def note_long_nom_variables(evaluation):
   long_moyenne_nom_variables = evaluation["nom des variables"]
   if long_moyenne_nom_variables >= 8 :
       return 1
   return long_moyenne_nom_variables * 1/8

def aeration(evaluation) :
   pourcentage_aeration = evaluation["pourcentage d'aeration"]
   if pourcentage_aeration >= 0.2 :
       return 1
   return pourcentage_aeration * 5

def plus_d_une_lettre(evaluation) :
   if evaluation["nom de variable trop court"] :
       return 1

def note_candidat(fichier, fichier_test, autres_fichiers, autres_fichiers_test):
    '''
    :param fichier: fichier du candidat
    :param fichier_test: fichier contenant les tests du candidats
    :param autres_fichiers: liste contenant les autres fichiers de la base de données
    :param autres_fichiers_test: liste contenant les autres fichiers de test de la base de données
    :return: la note du candidat sur 20
    '''
    total = 17.5
    note = 0
    note += resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1]["rapport nombre de fonctions et nombre de commentaires"] * 4
    note += resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1]["rapport nombre de fonctions et nombre de tests"] * 2
    note += note_assert_par_test(resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1])
    note += note_long_nom_fonction(resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1])
    note += note_long_nom_variables(resultat_final(fichier, fichier_test, autres_fichiers,autres_fichiers_test)[1])
    note += aeration(resultat_final(fichier, fichier_test, autres_fichiers,autres_fichiers_test)[1])
    note += resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1]["nom de variable correcte"]
    note += (1-resultat_final(fichier, fichier_test, autres_fichiers, autres_fichiers_test)[1]["duplication probable"] )* 4
    return(note / total * 20)


