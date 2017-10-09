def es_primo(n):
    # Comprueba si el número es 2 o 3.
    if n in (2, 3):
        return True
    # Comprueba si el número es multiplo de 2 o 3
    if n % 2 == 0 or n % 3 == 0:
        return False


    # Empezando desde 5: si el modulo de la division n con i o n con (i + 2) es 0, entonces no es primo. En caso de no
    # serlo, se le añade 6 a i hasta que el cuadrado de i sea mayor que n.
    # Si no ha devuelto "False" se considera como primo el numero n.
    #
    # Ej, con 29
    #
    # 29 no es ni 2, ni 3, ni divisible por ambos.
    #
    # i = 5 y el cuadrado de i (25) es menor que 29
    #
    # El modulo de 29 dividido por 5 es 4 y el modulo de 29 divido por 7 (5 + 2)  es 1, por lo que no es no-primo por
    # ahora. Se le suma 6 a i, que es 11. El cuadrado de 11 es 121 y por lo tanto mayor que 29. Como ha pasado todas las
    # comprobaciones anteriores, el numero 29 es primo.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6

    return True

lista = list()
num = int(input("Dígame un numero: "))

i = 1
while i <= num:
    if(es_primo(i)):
        lista.append(i)
    i += 1


print("Primos hasta {}: {}".format(num, lista))