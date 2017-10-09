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
    
palabra_buscar = input("Dígame la palabra a buscar: ")
contar_palabra = 0 
 
for i in range(num_palabras):
    if lista_palabras[i] == palabra_buscar:
        contar_palabra += 1
        
if contar_palabra == 0:
    print("La palabra '{}' no aparece en la lista.".format(palabra_buscar))
else:
    print("La palabra '{}' aparece {} veces en la lista.".format(palabra_buscar, contar_palabra))