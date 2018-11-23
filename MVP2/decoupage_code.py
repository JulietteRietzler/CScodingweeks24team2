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

def decoupage_du_code(fichier):
    '''
    :param fichier: fichier à analyser
    :return: 5 listes dans lesquelles sont recensées respectivement les débuts de fonction, les boucles if, for, while et
    until
    '''
    with open(fichier,'r')as code:
        index=0
        codelignes=code.readlines()
        splitDebut=[]
        splitIf=[]
        splitFor=[]
        splitWhile=[]
        splitUntil=[]
        for ligne in codelignes:
            if 'def ' in ligne:
                compteur=index+1
                while 'if ' not in codelignes[compteur] and 'for ' not in codelignes[compteur] and 'while ' not in codelignes[compteur] and 'until ' not in codelignes[compteur] and 'end\n' not in codelignes[compteur]:
                    compteur+=1
                splitDebut.append(codelignes[index+1:compteur+1])
            elif 'if ' in ligne:
                compteur=index+1
                while indentation(codelignes[compteur])<indentation(codelignes[index]):
                    compteur+=1
                splitIf.append(codelignes[index:compteur+1])
            elif 'for ' in ligne:
                compteur=index+1
                while indentation(codelignes[compteur])<indentation(codelignes[index]):
                    compteur+=1
                splitFor.append(codelignes[index:compteur+1])
            elif 'while ' in ligne:
                compteur=index+1
                while indentation(codelignes[compteur])<indentation(codelignes[index]):
                    compteur+=1
                splitWhile.append(codelignes[index:compteur+1])
            elif 'until ' in ligne:
                compteur=index+1
                while indentation(codelignes[compteur])<indentation(codelignes[index]):
                    compteur+=1
                splitUntil.append(codelignes[index:compteur+1])
            index+=1
        return(splitDebut, splitIf, splitFor, splitWhile, splitUntil)


#print(decoupage_du_code('EventCandidatA.rb'))
