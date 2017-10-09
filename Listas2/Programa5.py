def sucesion(u, n):
    if (u % 2 == 0):
        u = u / 2
    else:
        u = 3 * u + 1
    
    # Creamos una lista que contenga el valor de u que corresponda a la posición
    # correcta dentro de la sucesión.
    # correcta dentro de la sucesión.
    lista_sucesion = [u]
    n -= 1
    
    # Si n != 1 (1 es último termino de la sucesión) extenderá la lista
    # recurriendo la función hasta que n sea 1. Tras finalizar la recursión,
    # lista_sucesion será una lista con 'n' terminos.
    if (n != 1):
        lista_sucesion.extend(sucesion(u, n))
    
    return lista_sucesion

u0 = int(input("Dígame el valor de U(0): "))
n = int(input("Digame cuántos términos quieres: "))

lista_sucesion = [u0]

lista_sucesion.extend(sucesion(u0, n))

print(lista_sucesion)