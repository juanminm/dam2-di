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

    num_palabras = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))
    if num_palabras <= 0:
        print("No hay nada que borrar. La lista se queda como: ", lista_palabras)
    else:
        lista_para_borrar = crear_lista(num_palabras)
        print("La lista de palabras a eliminar es:", lista_para_borrar)

        for palabra in lista_para_borrar:
            while lista_palabras.count(palabra) > 0:
                lista_palabras.remove(palabra)

        print("La lista es ahora:", lista_palabras)