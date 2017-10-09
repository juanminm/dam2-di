'''
Created on 27 sept. 2017

@author: juamar
'''
def isVowel(char):
    if (char.lower() == "a" or char.lower() == "e" or char.lower() == "i"
        or char.lower() == "o" or char.lower() == "u"):
        
        return True
    else:
        return False


print(isVowel("e"))
print(isVowel("b"))
print(isVowel("U"))