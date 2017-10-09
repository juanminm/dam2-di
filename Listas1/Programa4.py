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

    palabra_a_sustituir = input("Palabra a eliminar: ")

    while lista_palabras.count(palabra_a_sustituir) > 0:
        lista_palabras.remove(palabra_a_sustituir)

    print("La lista es ahora:", lista_palabras)