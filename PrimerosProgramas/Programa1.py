'''
Created on 27 sept. 2017

@author: juamar
'''
varA = "Juan"
varB = 1

if (type(varA) == str or type(varB) == str):
    print("Cadena involucrada")
else:
    if (varA > varB):
        print("Grande")
    elif (varA < varB):
        print("Más pequeño")
    else:
        print("Igual")