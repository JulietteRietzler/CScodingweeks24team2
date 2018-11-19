def nb_de_tests(doc):
   """
   Compter le nombre de tests effectués par le candidat. On estime qu'un test correspond au nombre de lignes commençant
   par test et finissant par do.
   :param doc : document à analyser
   :return: entier
   """
   words = []
   compteur = 0
   with open(doc, "r") as file :
       for line in file :
           words = line.split(" ")
           # print(words)
           l = len(words)
           if "test" in words and (words[l-1] == "do\n" or words[l-1] == "do") :
               compteur +=1
   return compteur
