'''
Created on 3 oct. 2017

@author: juamar
'''
num_palabras = int(input("Dígame cuántas palabras tiene la lista: "))

if num_palabras <= 0:
    print("¡Imposible!")
else:
    lista_palabras = list()
    
    for i in range(num_palabras):
        lista_palabras.append(input("Dígame la palabra {}: ".format(i + 1)))

    print("La lista creada es: ", lista_palabras)