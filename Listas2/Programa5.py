def sucesion(u, n):
    if (u % 2 == 0):
        u = u / 2
    else:
        u = 3 * u + 1

    lista_sucesion = [u]
    n -= 1

    if (n == 1):
        return lista_sucesion
    else:
        lista_sucesion.extend(sucesion(u, n))

        return lista_sucesion

u0 = int(input("Dígame el valor de U(0): "))
n = int(input("Digame cuántos términos quieres: "))

lista_sucesion = [u0]

lista_sucesion.extend(sucesion(u0, n))

print(lista_sucesion)