def sucesion(a, b, u, n):
    u = a*u+b
    n -= 1
    
    # Creamos una lista que contenga el valor de u que corresponda a la posición
    # correcta dentro de la sucesión.
    lista_sucesion = [u]
    
    # Si n != 1 (1 es último termino de la sucesión) extenderá la lista
    # recurriendo la función hasta que n sea 1. Tras finalizar la recursión,
    # lista_sucesion será una lista con 'n' terminos.
    if (n != 1):
        lista_sucesion.extend(sucesion(a, b, u, n))
    
    return lista_sucesion

a = int(input("Dígame el valor de a: "))
b = int(input("Dígame el valor de b: "))
u0 = int(input("Dígame el valor de U(0): "))
n = int(input("Dígame cuantos terminos quieres: "))

lista_sucesion = [u0]

lista_sucesion.extend(sucesion(a, b, u0, n))

print(lista_sucesion)