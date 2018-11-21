from difflib import SequenceMatcher

def identique(str1, str2):
   '''
   :param str1,str2: deux chaînes de caractères à comparer
   :return: true si elles sont identiques, false sinon
   '''
   a=SequenceMatcher(None, str1, str2).ratio()
   if a==1:
       return(True)
   else:
       return(False)

def similatite_methode(methode1,methode2):
   '''
   :param methode1,methode2: deux chaines de carctères de codes de deux méthodes à comparer
   :return:
   '''
   return(SequenceMatcher(None, methode1, methode2).ratio())
