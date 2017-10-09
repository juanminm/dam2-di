'''
Created on 27 sept. 2017

@author: juamar
'''
def isVowel(char):
    if (char.lower() in ("a", "e", "i", "o", "u")):
        return True
    else:
        return False


print(isVowel("e"))
print(isVowel("b"))
print(isVowel("U"))