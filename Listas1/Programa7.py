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
    print("La lista creada es: ", lista_palabras)
    for palabra in lista_palabras:
        i = lista_palabras.index(palabra) + 1

        while i < len(lista_palabras):
            if palabra == lista_palabras[i]:
                lista_palabras.pop(i)

            i += 1

    print("La lista es ahora:", lista_palabras)