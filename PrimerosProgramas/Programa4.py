'''
Created on 27 sept. 2017

@author: juamar
'''
def isVowel(char):
    if (char.lower() in ("a", "e", "i", "o", "u")):
        return True
    else:
        return False
    
s = "buenas tardes, soy juan miguel"
cont = 0

for i in (range(len(s))):
    if isVowel(s[i]):
        cont += 1

print("Numero de vocales: ", cont)