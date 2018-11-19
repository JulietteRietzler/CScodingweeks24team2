def nb_de_fonctions(Nom,localisation = "") :
   """ retourne le nombre de fonction d'un fichier """
   fichier = open(Nom,'r')
   mots = []
   for line in fichier :
       mots += line.split(' ')
   return(mots.count('def')+mots.count('scope'))
