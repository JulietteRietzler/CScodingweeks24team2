
def nb_lines(code):

   nb_lines = 0

   with open(code, "r") as file:
       for line in file:
           nb_lines += 1

   return nb_lines



def pourcentage_d_espaces(code) :

   saut_de_ligne = 0
   nb_de_lignes = nb_lines(code)
   mots = []

   with open(code, "r") as file :

       for line in file :
           mots = mots + line.split(" ")

       l = len(mots)

       for i in range(3,l) :
           if mots[i] == "\n" and not (mots[i-3] == "\n" and mots[i-2] == "\n" and mots[i-1] == "\n") :
               saut_de_ligne += 1

   return saut_de_ligne/nb_de_lignes
