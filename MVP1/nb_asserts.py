from MVP1.nb_tests import *

def words(doc):
   words = []
   with open(doc, "r") as file :
       for line in file :
           words = words + line.split(" ")
   return words

def nb_de_asserts(doc) :
   compteur = 0
   liste = words(doc)
   for mot in liste :
       if mot == "assert" or mot == "assert_not" or mot == "assert_equal":
           compteur += 1
   return compteur

def nb_moyen_de_asserts_par_test(test) :
   try :
       if nb_de_tests(test) != 0 :
           return nb_de_asserts(test)/nb_de_tests(test)
   except :
       print("ZeroDivisionError")
