def sucesion(a, b, u, n):
    u = a*u+b
    n -= 1

    lista_sucesion = [u]


    if (n == 1):
        return lista_sucesion
    else:
        lista_sucesion.extend(sucesion(a, b, u, n))

        return lista_sucesion

a = int(input("Dígame el valor de a: "))
b = int(input("Dígame el valor de b: "))
u0 = int(input("Dígame el valor de U(0): "))
n = int(input("Dígame cuantos terminos quieres: "))

lista_sucesion = [u0]

lista_sucesion.extend(sucesion(a, b, u0, n))

print(lista_sucesion)