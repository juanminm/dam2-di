'''
Created on 3 oct. 2017

@author: juamar
'''
def crear_lista(num):
    lista = list()

    for i in range(num):
        lista.append(input("Dígame la palabra {}: ".format(i + 1)))

    return lista

num_palabras = int(input("Dígame cuántas palabras tiene la lista: "))
if num_palabras <= 0:
    print("¡Imposible!")
else:
    lista_palabras = crear_lista(num_palabras)
    lista_inversa = lista_palabras.copy()

    lista_inversa.reverse()
    print("La lista creada es:", lista_palabras)
    print("La lista inversa es:", lista_inversa)