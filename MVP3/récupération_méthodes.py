def indentation(ligne):
    '''
    :param ligne: un string
    :return: l'indentation au début de la ligne
    '''
    indentation=0
    i=0
    while ligne[i]==' ':
        i+=1
        indentation+=1
    return indentation

def récupérationm(fichier):
    '''
    :param fichier: le fichier à analyser.
    :return: une liste des différentes méthodes.
    '''
    with open(fichier,'r')as code:
        codelignes=code.readlines()
        liste_méthodes=[]
        index=0
        while index<len(codelignes):
            if "def " in codelignes[index]:
                compteur=index+1
                while indentation(codelignes[compteur])>=indentation(codelignes[index+1]):
                    compteur+=1
                liste_méthodes.append(codelignes[index:compteur+2])
                index=compteur
            elif "scope " in codelignes[index]:
                compteur=index
                if indentation(codelignes[compteur])>indentation(codelignes[index]):
                    compteur+=1
                liste_méthodes.append(codelignes[index:compteur+1])
                index+=1
            else:
                index+=1
        return(liste_méthodes)

print(récupérationm('EventCandidatA.rb'))
