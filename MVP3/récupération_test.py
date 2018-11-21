
def récupérationt(fichier):
    with open(fichier,'r')as code:
        codelignes=code.readlines()
        liste_test=[]
        index=0
        while index<len(codelignes):
            if "test" in codelignes[index] and "do\n" in codelignes[index] :
                compteur=index+1
                while 'end\n' not in codelignes[compteur]:
                    compteur+=1
                liste_test.append(codelignes[index:compteur+1])
                index=compteur
            else:
                index+=1
        return(liste_test)

print(récupérationt('EventCandidatATest.rb'))
