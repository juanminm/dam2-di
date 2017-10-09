def crear_lista(num):
    lista = list()

    for i in range(num):
        lista.append(input("Dígame la palabra {}: ".format(i + 1)))

    return lista

def eliminar_repeticiones(lista):
    for palabra in lista:
        i = lista.index(palabra) + 1

        while i < len(lista):
            if palabra == lista[i]:
                lista.pop(i)

            i += 1

    return lista

def union_listas(lista1, lista2):
    lista1.extend(lista2)

    return eliminar_repeticiones(lista1)

def diferencia_listas(lista1, lista2):
    lista1 = eliminar_repeticiones(lista1)
    lista2 = eliminar_repeticiones(lista2)
    for palabra in lista2:
        while lista1.count(palabra) > 0:
            lista1.remove(palabra)

    return lista1

def interseccion_listas(lista1, lista2):
    lista1 = eliminar_repeticiones(lista1)
    lista2 = eliminar_repeticiones(lista2)

    for palabra in lista1:
        if lista2.count(palabra) == 0:
            lista1.remove(palabra)

    for palabra in lista2:
        if lista1.count(palabra) == 0:
            lista2.remove(palabra)

    return union_listas(lista1, lista2)


num_palabras = int(input("Dígame cuántas palabras tiene la primera lista: "))

if num_palabras <= 0:
    print("¡Imposible!")
else:
    primera_lista = crear_lista(num_palabras)
    print("La primera lista es: ", primera_lista)

    num_palabras = int(input("Dígame cuántas palabras tiene la segunda lista: "))
    if num_palabras <= 0:
        print("No se pueden comparar las lista, ya que no existe una segunda lista")
    else:
        segunda_lista = crear_lista(num_palabras)
        print("La segunda lista es: ", segunda_lista)

        print("Palabras que aparecen en las dos lista:", interseccion_listas(primera_lista.copy(), segunda_lista.copy()))
        print("Palabras que solo aparecen en la primera lista:", diferencia_listas(primera_lista.copy(), segunda_lista.copy()))
        print("Palabras que solo aparecen en la segunda lista:", diferencia_listas(segunda_lista.copy(), primera_lista.copy()))
        print("palabras que aparecen en las dos lista:", union_listas(primera_lista.copy(), segunda_lista.copy()))

