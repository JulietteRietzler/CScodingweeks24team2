
def récupérationt(fichier):
    '''
    :param fichier: le fichier à analyser
    :return: une liste des tests contenus dans le fichier.
    '''
    with open(fichier,'r')as code:
        codelignes=code.readlines()
        liste_tests=[]
        index=0
        while index<len(codelignes):
            if "test" in codelignes[index] and "do\n" in codelignes[index] :
                compteur=index+1
                while 'end\n' not in codelignes[compteur]:
                    compteur+=1
                liste_tests.append(codelignes[index:compteur+1])
                index=compteur
            else:
                index+=1
        return(liste_tests)

#print(récupérationt('EventCandidatATest.rb'))
