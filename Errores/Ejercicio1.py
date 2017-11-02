def obtener_divisores(num):
    divisores = []

    i = 1
    while i <= num**(1/2):
        if num % i == 0:
            divisores.append(i)

            if i**2 != num:
                divisores.append(num // i)

        i += 1

    divisores.sort()
    return divisores

try:
    numero = int(input())

    print(obtener_divisores(numero))
except ValueError:
    print("El valor debe de ser un entero.")