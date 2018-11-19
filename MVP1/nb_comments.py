

def nombre_de_commentaires(fichier):
    '''
    :param file: nom du fichier à analyser
    :return: le nombre de commentaires présents dans le fichier
    '''
    with open(fichier,'r') as fichier_candidat:
        nb_commentaires=0
        lines=fichier_candidat.read()
        for character in lines:
            if character == '#':
                nb_commentaires+=1
        return nb_commentaires

print(nombre_de_commentaires("EventCandidatATest.rb"))

