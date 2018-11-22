import regex as re


def indice(l,x) :
    """retourne l'indice de l'élément x dans la liste l """
    for i in range(len(l)) :
        if l[i] == x :
            return(i)

def Ajoute_arguments(liste_arg) :
        """Pour une liste de string, sépare le nom d'une fct de ses arguments
        exemple : Ajoute_arguments(['Sum(a,b)']) = ['Sum','a','b'] """
        liste = []
        for mots in liste_arg :
            if '(' in mots and ',' in mots :
                i = indice(mots,'(')
                liste.append(mots[0:i])
                ttarguments = mots[i+1:len(mots)-1]
                liste += ttarguments.split(',')
            elif '(' in mots :
                i = indice(mots,'(')
                liste.append(mots[0:i])
                liste.append(mots[i+1:len(mots)-1])
            else :
                liste.append(mots)
        return(liste)

def enleve_variable_en_egal(liste) :
    """Pour une liste de string enleve les termes du string apres un =
    exemple : enleve_variable_en_egal(['Heure = 12']) = ['Heure'] """
    for mots in liste :
        if '=' in mots :
            i = indice(mots,'=')
            bon_mots= mots[0:i]
            liste.remove(mots)
            liste.append(bon_mots)
    return(liste)

def enleve_espace_string(str) :
    """enleve tous les espaces des termes d'une liste de strings"""
    res = ''
    for x in str :
        if x != ' ' :
            res+=x
    return(res)

def trouver_nom_fonction(Nom) :
    """En partant d'un fichier Ruby, retourne tous les noms de variables
    de fonctions et leurs arguments"""
    fichier = open (Nom,'r')
    fichier_string = fichier.read()
    liste_variable = []
    liste_variable += re.findall("def +(.+)\n+",fichier_string)
    L = Ajoute_arguments(liste_variable)
    reste_espace = enleve_variable_en_egal(L)
    for i in range(len(reste_espace)) :
        reste_espace[i] = enleve_espace_string(reste_espace[i])
    return(reste_espace)



def supprimer_blancs_de_liste(liste):
    '''
   Supprimer les blancs d'une liste
   :param : liste
   :return : liste sans blancs
   '''
    new_list = []
    for mot in liste :
       if not (mot == '' or mot == " "):
           new_list.append(mot)
    return(new_list)



def supprimer_doublons(liste):
   """Prend une liste en argument et retourne une liste sans doublons"""
   image = liste[:]
   resultat = []
   for elem in image :
       liste.remove(elem)
       if not elem in liste :
           resultat.append(elem)
   return(resultat)

def trouver_variables(doc):
    '''
    Cherche les noms des variables globales et locales du fichier dans le cas où le fichier ne comprend pas de variables
    nommées sous la forme a,b = 1,2
    :param : doc
    :return: liste des noms des variables
    '''

    # petit problème : a,b = 1,2

    file = open(doc,"r")
    file_string = file.read()
    #print(file_string)

    variable1 = re.findall("(\w*)=",file_string)
    variable2 = re.findall("(\w*) =",file_string)
    variable = supprimer_doublons(variable1 + variable2)
    return supprimer_blancs_de_liste(variable)

def trouver_scopes(doc):
    '''
    Cherche les noms des scopes
    :param doc: fichier
    :return: liste des noms des scopes
    '''

    file = open(doc,"r")
    file_string = file.read()
    #print(file_string)

    scope = re.findall("scope *: *(\w*) *,",file_string)

    return supprimer_doublons(scope)

def moyenne_longueur_variables(doc) :
    """Retourne la longuer moyenne des variables utilisés dans un fichier de code"""
    variables = supprimer_doublons( trouver_variables(doc))
    if variables == [] :
        return('Pas de variable détectée')
    else :
        sum = 0
        for mots in variables :
            sum += len(mots)
        return(float(sum)/len(variables))

def moyenne_longueur_nom_fonction(doc):
    """Retourne la longuer moyenne des noms de fonction utilisés dans un fichier de code"""
    fonctions = supprimer_doublons( trouver_nom_fonction(doc) + trouver_scopes(doc))
    if fonctions == [] :
        return('Pas de fonction détectée')
    else :
        sum = 0
        for mots in fonctions :
            sum += len(mots)
        return(float(sum)/len(fonctions))

def critere_variable_pas_trop_court(doc):
    '''Retourne True si le candidat n'utilises pas de variables de longueur 1'''
    variables = supprimer_doublons( trouver_scopes(doc) + trouver_variables(doc) + trouver_nom_fonction(doc))
    for mots in variables :
        if len(mots) == 1 :
            return(False)
    return(True)

