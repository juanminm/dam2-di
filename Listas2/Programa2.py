lista = list()
num = int(input("Dígame un numero: "))

i = 1
limit = num ** 0.5

# Empiezo el loop desde 1 y termino cuando i supere la raiz del número.
while i <= limit:
    # Si el número es divisible por i, el resto será 0 y lo añadimos a la lista.
    if num % i == 0:
        lista.append(i)

        # Añadiendo a lo de arriba: si numero / i = j, numero / j = i.
        #
        # En caso de cuadrados perfectos (4, 9, 16,...), se omite j cuando es igual a i para que no haya
        # repeticiones como en el caso de 4 que mostraría dos 2's.
        j = num/i
        if (i != j):
            lista.append(int(num/i))

    i += 1

lista.sort()

print("{} tiene {} divisores {}".format(num, len(lista), lista))