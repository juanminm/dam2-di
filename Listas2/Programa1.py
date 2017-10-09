def crear_lista(num):
    lista = list()

    for i in range(num):
        lista.append(input("Dígame la palabra {}: ".format(i + 1)))

    return lista

num_palabras = int(input("Dígame cuántas palabras tiene la primera lista: "))

if num_palabras <= 0:
    print("¡Imposible!")
else:
    primera_lista = crear_lista(num_palabras)
    lista_ordenada = primera_lista.copy()
    lista_ordenada.sort()

    print("La lista creada es:", primera_lista)
    print("La lista ordenada es:", lista_ordenada)

